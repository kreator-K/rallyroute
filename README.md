# RallyRoute — Macy's 100th Thanksgiving Day Parade

**A personal, event-aware city navigation assistant for New Yorkers.**

RallyRoute is a zero-download prototype built around the challenge: NYC is preparing for Macy's 100th Thanksgiving Day Parade, and New Yorkers need help monitoring disruptions, understanding their own travel plans and preferences, and adapting journeys with minimal effort.

The product direction is an **intent-first journey agent**: a user enters their origin, destination, departure time, preferred transport, crowd/accessibility preferences, and whether in-app auto-adaptation is enabled. RallyRoute then evaluates the parade disruption picture against that trip and updates the journey advisory when a relevant change is detected.

> [!WARNING]
> **Hackathon prototype — not a live navigation, emergency, or safety service.** The official closure schedule below is transcribed from the City's published November 25–26, 2026 notice. It is static, not a live feed. Crowd reports and injected disruption changes are simulated. The prototype does not ingest live NYC DOT, NYPD, MTA, 511NY, or social-media feeds, and does not provide street-level route calculation or background push notifications. Always follow official instructions.

## Open the app

Open [index.html](index.html) locally in a modern browser, or deploy the repository using GitHub Pages. No build step or account is required.

## Try the demo in 2 minutes

1. Open **My journey**.
2. Set an origin, destination, departure time, transport mode, and priority (avoid crowds, fastest practical trip, step-free access, or less walking).
3. Enable or disable **Journey autopilot**, then select **Start monitoring my journey**.
4. Review the personal journey strategy and the scheduled parade restrictions.
5. Select **Simulate a disruption**. With autopilot on, RallyRoute updates the in-app recommendation. With it off, it asks the user to approve the change.
6. Open **City watch** to inspect the official closure schedule and submit an unverified community report.
7. Open **Control room** to inspect the source signals and inject/reset the demo disruption.

The **Use my location** button requests browser geolocation only after the user taps it. Coordinates are placed in the origin field; the browser does not send them to a RallyRoute server.

## Product capabilities

| Capability | Prototype behavior |
| --- | --- |
| Travel intent | Captures origin, destination, departure date/time, mode, priority, walking tolerance, and step-free preference |
| Journey autopilot | User-controlled switch; adapts the in-app advisory automatically on a simulated relevant disruption, or requests approval when off |
| Parade intelligence | Displays 19 scheduled restriction entries from the official NYC CECM notice |
| Map context | Schematic map of the parade corridor and closure areas; optional Google Maps JavaScript base map |
| Community reports | Submissions are labeled unverified and never treated as official closures |
| Google Maps handoff | Opens Google Maps Directions with the user's origin, destination, and transport mode |
| Source transparency | Links to the City notice, NYC DOT traffic advisory, MTA, NYC Emergency Management, and the official event listing |

## 2026 event information used

- **Event:** 100th Macy's Thanksgiving Day Parade.
- **Date:** Thursday, November 26, 2026.
- **Scheduled parade window:** 8:30 AM–12:00 PM.
- **Crowd context:** The City notice says more than 3.5 million spectators are expected along the parade route.
- **Main corridors named by the City:** Central Park West / Central Park South and Sixth Avenue from 59th Street to 34th Street.
- **Important caveat:** The City notice explicitly says street closures are subject to change at NYPD direction.

The app lists the closure streets, boundaries, and time windows from the official City notice. These are **scheduled restrictions**, not a guarantee that every restriction will remain in effect exactly as published.

## Architecture

```text
Traveler intent + preferences
          |
          v
Journey profile (origin, destination, time, mode, accessibility, crowd tolerance)
          |
          v
Event intelligence
  |       |        |
  |       |        +-- Community reports (unverified signals)
  |       +----------- Transit status (external check in this prototype)
  +------------------- Official NYC event / closure notice (static)
          |
          v
Personal impact assessment
          |
          v
Journey autopilot (consent-controlled in-app adaptation)
          |
          v
Updated advisory + Google Maps Directions handoff
```

### What is real vs. simulated

**Grounded in an official source:** The 19 scheduled street-closure entries and their published boundaries/time windows are transcribed from the NYC Office of Citywide Event Coordination and Management notice for November 25–26, 2026. The parade date and 8:30 AM–12:00 PM time are listed by NYC.gov.

**Simulated:** Live crowd density, social-media reports, emerging closures, disruption detection, and the automatic re-evaluation trigger. The route advice is a high-level event-aware recommendation, not a computed route over the live NYC street graph.

**Not implemented:** Live NYC DOT/NYPD/MTA/511NY ingestion, production incident verification, real-time subway/elevator status, background monitoring, push notifications, continuous GPS tracking, or automatic control of the Google Maps app.

### Google Maps integration

- **Base map:** The optional Google Maps JavaScript API connection displays a familiar map and approximate event overlays.
- **Directions handoff:** RallyRoute opens Google Maps Directions with the entered origin, destination, and selected mode.
- **Important limitation:** Google Maps calculates its own route. The handoff does not force Google Maps to obey RallyRoute's custom restrictions or route advice. Do not treat the schematic or advisory as verified turn-by-turn directions.
- To connect a base map, click **Connect Google Maps** and enter a key from a Google Cloud project with Maps JavaScript API enabled and the correct website referrer restrictions. Do not commit API keys to this repository.

## Sources

1. [NYC CECM — Macy's Balloon Inflation & Thanksgiving Day Parade: standard street closures (Nov. 25–26, 2026)](https://www.nyc.gov/assets/cecm/downloads/pdf/thanksgiving-standard-street-closures-2026.pdf)
2. [NYC DOT — Weekly Traffic Advisory, Nov. 21–27, 2026](https://www.nyc.gov/html/dot/html/motorist/weektraf.shtml)
3. [NYC.gov — Macy's Thanksgiving Day Parade event listing](https://www.nyc.gov/main/events?id=270017&permalinkName=macys-thanksgiving-day-parade&sequence=1)
4. [Macy's, Inc. — The 100th Macy's Thanksgiving Day Parade announcement](https://macysinc.com/newsroom/news/news-details/2026/The-100th-Macys-Thanksgiving-Day-Parade-Brings-Holiday-Magic-to-Life-Through-a-Celebration-of-Culture-and-Creativity/default.aspx)
5. [MTA — Official service information](https://new.mta.info/)

## Suggested production roadmap

1. Build secure ingestion connectors for NYC DOT, NYPD / NYC Emergency Management, MTA service alerts and elevator status, 511NY, and approved event/venue feeds.
2. Normalize every disruption with source, timestamp, geospatial scope, confidence, expiry, and a verifiable source URL.
3. Use a real routable street/transit graph and calculate route alternatives against confirmed restrictions and accessibility requirements.
4. Add user-approved background monitoring, notification preferences, trip privacy controls, and secure storage.
5. Keep an explicit consent boundary: automatically refresh recommendations, but require user confirmation for material changes or actions outside the app.
6. Pilot with event attendees and measure disruption detection lag, false-positive rate, reroute usefulness, arrival reliability, and alert fatigue.

RallyRoute is an independent hackathon concept and is not affiliated with Macy's, the City of New York, NYPD, NYC DOT, MTA, or Google.
