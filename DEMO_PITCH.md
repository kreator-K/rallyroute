# RallyRoute — Hackathon Demo & Pitch (2 minutes)

## The hook (0:00–0:20)

"On Thanksgiving morning, New York is preparing for the 100th Macy's Parade. The City expects more than 3.5 million spectators along the route. The problem isn't that people can't find a map. It's that the city changes around their individual plans — streets close, station access changes, and crowd conditions evolve while people are already travelling.

RallyRoute is a personal navigation assistant that watches the disruption picture against your journey, then adapts your plan with minimal effort."

## The product (0:20–0:45)

"Instead of asking everyone to search a citywide closure map, RallyRoute asks for just a few things once: where you're starting, where you're going, when you're leaving, how you prefer to travel, and whether you need step-free access or want to avoid crowds.

Then you choose Journey Autopilot. The goal is to surface only changes that matter to your trip."

## Live walkthrough (0:45–1:35)

1. **Set intent:** Enter origin and destination, departure time, mode, and preferences. Turn Journey Autopilot on.
2. **Show city context:** Open City Watch. Highlight that the app contains the City's published November 25–26 closure schedule, including Central Park West, Sixth Avenue, 34th Street, and nearby blocks.
3. **Show trust:** Explain the difference between a City-published scheduled restriction and an unverified community report. A crowd post is a signal, not an official street closure.
4. **Trigger adaptation:** Click Simulate a disruption. With autopilot enabled, the in-app journey recommendation updates. Turn autopilot off and repeat to show the approval-required experience.
5. **Handoff:** Open the journey in Google Maps with the user's origin, destination, and preferred mode. Explain that Google Maps calculates its own route; RallyRoute's advisory is not injected into Google's route engine.

## Why this is different (1:35–1:50)

"Traditional navigation gives everyone a route. RallyRoute starts with the person: their destination, timing, transport preferences, accessibility needs, and crowd tolerance. It monitors only for disruptions that may affect that person's plan. The experience is proactive rather than another map users must constantly check."

## Close (1:50–2:00)

"RallyRoute is the personal intelligence layer between a changing city and a person's plans. The prototype demonstrates the journey setup, source-aware event context, and consent-controlled adaptation. The next step is connecting live official feeds and a real routing engine."

## Judge Q&A: important boundaries

- **Are the alerts live?** No. The scheduled road restrictions are transcribed from the official NYC CECM notice. Crowd and new-disruption events in the demo are simulated.
- **Does it reroute inside Google Maps?** No. It updates RallyRoute's own recommendation and opens a Google Maps Directions handoff. Google calculates its route independently.
- **Does it run in the background?** No. This is a browser prototype; it does not yet have backend monitoring or push notifications.
- **How do you protect trust?** Keep official restrictions, corroborated observations, and unverified community reports visibly distinct. Only an authorized authority feed should confirm a legal closure.
- **What is the next technical milestone?** Live agency ingestion, provenance and expiry handling, geospatial route calculation, MTA station/elevator status, and consent-based notification delivery.

## Data references

- NYC CECM, Macy's Balloon Inflation & Thanksgiving Day Parade — standard street closures, Nov. 25–26, 2026: https://www.nyc.gov/assets/cecm/downloads/pdf/thanksgiving-standard-street-closures-2026.pdf
- NYC DOT weekly traffic advisory, Nov. 21–27, 2026: https://www.nyc.gov/html/dot/html/motorist/weektraf.shtml
- NYC.gov event listing: https://www.nyc.gov/main/events?id=270017&permalinkName=macys-thanksgiving-day-parade&sequence=1
- Macy's, Inc. 100th Parade announcement: https://macysinc.com/newsroom/news/news-details/2026/The-100th-Macys-Thanksgiving-Day-Parade-Brings-Holiday-Magic-to-Life-Through-a-Celebration-of-Culture-and-Creativity/default.aspx
