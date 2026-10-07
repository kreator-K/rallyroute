# RallyRoute

**Event-aware journey intelligence for the moments when normal navigation isn't enough.**

RallyRoute is a **zero-download, mobile-friendly hackathon prototype** for fans and commuters leaving a major public event. It combines incident context, evidence labels, a simulated disruption-aware journey planner, and a familiar **Google Maps handoff**. The project uses a fictional New York Knicks championship celebration near Madison Square Garden to illustrate the concept.

> [!WARNING]
> **Demonstration only — not a live navigation or emergency service.** All event alerts, closure reports, source references, crowd information, route risks, and map detours are simulated. Never use these results to make real travel or safety decisions.

![RallyRoute product preview](preview.png)

## Try it in one minute

**No build tools, account, or API key required.**

1. [Download the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or open `index.html` locally in Chrome, Edge, Safari, or Firefox.
2. In **Traveler view**, select **Port Authority Bus Terminal** and review the simulated incidents and their evidence labels.
3. Select **Simulate new road closure** to see the schematic route change.
4. Submit a community report; notice that it remains **unverified**, rather than instantly blocking a road.
5. Switch to **Incident desk** to triage reports, review source states, reset the demo, or export incident JSON.
6. Open **Distribution kit** to preview the venue QR poster. QR code generation activates when the application is served from a public HTTPS URL.

If you prefer to run a local HTTP server:

```bash
python3 -m http.server 8000
```

Visit `http://localhost:8000`. The QR code remains disabled on localhost because attendees can't open your local address from their own phones.

## Features

| Feature | Prototype behavior |
| --- | --- |
| Event disruption map | Responsive Midtown schematic with mock closures, eyewitness reports and route overlays |
| Journey planning | Four sample destinations, three travel modes, and a simulated graph-based reroute |
| Evidence-first incident feed | Differentiates mocked official alerts, corroborated observations, and unverified submissions |
| Community reporting | Local report submission, operator triage, reset and JSON export (browser-session only) |
| Google Maps handoff | Opens a real Google Maps Directions URL for the selected origin, destination and mode |
| Optional Google Maps backdrop | Loads Google Maps JavaScript API when a user supplies their own restricted API key |
| Distribution kit | Partner landing experience and QR poster on a hosted HTTPS site |

### Traveler and mobile experiences

| Desktop | Mobile |
| --- | --- |
| ![Desktop screenshot](screenshot_desktop.png) | ![Mobile screenshot](screenshot_mobile.png) |

## Architecture and important boundaries

```text
Official authority feeds     Venue / operator notices     Community reports
             \                     |                   /
              \___________ incident ingestion __________/
                             |
                Validation, geolocation, expiry,
                    provenance and deduplication
                             |
                    Verified incident store
                             |
                Event map + disruption advisory
                             |
                 Navigation / Google Maps handoff
```

**In this prototype**, the sources and incidents are mock data embedded in `index.html`; there is no backend. The route-changing example runs against an illustrative street-grid graph, **not** the real NYC road network. Local reports do not propagate to other users. The incident desk is not authenticated and is not for public production use.

**Google Maps handoff is not a custom route override.** RallyRoute opens `https://www.google.com/maps/dir/?api=1` with your selected destination and mode. Google Maps independently calculates the actual route; it is **not required** to follow RallyRoute's demo detours or incident assessments. The optional Google Maps JavaScript backdrop merely displays an actual base map with approximate incident overlays. It does **not** mean the prototype has Google Routes API integration or actual closure-aware navigation.

### Optional: Google Maps backdrop

1. Create a Google Cloud project and enable **Maps JavaScript API**.
2. Configure Google Maps Platform billing if required.
3. Create an API key, restrict it to **Maps JavaScript API**, and restrict HTTP referrers to the web origins you control.
4. Serve the app through HTTPS. Choose **Connect Google Maps** in the UI and supply the key when prompted.

The key is used for that browser session, not saved in the app's storage. Never commit an unrestricted key to this repository. See [Google Maps API key guidance](https://developers.google.com/maps/documentation/javascript/get-api-key) and [Maps URLs](https://developers.google.com/maps/documentation/urls/guide).

## Publish a discoverable event experience

The go-to-market concept is **B2B2C distribution**: a venue or organizer directs attendees to the web app from exit signs, digital screens, ticket communications, opted-in SMS, or a QR code.

A simple static-hosting option is GitHub Pages:

1. Push this project to a GitHub repository.
2. In that repository, open **Settings → Pages**, select **Deploy from a branch**, and choose the default branch (`main`) and `/ (root)` folder (where available for the repository/account).
3. After publishing, open the HTTPS Pages URL on a phone.
4. In **Distribution kit**, preview the poster and QR code linking to the published event URL.

Publishing does **not** add live city feeds or safety validation. Keep the demonstration disclaimer visible on any public link. GitHub Pages availability depends on repository visibility and account settings.

## Run regression tests

Requires Python, Playwright and a Chromium browser:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m playwright install chromium
python3 test_regression.py
```

The test script exercises simulated route changes, incident filtering and triage, community-report safeguards, Maps handoff URL generation, QR generation, and mobile layout. It saves fresh desktop/mobile screenshots.

## Project structure

```text
.
├── index.html              # Self-contained single-page experience
├── README.md               # Project guide
├── DEMO_PITCH.md           # Two-minute judge walkthrough
├── QR_LICENSE.md           # Bundled third-party QR code attribution
├── preview.png             # Product preview
├── screenshot_desktop.png  # Desktop capture
├── screenshot_mobile.png   # Mobile capture
├── build_qr.py             # QR encoder build helper
├── test_regression.py      # Automated browser regression checks
├── requirements-dev.txt    # Browser-test dependency
└── .gitignore
```

## Production gaps / roadmap

- Ingest **actual** NYC DOT, NYPD, MTA, transit, venue, and other authorized feeds; maintain source URLs and expiration rules.
- Implement secure ingestion, provenance preservation, operator authentication and moderation.
- Run geospatial routing against *real* road/transit data while enforcing verified restrictions and accessibility constraints.
- Handle uncertainty explicitly: freshness, confidence, coverage gaps, and conflicts between reports.
- Add monitored hosting, privacy/data-retention controls, incident response, and independent safety testing.
- Prove effectiveness through a small venue pilot: advisory engagement, closure-detection lag, false reports, and route-decision usefulness.

This project has **no relationship or official partnership** with Google, the Knicks, Madison Square Garden, NYC DOT, NYPD, or the MTA. No live transportation, police, or emergency data is included.

## Credits and licensing

This prototype bundles a third-party QR encoder licensed under the MIT license; see [`QR_LICENSE.md`](QR_LICENSE.md) for attribution. **No license has been assigned to the original RallyRoute application code**; reuse permissions for that original code are not granted by the QR dependency's license.

For the live presentation script, see [`DEMO_PITCH.md`](DEMO_PITCH.md).