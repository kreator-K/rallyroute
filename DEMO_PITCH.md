# RallyRoute — Hackathon Pitch & Live Demo (2 minutes)

## The problem (0:00–0:20)

"The Knicks win. Millions of people want to celebrate. But someone leaving Madison Square Garden has a surprisingly basic problem: which way can I actually go home? Traditional navigation shows destinations, but chaotic event disruptions can appear faster than that user can interpret them."

## Reframe (0:20–0:35)

"We're not trying to replace Google Maps. We're adding an event intelligence layer *before* navigation, where source credibility and last-minute disruptions can change the decision."

## Live demo (0:35–1:25)

1. Open **Traveler view**. Show the map, mocked official restriction, unverified eyewitness reports, and evidence detail. Emphasize these are fabricated demo items, not actual NYC incidents.
2. Select **Port Authority Bus Terminal**. Show the green schematic path and WATCH indicator.
3. Click **Simulate new road closure**. Explain that a fictional official alert blocks an edge in the illustrative grid. The route path changes and the incident risk elevates to ELEVATED. Do *not* claim the path is real or safe.
4. Show **Open destination in Google Maps**. Explain that Google Maps supplies actual directions but won't automatically enforce our custom detour. The user reviews live conditions before travel.
5. Enter a visitor report, open **Incident desk**, and show that a public report starts **unverified**. Simulate a second observation — it becomes corroborated, **not an officially confirmed closure**.

## Distribution (1:25–1:45)

"The hardest part isn't route-finding, it's discovery. People will not download a new app in the middle of a crowded championship celebration. That's why RallyRoute is a web link venues can put on their own screens, QR signs, ticket emails, and opted-in communications."

Open **Distribution kit** to show the QR poster. On a published HTTPS URL it becomes scannable; from a local file it correctly warns that mobile visitors can't reach it.

## Close (1:45–2:00)

"RallyRoute is not another map. It's a trusted disruption layer distributed through the organizations people already listen to. We turn fragmented signals into clear, source-aware choices — and let familiar navigation take over."

## Judging / technical talking points

- **User:** fans and commuters leaving large events; **buyer/distributor:** venue or city/event partner (B2B2C).
- **Trust principle:** official alerts can establish confirmed closures; community reports cannot on their own.
- **Prototype:** working UI, source statuses, local reporting, schematic rerouting, Google Maps handoff, QR generation on HTTPS.
- **Out of scope:** no live NYC feeds, no real route guarantees, no integrated Google Maps street closure enforcement.
- **Success metrics:** verified-incident freshness, reliable alternative identification, advisory engagement, conversion from venue QR, incident false-positive rate, rerouting outcomes in a validated pilot.

## Practical deployment plan

First pilot: one venue, one event, one set of trusted official disruption feeds, and a published HTTPS domain. Secure an organizer who will place the QR code on their signage and existing attendee communication channels. Evaluate incident accuracy and whether attendees make better travel decisions, before attempting multi-city scale.