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
    page = browser.new_page(viewport={"width": 1400, "height": 1000})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.set_content(html)

    check("Parade-specific title", "Macy's 100th Parade" in page.title())
    check("Official closure count is 19", page.locator("#closure-count").inner_text() == "19")
    check("Schematic parade map visible", page.locator("#schematic").is_visible())
    check("Initial journey is unset", page.locator("#watch-status").inner_text() == "Not set")

    page.locator("#plan-form button[type=submit]").click()
    check("Journey watch starts", page.locator("#watch-status").inner_text() == "Active")
    check("Journey profile is summarized", "Brooklyn, NY" in page.locator("#active-plan").inner_text())
    check("Autopilot preference shown", "Autopilot: ON" in page.locator("#active-plan").inner_text())

    page.locator("#simulate-change").click()
    check("Autopilot adapts in-app advisory", "Auto-adapted your in-app plan" in page.locator("#change-alert").inner_text())
    check("Disruption remains clearly simulated", "hypothetical" in page.locator("#control-feed").inner_text().lower())

    page.locator("#autoadapt").uncheck()
    page.locator("#plan-form button[type=submit]").click()
    page.locator("#simulate-change").click()
    check("Manual approval required when autopilot off", "Decision needed" in page.locator("#change-alert").inner_text())
    page.locator("#apply-change").click()
    check("Manual alternative approval works", page.locator("#change-alert").is_hidden())

    page.locator('[data-tab="watch"]').click()
    check("City watch view opens", page.locator("#watch-view").is_visible())
    check("All 19 official schedule entries render", page.locator("#closure-list .closure").count() == 19)
    check("Official city notice linked", "thanksgiving-standard-street-closures-2026.pdf" in page.locator("#watch-view a").get_attribute("href"))

    page.locator("#report-area").select_option(label="Sixth Avenue")
    page.locator("#report-detail").fill("Crowds are building near the corner")
    page.locator("#report-form button[type=submit]").click()
    check("Community report submitted as unverified", "UNVERIFIED" in page.locator("#report-list").inner_text())

    page.locator('[data-tab="control"]').click()
    check("Control room opens", page.locator("#control-view").is_visible())
    check("Control room shows source signals", page.locator("#control-feed .signal").count() >= 4)
    page.locator("#ops-reset").click()
    check("Demo signal reset works", page.locator("#control-feed .signal").count() == 3)

    page.locator('[data-tab="journey"]').click()
    page.evaluate("window.open = function(url){window.__openedUrl=url}")
    page.locator("#open-maps").click()
    url = page.evaluate("window.__openedUrl")
    params = parse_qs(urlparse(url).query)
    check("Google Maps handoff includes origin", params["origin"] == ["Brooklyn, NY"])
    check("Google Maps handoff includes destination", params["destination"] == ["Penn Station, New York, NY"])
    check("Google Maps handoff includes transit mode", params["travelmode"] == ["transit"])
    check("No desktop JavaScript errors", len(errors) == 0)

    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile_errors = []
    mobile.on("pageerror", lambda e: mobile_errors.append(str(e)))
    mobile.set_content(html)
    check("Mobile journey form visible", mobile.locator("#plan-form").is_visible())
    check("Mobile map visible", mobile.locator("#schematic").is_visible())
    check("No mobile horizontal overflow", mobile.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 2"))
    check("No mobile JavaScript errors", not mobile_errors)

    browser.close()

print("PASS", len(passed), "tests")
for item in passed:
    print(" -", item)
