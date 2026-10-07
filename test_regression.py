from pathlib import Path
from playwright.sync_api import sync_playwright
from urllib.parse import parse_qs, urlparse

html = Path(__file__).with_name("index.html").read_text()
passed = []

def check(name, condition):
    assert condition, name
    passed.append(name)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 950})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.set_content(html)
    check("Four initial incidents", page.locator(".incident").count() == 4)
    check("Default two route polylines", page.locator("#route-layer polyline").count() == 2)
    before = page.evaluate("window.__RALLY_TEST__.gridRoute('port').map(x=>x.id).join(',')")
    page.locator("#simulate-new").click()
    after = page.evaluate("window.__RALLY_TEST__.gridRoute('port').map(x=>x.id).join(',')")
    check("Verified closure changes schematic route", before != after)
    check("Scenario risk elevates", page.locator("#risk-stat").inner_text() == "ELEVATED")
    check("Incident appears in traveler feed", page.locator(".incident").count() == 5)
    page.locator('[data-filter="verified"]').click()
    check("Verified filter excludes eyewitness", page.locator(".incident").count() == 2)
    page.locator('[data-filter="all"]').click()
    page.locator("#rep-location").select_option("w36")
    page.locator("#rep-detail").fill("Very large crowd seen moving east on this street")
    page.locator("#report-form button[type=submit]").click()
    check("Community report is unverified", page.locator(".incident").count() == 6 and "UNVERIFIED" in page.locator(".incident").first.inner_text())
    report_id = page.evaluate("window.__RALLY_TEST__.state.incidents[0].id")
    check("Community report cannot block street", page.evaluate("window.__RALLY_TEST__.state.incidents[0].block.length===0"))
    page.locator('[data-view="ops"]').click()
    check("Operator desk visible", page.locator("#view-ops").is_visible())
    page.locator('[data-action="corroborate"][data-id="'+report_id+'"]').click()
    check("Corroboration is not official verification", page.evaluate("window.__RALLY_TEST__.state.incidents[0].status") == "corroborated")
    page.locator('[data-action="resolve"][data-id="i1"]').click()
    check("Resolved closure removes block", page.evaluate("window.__RALLY_TEST__.state.incidents.find(i=>i.id==='i1').status") == "resolved")
    page.locator("#ops-reset").click()
    check("Reset restores four incidents", page.evaluate("window.__RALLY_TEST__.state.incidents.length") == 4)
    page.locator('[data-view="travel"]').click()
    page.locator("#destination").select_option("herald")
    page.locator('[data-mode="transit"]').click()
    params = parse_qs(urlparse(page.evaluate("window.__RALLY_TEST__.mapURL()")).query)
    check("Google Maps URL populated", params["api"] == ["1"] and params["travelmode"] == ["transit"] and "Herald" in params["destination"][0])
    page.locator('[data-view="share"]').click()
    check("Distribution poster visible", page.locator("#poster").is_visible())
    check("QR disabled on nonpublic origin", page.locator("#qr-code").inner_text().strip().startswith("QR available"))
    check("QR encoder works", page.evaluate("(()=>{let qr=new QRCodeModel(-1,0);qr.addData('https://example.org/?event=knicks');qr.make();return qr.getModuleCount()>20})()"))
    check("No browser JavaScript errors", len(errors) == 0)
    page.locator('[data-view="travel"]').click()
    mobile = browser.new_page(viewport={"width":390, "height":844})
    mobile_errors = []
    mobile.on("pageerror", lambda e: mobile_errors.append(str(e)))
    mobile.set_content(html)
    check("Mobile map and planner visible", mobile.locator("#street-svg").is_visible() and mobile.locator("#destination").is_visible())
    check("Mobile has no horizontal overflow", mobile.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 2"))
    check("No mobile JavaScript errors", not mobile_errors)
    browser.close()
print("PASS", len(passed), "tests")
for item in passed:
    print(" -", item)
