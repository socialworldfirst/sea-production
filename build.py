#!/usr/bin/env python3
"""SEA brand channel — production cards v3.
- Video title = primary label (what viewers see on TikTok/YouTube)
- Angle approach = subtitle (Pain-led, Curiosity-led, etc.)
- 3 ratings per angle: social/viral · audience alignment · product/brand · overall
- Full mini-script always visible (no expand)
- Multi-select pick
- Per-card comment box
- Sticky bottom prompt panel
"""
import os, json
from html import escape

VERSION = "v3"

TOPIC_NAMES = {
    "01": "CNY rails + money flow to/from China",
    "02": "FX margin + hidden costs",
    "03": "WorldFirst product mechanics",
    "04": "Personal vs business tools",
    "05": "Paying in CNY economics",
    "06": "Wire rejection failure modes",
    "07": "Switch-point math (KOL)",
}

# Topic 01 — full mini-scripts with video titles + 3 ratings each

def _overall(s, a, p):
    return round((s + a + p) / 3, 1)

SF_TOPIC_01 = [
    {
        "id": "P1-A2", "format": "SF", "pillar": "P1", "topic": "01", "status": "ready",
        "title": "3 ways CNY actually reaches your supplier",
        "format_spec": "Short-form 60s · bilingual",
        "findings": [
            "The 3 ways: SWIFT-routed via correspondent banks; CIPS direct clearing; MYbank/Alipay corporate (for 1688).",
            "CIPS processed $24.47T USD-equivalent in 2024 (+42.6% YoY) — real-scale infrastructure.",
            "Most operators treat the three as one mechanism. Differences are speed, cost, supplier-side amount.",
            "WF SG public page doesn't name MYbank — use 'dedicated CNY rail' framing.",
        ],
        "angles": [
            {"video_title": "The 3 paths your CNY takes to China (most operators only know one)",
             "approach": "Curiosity-led",
             "rating_social": 4.5, "rating_audience": 4.5, "rating_product": 4.0,
             "hook": "Your CNY can take three different paths to reach a Chinese supplier. Only one is same-day.",
             "body": "Path one: SWIFT through correspondent banks — 3 to 5 days. Path two: CIPS, China's own clearing system — 1 to 2 days. Path three: MYbank routing for 1688 — same-day when set up right. Most banks don't tell you which one you're on.",
             "close": "Check your wire confirmation. The routing's on it.",
             "visual": "Animated 3-rail diagram, money moving on each at different speeds"},
            {"video_title": "I sent CNY. My supplier got USD. This is why.",
             "approach": "Pain-led",
             "rating_social": 4.8, "rating_audience": 4.7, "rating_product": 4.3,
             "hook": "You sent CNY. Your supplier received USD. The bank converted at their rate.",
             "body": "This happens because not every bank labelled 'CNY transfer' uses a CNY-direct rail. Some route through SWIFT to a USD-clearing correspondent. Conversion happens mid-flight. Your supplier gets USD. Same wire, different bank, different outcome.",
             "close": "Check the routing before you send.",
             "visual": "Split screen — sent CNY (clean) vs received USD (red highlight)"},
            {"video_title": "$10K to China through 3 different rails (live test)",
             "approach": "Demo-led",
             "rating_social": 4.2, "rating_audience": 4.3, "rating_product": 4.5,
             "hook": "Watch what happens to your CNY at each of three different rails.",
             "body": "Same $10K, three rails. Rail one — SWIFT with intermediary fees: supplier gets $9,800 USD. Rail two — CIPS direct: supplier gets 70,000 CNY clean. Rail three — MYbank for 1688: supplier gets 70,000 CNY same-day. The rail decides the receipt.",
             "close": "Three rails. Three receipts. Pick the right one.",
             "visual": "Three-panel demo on screen, money flow on each"},
            {"video_title": "Two banks said 'CNY transfer'. Only one moved CNY.",
             "approach": "Comparison-led",
             "rating_social": 4.0, "rating_audience": 4.2, "rating_product": 4.2,
             "hook": "Two banks both say 'CNY transfer'. Watch what each actually does.",
             "body": "Bank A: sends through SWIFT, your CNY routes via USD-clearing correspondent, supplier gets converted USD. Bank B: sends through CIPS direct, CNY stays CNY, supplier receives the exact amount you sent. Same label, different infrastructure.",
             "close": "Same words, different outcomes. Read the rail.",
             "visual": "Side-by-side bank screen recordings + supplier-side receipts"},
            {"video_title": "What is CIPS? China's $24T payment system explained",
             "approach": "Authority-led",
             "rating_social": 3.8, "rating_audience": 4.0, "rating_product": 3.5,
             "hook": "CIPS processed $24 trillion in 2024. Most operators don't know what CIPS is.",
             "body": "CIPS is China's own cross-border clearing system. Unlike SWIFT which just sends messages, CIPS actually moves the CNY. 1,600 banks across 180 countries connect to it. When your CNY rides CIPS, it stays CNY all the way to your supplier.",
             "close": "Learn what your money actually does.",
             "visual": "Data viz of CIPS volume bars year-over-year"},
        ],
    },
    {
        "id": "P1-A7", "format": "SF", "pillar": "P1", "topic": "01", "status": "ready",
        "title": "Two banks offer 'CNY transfer'. Only one moves CNY.",
        "format_spec": "Short-form 45s · bilingual",
        "findings": [
            "Bank A: routes via SWIFT to USD-clearing correspondent; supplier receives USD.",
            "Bank B: routes via CIPS or MYbank direct; supplier receives true CNY.",
            "Same label ('CNY transfer'), different infrastructure, different outcomes.",
            "Marketing claims don't match operational reality.",
        ],
        "angles": [
            {"video_title": "Sent CNY. Got USD. Same wire, two banks.",
             "approach": "Pain-first",
             "rating_social": 4.7, "rating_audience": 4.6, "rating_product": 4.5,
             "hook": "You sent CNY. Your supplier got USD. Both banks called it 'CNY transfer'.",
             "body": "One bank routed your money through SWIFT to a USD-clearing correspondent. Conversion happened mid-flight. The other bank would have routed via CIPS direct, keeping CNY all the way through. Same label. Different rail. Different supplier-side amount.",
             "close": "Read the rail, not the label.",
             "visual": "Two wire confirmations side by side; supplier opens both, sees different currencies"},
            {"video_title": "Same $50K, two banks. Watch what your supplier sees.",
             "approach": "Comparison split-screen",
             "rating_social": 4.5, "rating_audience": 4.5, "rating_product": 4.5,
             "hook": "Same wire, two banks, two outcomes. Which one moved real CNY.",
             "body": "Bank A — SWIFT routing, USD-clearing intermediary, supplier receives $48,800 USD. Bank B — CIPS direct, supplier receives 350,000 CNY. Same wire instruction, two different infrastructures, two different receipts.",
             "close": "Same labels mean different things. Confirm the rail.",
             "visual": "Animated split screen following both wires from send to supplier"},
            {"video_title": "There are 2 definitions of 'CNY transfer'. Most operators don't know.",
             "approach": "Curiosity-led",
             "rating_social": 4.3, "rating_audience": 4.3, "rating_product": 4.2,
             "hook": "There are two definitions of 'CNY transfer' in banking. Only one means CNY actually moves CNY.",
             "body": "Definition one: send CNY label, route via SWIFT, conversion happens at correspondent. Definition two: send CNY label, route via CIPS direct, no conversion. Your bank picks the definition for you. The label doesn't change. The outcome does.",
             "close": "Check which definition your bank uses.",
             "visual": "Two dictionary-style definitions overlaid on bank logos"},
            {"video_title": "What your supplier's bank actually sees on a 'CNY' wire",
             "approach": "Authority-led",
             "rating_social": 3.8, "rating_audience": 4.0, "rating_product": 4.0,
             "hook": "What a supplier's bank actually sees when you send 'CNY'.",
             "body": "On the supplier side, an incoming SWIFT message may show CNY or may show USD with a CNY conversion request. CIPS-routed transfers always arrive as CNY. SWIFT-routed CNY may arrive as USD if the correspondent doesn't hold CNY. Banker-side view explains the gap.",
             "close": "Insider literacy on cross-border CNY.",
             "visual": "Mock bank-side admin screen showing incoming message details"},
            {"video_title": "Live: $20K wire, two banks, supplier-side notifications",
             "approach": "Demo-led",
             "rating_social": 4.2, "rating_audience": 3.8, "rating_product": 4.0,
             "hook": "Live: same wire, two banks. Watch the difference at the supplier end.",
             "body": "I'm sending $20K-equivalent CNY via Bank A and Bank B simultaneously. Same supplier, same amount, same currency instruction. In two minutes, two notifications hit the supplier's phone. One says CNY 140,000. One says USD 19,400.",
             "close": "The rail decided this, not the label.",
             "visual": "Live screen recording on two banking apps + supplier WeChat notifications"},
        ],
    },
    {
        "id": "P1-A8", "format": "SF", "pillar": "P1", "topic": "01", "status": "ready",
        "title": "The 3-letter code that decides if your wire is same-day",
        "format_spec": "Short-form 45s · bilingual",
        "findings": [
            "Field 71A of SWIFT MT103 holds the OUR/SHA/BEN code.",
            "OUR = sender pays all → supplier gets full amount.",
            "SHA = shared → intermediaries deduct from amount (default at most banks).",
            "BEN = beneficiary pays → unpredictable arrival amount.",
            "Each intermediary bank charges $15-50. Multiple intermediaries possible.",
        ],
        "angles": [
            {"video_title": "The 3-letter code on every China wire (most operators never see it)",
             "approach": "Curiosity-led",
             "rating_social": 4.4, "rating_audience": 4.4, "rating_product": 4.2,
             "hook": "There's a 3-letter code on every China wire. Your bank picks it for you.",
             "body": "Field 71A of SWIFT MT103. Three options. OUR — sender pays all intermediary fees, supplier gets full amount. SHA — shared, intermediaries deduct from amount, supplier gets less. BEN — beneficiary pays, supplier covers everything. Your bank's default is usually SHA.",
             "close": "Change the code, change the outcome.",
             "visual": "Zoom into a real SWIFT MT103 message, highlight field 71A"},
            {"video_title": "My supplier got $200 less. A code I didn't choose did this.",
             "approach": "Pain-led",
             "rating_social": 4.6, "rating_audience": 4.5, "rating_product": 4.5,
             "hook": "Your supplier got $200 less. The reason is a code you didn't choose.",
             "body": "You sent $10,000. They got $9,800. The bank set Field 71A to SHA — shared fees. Two intermediary banks took $100 each in transit. If you'd set it to OUR, you'd have paid those fees upfront and your supplier would have received the full amount.",
             "close": "Ask your bank to set OUR on next China wire.",
             "visual": "Wire confirmation zoom showing SHA, then supplier receipt showing shortfall"},
            {"video_title": "How to switch your China wires from SHA to OUR (60s)",
             "approach": "Tutorial-led",
             "rating_social": 4.0, "rating_audience": 4.0, "rating_product": 4.5,
             "hook": "How to switch from SHA to OUR — supplier receives full amount.",
             "body": "When initiating a wire, look for 'Details of Charges' or 'Fee instruction'. Most banking apps default to SHA. Change it to OUR. The cost of intermediary fees ($30-100 typically) is added upfront to your wire amount. Your supplier receives exactly what you intended.",
             "close": "One field on the form. Big difference at the other end.",
             "visual": "Screen recording of online banking, highlighting the fee field"},
            {"video_title": "$50K wire, 3 codes, 3 different supplier-side amounts",
             "approach": "Comparison-led",
             "rating_social": 4.2, "rating_audience": 4.2, "rating_product": 4.2,
             "hook": "OUR vs SHA vs BEN on a real $50K wire to Shenzhen.",
             "body": "Same $50K, same supplier, three different fee instructions. OUR: supplier receives full $50,000; sender paid $80 extra in fees upfront. SHA: supplier receives $49,800; intermediaries took $200 in transit. BEN: supplier receives $49,650; all fees stripped from amount.",
             "close": "Pick the code that matches what you want.",
             "visual": "Three receipts side by side with code labels"},
            {"video_title": "Field 71A: the SWIFT field that decides your fee",
             "approach": "Authority-led",
             "rating_social": 3.6, "rating_audience": 4.0, "rating_product": 4.0,
             "hook": "Field 71A of SWIFT MT103. Read this field, you know what happens.",
             "body": "SWIFT MT103 is the standard message format for international wires. Field 71A — Details of Charges — controls fee allocation. The values are OUR, SHA, BEN. This isn't insider trivia. It's the literal mechanism that decides what your supplier sees. Banks rarely surface it.",
             "close": "Banker literacy. Your wires deserve it.",
             "visual": "Annotated MT103 diagram with arrows pointing to 71A"},
        ],
    },
    {
        "id": "P1-A9", "format": "SF", "pillar": "P1", "topic": "01", "status": "ready",
        "title": "Supplier said wire didn't arrive. Bank says it did.",
        "format_spec": "Short-form 60s · bilingual",
        "findings": [
            "Wires can sit between intermediary correspondents for hours to days.",
            "Currency conversion windows add up to 2 working days.",
            "Local bank holidays in CN or SEA cause silent delays.",
            "AML/fraud thresholds can hold wires above certain amounts without sender notification.",
        ],
        "angles": [
            {"video_title": "My bank says sent. My supplier says nothing. Both right.",
             "approach": "Pain-first",
             "rating_social": 4.7, "rating_audience": 4.7, "rating_product": 4.5,
             "hook": "Your bank says sent. Your supplier says nothing. Both are right.",
             "body": "When a bank says 'sent,' it means the wire left their system. When a supplier says 'nothing,' it means nothing has arrived in their account. The space between is where intermediary banks sit. Hours. Sometimes days. Especially with conversion or AML holds in the chain.",
             "close": "Track the wire by SWIFT reference, not by 'sent.'",
             "visual": "Split screen: bank app showing 'sent', supplier WhatsApp saying 'nothing'"},
            {"video_title": "3 places your China wire can sit before it arrives",
             "approach": "Mechanism-led",
             "rating_social": 4.2, "rating_audience": 4.4, "rating_product": 4.5,
             "hook": "Three places your wire can sit between 'sent' and 'received'.",
             "body": "Place one: sending bank's outbound queue, especially after-hours. Place two: intermediary correspondent — conversion or AML hold. Place three: receiving bank's inbound clearance, especially during local holidays. Each adds 1-3 business days. Bank confirms 'sent'; reality is 'in transit at place X.'",
             "close": "Know the three places. Track them.",
             "visual": "Map-style flow diagram with three waypoints highlighted"},
            {"video_title": "How to track a missing wire to China (step by step)",
             "approach": "Tutorial-led",
             "rating_social": 4.0, "rating_audience": 4.2, "rating_product": 4.4,
             "hook": "How to track a missing wire to China step by step.",
             "body": "Step one: get the SWIFT reference number from your bank. Step two: ask for an MT199 status request — banks can query intermediaries. Step three: check correspondent bank list, see which one has the holdup. Step four: ask receiving bank to confirm arrival.",
             "close": "Don't wait for the bank to chase. Drive it.",
             "visual": "Phone screen overlay showing each tracking step"},
            {"video_title": "I sent $42K Friday. Supplier got nothing Monday. Here's what I found.",
             "approach": "Story-led",
             "rating_social": 4.7, "rating_audience": 4.5, "rating_product": 4.5,
             "hook": "I sent $42K Friday. Supplier got nothing by Monday. Here's what I found.",
             "body": "Friday 3pm Sydney time: I hit send. Bank confirmed sent at 3:02pm. Monday 9am Shenzhen: supplier said nothing arrived. I called my bank — they showed sent. I asked for the correspondent chain. The wire was sitting at an intermediary in Singapore on AML hold over the weekend. Released Tuesday. Supplier received Wednesday.",
             "close": "Wires don't follow your calendar.",
             "visual": "Timeline animation: Friday → Monday → Tuesday → Wednesday"},
            {"video_title": "What 'sent' actually means on a SWIFT wire",
             "approach": "Authority-led",
             "rating_social": 3.5, "rating_audience": 3.9, "rating_product": 4.0,
             "hook": "What 'sent' actually means on a SWIFT wire. It doesn't mean 'received.'",
             "body": "In SWIFT messaging, 'sent' triggers when the originating bank releases the MT103 to the correspondent network. That's a system event. Receipt is a separate event — when the beneficiary bank credits the supplier's account. The two can be hours or days apart. Banks track separately.",
             "close": "Sent is not received. Two different events.",
             "visual": "Clean diagram showing 'sent event' vs 'received event' with timeline gap"},
        ],
    },
    {
        "id": "P1-A10", "format": "SF", "pillar": "P1", "topic": "01", "status": "ready",
        "title": "The routing decision that quietly changes your fee 1%",
        "format_spec": "Short-form 45s · bilingual",
        "findings": [
            "Banks choose correspondent routing path per wire, silently.",
            "Wrong correspondent = extra intermediary = extra fee.",
            "1% on $100K = $1,000 silently extracted.",
            "Each intermediary in chain charges $15-50; multiple intermediaries compound.",
        ],
        "angles": [
            {"video_title": "The 1% routing decision your bank makes silently on every China wire",
             "approach": "Curiosity-led",
             "rating_social": 4.5, "rating_audience": 4.5, "rating_product": 4.5,
             "hook": "Your bank makes one silent decision on every China wire. It changes your fee 1%.",
             "body": "When you initiate a wire, your bank picks the correspondent path. Sometimes one intermediary. Sometimes three. Each intermediary takes $15-50. On a $100K wire, the difference between one and three intermediaries is roughly $100. Add FX correspondent spread, and you're at 1%.",
             "close": "Ask your bank for the correspondent chain.",
             "visual": "Wire flow diagram, highlight the routing fork"},
            {"video_title": "Where did $1,000 go on my $100K China wire?",
             "approach": "Pain-led",
             "rating_social": 4.6, "rating_audience": 4.6, "rating_product": 4.7,
             "hook": "Where did $1,000 go on your $100K wire? The routing fork you never saw.",
             "body": "Your $100K wire passed through three intermediary correspondents. Each took fees: $25, $35, $40 = $100 in flat fees. Plus the correspondent FX spread on the conversion leg added 0.9% — another $900. Total: $1,000 silently extracted. None of it on the wire confirmation.",
             "close": "Demand a correspondent chain before you send.",
             "visual": "$100K wire with three deduction stops, each labelled"},
            {"video_title": "Your bank knows the correspondent chain. They won't show you.",
             "approach": "Authority-led",
             "rating_social": 3.8, "rating_audience": 4.0, "rating_product": 4.2,
             "hook": "The correspondent banks your money passes through. Most banks won't show you.",
             "body": "Every SWIFT wire generates an audit trail of intermediary correspondents. Your bank has it. Compliance teams use it. But customer-facing banking apps don't surface it. Operators are flying blind on cost. Specialised cross-border rails publish the routing chain upfront.",
             "close": "Banker information asymmetry. Close it.",
             "visual": "Mock compliance dashboard vs customer app showing the gap"},
            {"video_title": "Watch a $100K wire route through 3 banks (live deductions)",
             "approach": "Mechanism-led",
             "rating_social": 4.1, "rating_audience": 4.1, "rating_product": 4.2,
             "hook": "Watch a wire route across correspondents and see fee deductions live.",
             "body": "Sending bank → correspondent 1 ($25 fee) → correspondent 2 ($35) → correspondent 3 ($40) → receiving bank. Plus FX spread of 0.9% on the conversion correspondent. Total deductions: $1,000. Animated flow shows where each fee taken.",
             "close": "Visualise the route. Demand the same from your bank.",
             "visual": "Animated map-style routing with fee popups"},
            {"video_title": "Same $100K wire, 2 routing paths. $950 difference.",
             "approach": "Comparison-led",
             "rating_social": 4.2, "rating_audience": 4.2, "rating_product": 4.5,
             "hook": "Same wire, two routing paths, $1,000 difference at the end.",
             "body": "Path one: 3 intermediaries, multiple correspondent spreads, supplier receives $99,000. Path two: 1 direct correspondent, single spread, supplier receives $99,950. Same wire instruction. Different chain. $950 lost or kept depending on routing.",
             "close": "Cross-border rail vs SWIFT chain. The difference is in the chain.",
             "visual": "Two routing paths side by side, end totals highlighted"},
        ],
    },
    {
        "id": "P1-A11", "format": "SF", "pillar": "P1", "topic": "01", "status": "ready",
        "title": "Why your CNY payment sometimes arrives in USD",
        "format_spec": "Short-form 60s · bilingual",
        "findings": [
            "Conversion can happen at sender side, correspondent, or beneficiary bank.",
            "If no CNY-direct correspondent in chain, USD conversion happens by default.",
            "Supplier ends up holding USD when expecting CNY.",
            "Supplier then converts USD → CNY at their bank → double conversion cost.",
        ],
        "angles": [
            {"video_title": "I sent CNY. My supplier got USD. Here's why.",
             "approach": "Pain-first",
             "rating_social": 4.7, "rating_audience": 4.7, "rating_product": 4.6,
             "hook": "You sent CNY. Your supplier received USD. Their bank converted at their rate.",
             "body": "When a wire labelled CNY routes through a correspondent that only holds USD, conversion happens mid-flight at the correspondent's rate. The supplier receives USD. Their local bank converts USD back to CNY at another rate. Two conversions. Two costs. Your supplier ate both. Now they're quoting you higher next time.",
             "close": "Avoid the double conversion. Use a CNY-direct rail.",
             "visual": "Wire confirmation says CNY; supplier receipt says USD; supplier statement shows USD→CNY conversion"},
            {"video_title": "3 places where your CNY can become USD",
             "approach": "Mechanism-led",
             "rating_social": 4.3, "rating_audience": 4.5, "rating_product": 4.4,
             "hook": "Three places where your CNY can become USD between you and your supplier.",
             "body": "Point one: sender's bank converts to USD before sending (cheaper for them). Point two: intermediary correspondent converts because they only hold USD. Point three: receiving bank converts because they can't accept CNY directly. Each conversion point adds a spread.",
             "close": "Map the conversion points. Eliminate them.",
             "visual": "Pipeline diagram with three conversion stops highlighted"},
            {"video_title": "When 'CNY transfer' becomes 'USD transfer' mid-flight",
             "approach": "Curiosity-led",
             "rating_social": 4.3, "rating_audience": 4.3, "rating_product": 4.2,
             "hook": "When 'CNY transfer' becomes 'USD transfer' mid-flight: the routing trap.",
             "body": "Your wire leaves marked CNY. Halfway through the correspondent chain, it hits a bank that doesn't hold CNY. The bank converts to USD to keep the wire moving. The receiving end gets USD, even though the original instruction was CNY. Routing transparency exists; it's just not customer-facing.",
             "close": "Routing transparency. Demand it.",
             "visual": "Wire travelling, CNY label visible, then morphs into USD label at correspondent"},
            {"video_title": "The double conversion no one talks about (and who pays for it)",
             "approach": "Cost-led",
             "rating_social": 4.6, "rating_audience": 4.6, "rating_product": 4.7,
             "hook": "Double conversion: who pays? Spoiler: your supplier, then you on the next order.",
             "body": "Round one: your CNY converts to USD mid-flight (correspondent spread, ~0.3%). Round two: supplier converts USD back to CNY at their bank (~0.5%). Supplier ate 0.8% total. They factor it into the next price. You pay it on the second invoice. Then the next. Compounding.",
             "close": "Stop the loop. CNY-direct rail.",
             "visual": "Cost accumulation animation across rounds"},
            {"video_title": "Why CIPS exists (and why most operators don't know about it)",
             "approach": "Authority-led",
             "rating_social": 3.7, "rating_audience": 4.0, "rating_product": 3.5,
             "hook": "Why CIPS exists — to keep CNY as CNY end-to-end.",
             "body": "CIPS was launched by the People's Bank of China in 2015 specifically because SWIFT-routed CNY kept getting converted mid-flight. CIPS is purpose-built to clear CNY end-to-end, no intermediate conversion. 80% of cross-border RMB clearance now goes through CIPS.",
             "close": "CIPS-routed CNY. The infrastructure exists.",
             "visual": "PBOC building / CIPS logo with explanation text overlay"},
        ],
    },
]

LF_P1_A1 = {
    "id": "P1-A1", "format": "LF", "pillar": "P1", "topic": "01", "status": "ready",
    "title": "Money in and out of China: the operator's full picture",
    "format_spec": "Long-form 15-20 min · bilingual EN + Mandarin · Hui Mei lead · 6-8 SF micro-cuts pulled from this shoot",
    "findings": [
        "CIPS processed ¥175.49 trillion in 2024 (+42.6% YoY). The CNY rail is now real-scale infrastructure.",
        "80% of CIPS transactions still use SWIFT for messaging — mixed-rail reality.",
        "ASEAN remittance used to cost >6% in fees; PromptPay-PayNow now seconds at fraction of cost.",
        "Bidirectional flow (in + out) is rarely covered as one piece — SEO + audience gap.",
        "WF SG public page doesn't name MYbank — use 'dedicated CNY rail' framing.",
    ],
    "angles": [
        {"video_title": "Money in and out of China: the complete operator's guide",
         "approach": "Sequential — in then out",
         "rating_social": 3.8, "rating_audience": 4.2, "rating_product": 4.2,
         "hook": "Most operators know one direction of money with China. The full picture has two.",
         "body": "Act 1 (0:00-1:00) Frame the bidirectional picture. Act 2 (1:00-9:00) Inbound: paying suppliers — rails, mechanics, failure modes. Act 3 (9:00-15:00) Outbound: marketplace payouts, repatriation, holding multi-currency. Act 4 (15:00-17:00) Synthesis — operator decisions across both directions.",
         "close": "Master both directions, you're operating. Master one, you're partial.",
         "visual": "Animated bidirectional money flow map · SEA → CN → SEA"},
        {"video_title": "3 things go wrong with cross-border China payments (and how to fix them)",
         "approach": "Problem-led",
         "rating_social": 4.7, "rating_audience": 4.7, "rating_product": 4.6,
         "hook": "Three things go wrong with operator money flow to China.",
         "body": "Act 1 Hook + frame. Act 2 Break 1 — wire rejections (beneficiary mismatch, fraud rules). Act 3 Break 2 — FX gaps (visible + invisible). Act 4 Break 3 — routing delays (SWIFT vs alternative rails). Act 5 Cross-cutting fix — what specialised rails change.",
         "close": "Real operator wins from operators who fixed all three.",
         "visual": "Three operator scenarios, each broken then fixed"},
        {"video_title": "24 hours of money to and from China (one operator's reality)",
         "approach": "Day-in-the-life",
         "rating_social": 4.5, "rating_audience": 4.5, "rating_product": 4.0,
         "hook": "One operator's 24 hours of money to and from China.",
         "body": "9am marketplace payout from Amazon AU lands. 10am supplier wire to Shenzhen. 11am FX exposure check. 2pm bulk transfer to 5 suppliers. 4pm receivables check, end-of-day reconciliation. Each timestamp = one money-flow moment.",
         "close": "This is the actual rhythm of operator money. Leverage points throughout.",
         "visual": "Documentary cuts — real operator desk, screens, phones across the day"},
        {"video_title": "Where $5,000 leaks every month from a $100K China cycle",
         "approach": "Cost-decomposition",
         "rating_social": 4.4, "rating_audience": 4.5, "rating_product": 4.5,
         "hook": "On a $100K monthly import + payout cycle, here's where money actually leaks.",
         "body": "Leak 1 — FX margin on inbound supplier payments ($1,800/month). Leak 2 — wire + intermediary bank fees ($150-400/month). Leak 3 — marketplace payout currency conversion losses ($1,500/month). Total: ~$3,500-5,000/month silently extracted. Fix: routing through specialist rail.",
         "close": "Annualised: a hire / a holiday / next year's working capital.",
         "visual": "On-screen calculator + leak diagram animation"},
        {"video_title": "5 questions every China-sourcing operator asks (answered)",
         "approach": "Question-led",
         "rating_social": 4.0, "rating_audience": 4.3, "rating_product": 4.0,
         "hook": "Five questions every operator asks about money + China. Here are the answers.",
         "body": "Q1 How to pay a Chinese supplier? Q2 Why does my supplier sometimes ask for more? Q3 How fast can the payment land? Q4 How do I get paid back from marketplaces in CNY-friendly ways? Q5 When should I switch off my local bank?",
         "close": "If you're asking these, you're already operator-grade.",
         "visual": "Five Q&A title cards with answers cut between"},
    ],
}


def pending(id_, pillar, topic, title, format_spec, fmt="SF"):
    return {"id": id_, "format": fmt, "pillar": pillar, "topic": topic, "status": "pending",
            "title": title, "format_spec": format_spec, "findings": [], "angles": []}

PENDING_CARDS = [
    pending("P1-A12", "P1", "02", "$1,200 gone from a $50K supplier wire. Where.", "Short-form 45s · bilingual"),
    pending("P1-A13", "P1", "02", "Bank says no fee. You still paid $300.", "Short-form 30s · bilingual"),
    pending("P1-A14", "P1", "02", "Three operators, same $50K wire, three different supplier-end amounts", "Short-form 60s"),
    pending("P1-A15", "P1", "02", "What 'no fee' costs you per $10K to China", "Short-form 60s · bilingual"),
    pending("P1-A16", "P1", "02", "Receipt says $50K. Statement says $51.2K.", "Short-form 60s"),
    pending("P2-A1", "P2", "02", "How a 2% bank-to-rail gap compounds over a year", "Short-form 60s"),
    pending("P2-A7", "P2", "02", "Your sourcing budget shrinks 4% a year (silent compound)", "Short-form 60s"),
    pending("P2-A8", "P2", "02", "How to read FX margin off your wire confirmation", "Short-form 60s tutorial"),
    pending("P2-A9", "P2", "02", "Good rate quoted vs real interbank rate", "Short-form 45s"),
    pending("P3-A2", "P3", "03", "World Account setup, end-to-end in 8 minutes", "Long-form 8-10 min tutorial · Hui Mei lead", fmt="LF"),
    pending("P3-A10", "P3", "03", "Why SMEs are building a financial stack", "Short-form 60s"),
    pending("P2-A3", "P2", "03", "Bank wire vs WorldFirst on the same $50K payment", "Short-form 60s comparison"),
    pending("P2-A12", "P2", "04", "Personal cross-border tools weren't built for business", "Short-form 60s"),
    pending("P2-A13", "P2", "04", "How much PayPal actually costs you on a $20K supplier payment", "Short-form 60s"),
    pending("P2-A14", "P2", "04", "Credit cards for international supplier payments: the gap", "Short-form 60s"),
    pending("P2-A18", "P2", "04", "Personal vs business FX rate: the spread", "Short-form 60s"),
    pending("P2-A24", "P2", "04", "When CAN you pay a Chinese supplier by card?", "Short-form 60s"),
    pending("P1-A6", "P1", "05", "Why paying your supplier in CNY actually wins", "Short-form 60s · bilingual"),
    pending("P1-A4", "P1", "06", "Your supplier asked you to pay the $200 they didn't receive", "Short-form 60s · bilingual"),
    pending("P1-A5", "P1", "06", "SWIFT vs the alternatives: which actually pays your supplier faster", "Short-form 60s · bilingual"),
    pending("P2-A6", "P2", "07", "The break-even: when should you switch providers?", "KOL distributed · math/decision-led", fmt="KOL"),
]

CARDS = [LF_P1_A1] + SF_TOPIC_01 + PENDING_CARDS


def render_rating_bar(label, value, color_class):
    pct = (value / 5.0) * 100
    return f'''
<div class="rating-bar {color_class}">
  <span class="rating-label">{label}</span>
  <div class="rating-track"><div class="rating-fill" style="width: {pct}%"></div></div>
  <span class="rating-value">{value}</span>
</div>'''


def render_angle(card_id, idx, a, is_lf=False):
    angle_id = f"{card_id}-a{idx+1}"
    overall = _overall(a['rating_social'], a['rating_audience'], a['rating_product'])
    if is_lf:
        body_label = "Structure"
    else:
        body_label = "Body (5-50s)"
    visual_block = ""
    if a.get('visual'):
        visual_block = f'''<div class="mini-row"><span class="mini-label">Visual</span><span class="mini-text">{escape(a.get('visual',''))}</span></div>'''
    return f'''
<div class="angle" data-angle-id="{angle_id}">
  <label class="angle-check">
    <input type="checkbox" class="angle-pick" data-card="{card_id}" data-idx="{idx+1}" data-title="{escape(a['video_title'])}">
    <span class="checkmark"></span>
  </label>
  <div class="angle-content">
    <h4 class="video-title">{escape(a['video_title'])}</h4>
    <div class="approach">{escape(a['approach'])}</div>

    <div class="ratings">
      {render_rating_bar('Social', a['rating_social'], 'rating-social')}
      {render_rating_bar('Audience', a['rating_audience'], 'rating-audience')}
      {render_rating_bar('Product', a['rating_product'], 'rating-product')}
      <div class="rating-overall">Overall <strong>{overall}</strong></div>
    </div>

    <div class="mini-script">
      <div class="mini-row"><span class="mini-label">Hook</span><span class="mini-text">{escape(a.get('hook',''))}</span></div>
      <div class="mini-row"><span class="mini-label">{body_label}</span><span class="mini-text">{escape(a.get('body',''))}</span></div>
      <div class="mini-row"><span class="mini-label">Close</span><span class="mini-text">{escape(a.get('close',''))}</span></div>
      {visual_block}
    </div>
  </div>
</div>
'''


def render_card(c):
    fmt_class = f"fmt-{c['format'].lower()}"
    is_lf = c['format'] == 'LF'
    is_pending = c['status'] == 'pending'

    if is_pending:
        body = f'''
        <div class="card-section">
          <div class="pending-msg">
            <strong>Awaiting research</strong>
            <p>Writing angles will appear after Topic {c['topic']} research run completes ({escape(TOPIC_NAMES.get(c['topic'], ''))}).</p>
          </div>
        </div>'''
    else:
        angles_html = "\n".join(render_angle(c['id'], i, a, is_lf=is_lf) for i, a in enumerate(c.get('angles', [])))
        findings_list = "\n".join(f'<li>{escape(f)}</li>' for f in c.get('findings', []))
        body = f'''
        <div class="card-section">
          <div class="section-head">
            <h4 class="section-h">Writing angles ({len(c.get('angles', []))}) · pick one or more</h4>
          </div>
          {angles_html}
        </div>
        <div class="card-section comment-block">
          <h4 class="section-h">Your comment on this card</h4>
          <textarea class="card-comment" data-card="{c['id']}" placeholder="Notes / red flags / direction. Minor notes → I auto-route to script drafting for the picked angles. Major rework → I'll produce v3 cards."></textarea>
        </div>
        <details class="findings-details">
          <summary class="findings-summary">Research findings ({len(c.get('findings', []))}) · click to expand</summary>
          <ul class="findings">{findings_list}</ul>
        </details>'''

    return f'''
<article class="card status-{c['status']}" id="{c['id']}" data-format="{c['format'].lower()}" data-status="{c['status']}" data-topic="{c['topic']}">
  <header class="card-head">
    <div class="card-meta">
      <span class="card-id">{escape(c['id'])}</span>
      <span class="card-fmt {fmt_class}">{escape(c['format'])}</span>
      <span class="card-pillar">{escape(c['pillar'])}</span>
      <span class="card-topic">Topic {c['topic']}</span>
      <span class="card-status">{c['status'].upper()}</span>
    </div>
    <h3 class="card-title">{escape(c['title'])}</h3>
    <div class="card-format-spec">{escape(c['format_spec'])}</div>
  </header>
  {body}
</article>'''


TOPIC_STATUS = {"01": "done", "02": "pending", "03": "pending", "04": "pending", "05": "pending", "06": "pending", "07": "pending"}


def render_topic_strip():
    counts = {}
    for c in CARDS:
        counts[c['topic']] = counts.get(c['topic'], 0) + 1
    out = []
    for tnum, name in TOPIC_NAMES.items():
        status = TOPIC_STATUS[tnum]
        out.append(f'''
<div class="topic-strip-card">
  <div class="topic-strip-num">TOPIC {tnum}</div>
  <div class="topic-strip-name">{escape(name)}</div>
  <div class="topic-strip-status {status}">{status.upper()}</div>
  <div class="topic-strip-count">{counts.get(tnum, 0)} cards</div>
</div>''')
    return "\n".join(out)


CSS = r"""
*, *::before, *::after { box-sizing: border-box; }
:root {
  --fg: #111;
  --fg-muted: #5b5b5b;
  --fg-soft: #888;
  --bg: #fafafa;
  --bg-paper: #fff;
  --hairline: rgba(0,0,0,0.09);
  --hairline-soft: rgba(0,0,0,0.05);
  --dot: #0a6d2f;
  --pending: rgba(0,0,0,0.06);
  --pick: #0a6d2f;
  --social: #1a6dcc;
  --audience: #946100;
  --product: #b03060;
  --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
}
html, body { margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif; background: var(--bg); color: var(--fg); -webkit-font-smoothing: antialiased; line-height: 1.6; font-size: 16px; }
a { color: var(--fg); }

.layout { max-width: 1200px; margin: 0 auto; padding: 32px 24px 130px; }

.hero { padding-bottom: 28px; border-bottom: 1px solid var(--hairline); margin-bottom: 32px; }
.eyebrow { font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--fg-soft); margin-bottom: 14px; }
.hero h1 { font-size: 32px; line-height: 1.15; font-weight: 600; letter-spacing: -0.02em; margin: 0 0 14px; }
.lede { font-size: 16px; line-height: 1.55; color: var(--fg-muted); max-width: 720px; margin: 0 0 18px; }
.meta { display: flex; flex-wrap: wrap; gap: 14px 28px; font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fg-soft); }

.topic-strip { margin-bottom: 28px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
.topic-strip-card { padding: 12px 14px; border: 1px solid var(--hairline); border-radius: 8px; background: var(--bg-paper); font-size: 13px; }
.topic-strip-num { font-family: var(--mono); font-size: 10px; color: var(--fg-soft); letter-spacing: 0.06em; }
.topic-strip-name { font-weight: 600; margin-top: 2px; font-size: 13px; line-height: 1.3; }
.topic-strip-status { font-family: var(--mono); font-size: 9px; padding: 3px 7px; border-radius: 100px; letter-spacing: 0.06em; text-transform: uppercase; font-weight: 600; margin-top: 6px; display: inline-block; }
.topic-strip-status.done { background: var(--dot); color: #fff; }
.topic-strip-status.pending { background: var(--pending); color: var(--fg-soft); }
.topic-strip-count { font-family: var(--mono); font-size: 10px; color: var(--fg-soft); margin-top: 4px; letter-spacing: 0.04em; }

.filters { position: sticky; top: 0; z-index: 40; background: var(--bg); padding: 12px 0 14px; margin: 0 -24px 24px; padding-left: 24px; padding-right: 24px; border-bottom: 1px solid var(--hairline); }
.filter-row { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-bottom: 6px; }
.filter-row:last-child { margin-bottom: 0; }
.filter-label { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fg-soft); margin-right: 6px; }
.chip { font-size: 12px; padding: 6px 12px; border: 1px solid var(--hairline); border-radius: 100px; background: var(--bg-paper); cursor: pointer; color: var(--fg-muted); font-family: inherit; min-height: 30px; }
.chip:hover { border-color: rgba(0,0,0,0.3); color: var(--fg); }
.chip-active { background: var(--fg); color: #fff; border-color: var(--fg); }

.cards-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
.card { background: var(--bg-paper); border: 1px solid var(--hairline); border-radius: 12px; padding: 22px 20px; }
.card.hidden { display: none; }
.card.status-ready { border-color: rgba(10,109,47,0.22); }
.card-head { margin-bottom: 18px; padding-bottom: 14px; border-bottom: 1px solid var(--hairline-soft); }
.card-meta { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-bottom: 8px; }
.card-id { font-family: var(--mono); font-size: 11px; color: var(--fg-soft); font-weight: 600; }
.card-fmt, .card-pillar, .card-topic, .card-status { font-family: var(--mono); font-size: 10px; padding: 3px 8px; border-radius: 100px; letter-spacing: 0.05em; }
.card-fmt.fmt-lf { background: rgba(148,97,0,0.08); color: #946100; }
.card-fmt.fmt-sf { background: rgba(10,109,47,0.08); color: var(--dot); }
.card-fmt.fmt-kol { background: rgba(107,58,160,0.08); color: #6b3aa0; }
.card-pillar, .card-topic { border: 1px solid var(--hairline); color: var(--fg-muted); }
.card-status { background: var(--pending); color: var(--fg-soft); font-weight: 600; }
.card.status-ready .card-status { background: var(--dot); color: #fff; }
.card-title { margin: 6px 0 6px; font-size: 16px; font-weight: 500; line-height: 1.35; letter-spacing: -0.005em; color: var(--fg-muted); }
.card-format-spec { font-family: var(--mono); font-size: 11px; color: var(--fg-soft); letter-spacing: 0.04em; }

.card-section { padding: 18px 0 4px; }
.section-head { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.section-h { font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fg-soft); margin: 0; font-weight: 600; }

/* Angle */
.angle { display: grid; grid-template-columns: 32px 1fr; gap: 12px; padding: 16px 18px; border: 1px solid var(--hairline-soft); border-radius: 8px; margin-bottom: 12px; transition: border-color 0.15s, background 0.15s; }
.angle.picked { border-color: var(--pick); background: rgba(10,109,47,0.03); }
.angle:last-child { margin-bottom: 0; }
.angle-check { position: relative; display: inline-flex; cursor: pointer; padding-top: 2px; }
.angle-check input { position: absolute; opacity: 0; cursor: pointer; }
.checkmark { display: block; width: 22px; height: 22px; border: 2px solid var(--hairline); border-radius: 5px; background: var(--bg-paper); transition: all 0.15s; flex-shrink: 0; }
.angle-check input:checked ~ .checkmark { background: var(--pick); border-color: var(--pick); }
.angle-check input:checked ~ .checkmark::after { content: '✓'; display: block; color: #fff; font-size: 15px; line-height: 18px; text-align: center; font-weight: 700; }
.angle-content { min-width: 0; }

.video-title { margin: 0 0 4px; font-size: 17px; font-weight: 600; line-height: 1.3; letter-spacing: -0.01em; color: var(--fg); }
.approach { font-family: var(--mono); font-size: 11px; color: var(--fg-soft); letter-spacing: 0.04em; margin-bottom: 14px; text-transform: uppercase; }

.ratings { display: flex; flex-wrap: wrap; gap: 14px 18px; padding: 10px 14px; background: rgba(0,0,0,0.025); border-radius: 6px; margin-bottom: 14px; align-items: center; }
.rating-bar { display: flex; align-items: center; gap: 8px; font-size: 11px; font-family: var(--mono); flex: 1; min-width: 160px; }
.rating-label { color: var(--fg-soft); text-transform: uppercase; letter-spacing: 0.05em; min-width: 56px; font-size: 10px; }
.rating-track { flex: 1; height: 6px; background: rgba(0,0,0,0.06); border-radius: 100px; overflow: hidden; min-width: 50px; }
.rating-fill { height: 100%; border-radius: 100px; transition: width 0.3s; }
.rating-social .rating-fill { background: var(--social); }
.rating-audience .rating-fill { background: var(--audience); }
.rating-product .rating-fill { background: var(--product); }
.rating-value { color: var(--fg); font-weight: 600; min-width: 22px; text-align: right; }
.rating-overall { font-size: 12px; color: var(--fg); font-family: var(--mono); margin-left: auto; padding-left: 14px; border-left: 1px solid var(--hairline); }
.rating-overall strong { font-size: 14px; font-weight: 700; margin-left: 4px; }

.mini-script { display: flex; flex-direction: column; gap: 0; border: 1px solid var(--hairline-soft); border-radius: 6px; overflow: hidden; }
.mini-row { display: grid; grid-template-columns: 100px 1fr; gap: 12px; padding: 8px 12px; align-items: start; }
.mini-row + .mini-row { border-top: 1px dashed var(--hairline-soft); }
.mini-label { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--fg-soft); padding-top: 2px; font-weight: 600; }
.mini-text { font-size: 13px; line-height: 1.55; color: var(--fg); }

/* Comment */
.comment-block { padding-top: 14px; border-top: 1px solid var(--hairline-soft); }
.card-comment { width: 100%; min-height: 60px; padding: 10px 12px; border: 1px solid var(--hairline); border-radius: 8px; font-family: inherit; font-size: 13px; line-height: 1.5; resize: vertical; box-sizing: border-box; background: var(--bg-paper); }
.card-comment:focus { outline: 1px solid var(--fg); border-color: var(--fg); }
.card-comment::placeholder { color: rgba(0,0,0,0.3); }

/* Findings collapsed */
.findings-details { margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--hairline-soft); }
.findings-summary { cursor: pointer; font-family: var(--mono); font-size: 11px; color: var(--fg-soft); text-transform: uppercase; letter-spacing: 0.06em; user-select: none; padding: 4px 0; }
.findings-summary:hover { color: var(--fg); }
.findings { padding-left: 22px; margin: 12px 0 4px; }
.findings li { font-size: 13px; color: var(--fg-muted); line-height: 1.55; margin-bottom: 6px; }

.pending-msg { padding: 16px 18px; background: rgba(0,0,0,0.025); border-radius: 8px; border-left: 2px dashed var(--hairline); }
.pending-msg strong { display: block; font-size: 13px; color: var(--fg); margin-bottom: 4px; }
.pending-msg p { font-size: 12px; color: var(--fg-soft); margin: 0; line-height: 1.5; }

/* Sticky bottom panel */
.bottom-panel { position: fixed; bottom: 0; left: 0; right: 0; background: var(--fg); color: #fff; z-index: 100; box-shadow: 0 -2px 16px rgba(0,0,0,0.18); }
.bottom-panel.collapsed .panel-body { display: none; }
.panel-bar { display: flex; align-items: center; justify-content: space-between; padding: 14px 18px; cursor: pointer; gap: 12px; min-height: 56px; }
.panel-count { font-size: 14px; font-weight: 500; }
.panel-count .count-zero { color: #888; font-weight: 400; }
.panel-toggle { font-family: var(--mono); font-size: 11px; color: #aaa; text-transform: uppercase; letter-spacing: 0.05em; }
.panel-body { padding: 6px 18px 18px; max-height: 60vh; overflow-y: auto; }
.panel-label { display: block; font-family: var(--mono); font-size: 10px; color: #aaa; text-transform: uppercase; letter-spacing: 0.06em; margin: 12px 0 6px; }
.panel-prompt { width: 100%; min-height: 200px; padding: 12px; border: 1px solid rgba(255,255,255,0.15); border-radius: 6px; background: rgba(255,255,255,0.05); color: #fff; font-family: var(--mono); font-size: 12px; line-height: 1.55; resize: vertical; white-space: pre-wrap; box-sizing: border-box; }
.panel-actions { display: flex; gap: 8px; margin-top: 12px; flex-wrap: wrap; }
.panel-btn { padding: 10px 16px; border-radius: 8px; font-size: 13px; font-weight: 500; cursor: pointer; border: none; min-height: 40px; font-family: inherit; }
.btn-copy { background: #fff; color: #111; }
.btn-copy.copied { background: var(--dot); color: #fff; }

.foot { margin-top: 60px; padding-top: 24px; border-top: 1px solid var(--hairline); font-family: var(--mono); font-size: 11px; color: var(--fg-soft); text-transform: uppercase; letter-spacing: 0.06em; }
.foot p { margin: 4px 0; }

@media (min-width: 720px) {
  .layout { padding: 40px 32px 150px; }
  .hero h1 { font-size: 38px; }
  .topic-strip { grid-template-columns: repeat(4, 1fr); }
  .bottom-panel { max-width: 800px; left: 50%; transform: translateX(-50%); border-radius: 12px 12px 0 0; }
}
@media (min-width: 1024px) {
  .topic-strip { grid-template-columns: repeat(7, 1fr); }
}
"""


def render_html():
    cards_html = "\n".join(render_card(c) for c in CARDS)
    n_total = len(CARDS)
    n_ready = sum(1 for c in CARDS if c['status'] == 'ready')
    n_pending = n_total - n_ready
    total_angles = sum(len(c.get('angles', [])) for c in CARDS)
    card_meta = {c['id']: {'title': c['title'], 'angles': [a['video_title'] for a in c.get('angles', [])]} for c in CARDS}
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>SEA brand channel — production cards {VERSION}</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">

  <header class="hero">
    <div class="eyebrow">Sparkloop · production cards · {VERSION} · SEA</div>
    <h1>SEA brand channel — production cards</h1>
    <p class="lede">Each angle now leads with the video title (what viewers see on TikTok or YouTube). Three ratings per angle: social/viral, audience alignment, product/brand. Mini-script visible inline. Pick one or more angles per card. Drop a comment if anything needs rework. Sticky bottom panel builds the prompt.</p>
    <div class="meta">
      <span>2026-05-13</span>
      <span>{total_angles} angles ready · {n_pending} cards awaiting research</span>
    </div>
  </header>

  <div class="topic-strip">{render_topic_strip()}</div>

  <div class="filters">
    <div class="filter-row">
      <span class="filter-label">Status</span>
      <button class="chip chip-active" data-filter-status="all">All ({n_total})</button>
      <button class="chip" data-filter-status="ready">Ready ({n_ready})</button>
      <button class="chip" data-filter-status="pending">Pending ({n_pending})</button>
    </div>
    <div class="filter-row">
      <span class="filter-label">Format</span>
      <button class="chip chip-active" data-filter-format="all">All</button>
      <button class="chip" data-filter-format="lf">Long-form</button>
      <button class="chip" data-filter-format="sf">Short-form</button>
      <button class="chip" data-filter-format="kol">KOL</button>
    </div>
  </div>

  <div class="cards-grid">{cards_html}</div>

  <footer class="foot">
    <p>SEA brand channel · production cards · {VERSION}</p>
    <p>Pick angles, drop comments, copy prompt → I respond</p>
  </footer>

</div>

<div class="bottom-panel collapsed" id="bottom-panel">
  <div class="panel-bar" onclick="togglePanel()">
    <span class="panel-count"><span id="pick-count" class="count-zero">0 angles picked</span> across <span id="card-count">0</span> cards</span>
    <span class="panel-toggle" id="panel-toggle">tap to expand</span>
  </div>
  <div class="panel-body">
    <label class="panel-label">Generated prompt (auto-updates)</label>
    <textarea class="panel-prompt" id="panel-prompt" readonly></textarea>
    <div class="panel-actions">
      <button class="panel-btn btn-copy" onclick="copyPrompt()" id="btn-copy">Copy prompt</button>
    </div>
  </div>
</div>

<script type="application/json" id="card-meta">{json.dumps(card_meta)}</script>

<script>
  let cardMeta = {{}};
  let picks = {{}};
  let comments = {{}};
  const STATE_KEY = 'sea_production_cards_v3';

  function loadMeta() {{
    try {{ cardMeta = JSON.parse(document.getElementById('card-meta').textContent); }} catch(_) {{}}
  }}
  function loadState() {{
    try {{
      const s = JSON.parse(localStorage.getItem(STATE_KEY) || '{{}}');
      picks = s.picks || {{}};
      comments = s.comments || {{}};
    }} catch(_) {{}}
  }}
  function saveState() {{
    try {{ localStorage.setItem(STATE_KEY, JSON.stringify({{picks, comments}})); }} catch(_) {{}}
  }}
  function initUI() {{
    document.querySelectorAll('.angle-pick').forEach(cb => {{
      const card = cb.dataset.card;
      const idx = parseInt(cb.dataset.idx);
      if ((picks[card] || []).includes(idx)) {{
        cb.checked = true;
        cb.closest('.angle').classList.add('picked');
      }}
    }});
    document.querySelectorAll('.card-comment').forEach(ta => {{
      const card = ta.dataset.card;
      if (comments[card]) ta.value = comments[card];
    }});
  }}
  function onPickChange(e) {{
    const cb = e.target;
    const card = cb.dataset.card;
    const idx = parseInt(cb.dataset.idx);
    if (!picks[card]) picks[card] = [];
    if (cb.checked) {{
      if (!picks[card].includes(idx)) picks[card].push(idx);
      cb.closest('.angle').classList.add('picked');
    }} else {{
      picks[card] = picks[card].filter(i => i !== idx);
      if (picks[card].length === 0) delete picks[card];
      cb.closest('.angle').classList.remove('picked');
    }}
    saveState();
    updatePanel();
  }}
  function onCommentChange(e) {{
    const card = e.target.dataset.card;
    const v = e.target.value;
    if (v.trim()) comments[card] = v;
    else delete comments[card];
    saveState();
    updatePanel();
  }}
  function attachHandlers() {{
    document.querySelectorAll('.angle-pick').forEach(cb => cb.addEventListener('change', onPickChange));
    document.querySelectorAll('.card-comment').forEach(ta => ta.addEventListener('input', onCommentChange));
  }}
  function attachFilters() {{
    let activeStatus = 'all', activeFormat = 'all';
    function apply() {{
      document.querySelectorAll('.card').forEach(card => {{
        let show = true;
        if (activeStatus !== 'all' && card.dataset.status !== activeStatus) show = false;
        if (activeFormat !== 'all' && card.dataset.format !== activeFormat) show = false;
        card.classList.toggle('hidden', !show);
      }});
    }}
    document.querySelectorAll('[data-filter-status]').forEach(c => c.addEventListener('click', () => {{
      document.querySelectorAll('[data-filter-status]').forEach(x => x.classList.remove('chip-active'));
      c.classList.add('chip-active');
      activeStatus = c.dataset.filterStatus;
      apply();
    }}));
    document.querySelectorAll('[data-filter-format]').forEach(c => c.addEventListener('click', () => {{
      document.querySelectorAll('[data-filter-format]').forEach(x => x.classList.remove('chip-active'));
      c.classList.add('chip-active');
      activeFormat = c.dataset.filterFormat;
      apply();
    }}));
  }}
  function generatePrompt() {{
    const lines = [];
    lines.push('SEA production cards v3 — picks + comments:');
    lines.push('');
    const pickedCards = Object.keys(picks).filter(c => picks[c].length > 0).sort();
    let totalAngles = 0;
    pickedCards.forEach(c => totalAngles += picks[c].length);
    if (pickedCards.length === 0) {{
      lines.push('== PICKED ANGLES (none yet) ==');
    }} else {{
      lines.push(`== PICKED ANGLES (${{totalAngles}} across ${{pickedCards.length}} cards) ==`);
      lines.push('');
      pickedCards.forEach(c => {{
        const meta = cardMeta[c] || {{}};
        lines.push(`${{c}} — ${{meta.title || ''}}`);
        picks[c].sort((a,b) => a-b).forEach(idx => {{
          const angleTitle = meta.angles && meta.angles[idx-1] ? meta.angles[idx-1] : `Angle ${{idx}}`;
          lines.push(`  ${{idx}}. "${{angleTitle}}"`);
        }});
        lines.push('');
      }});
    }}
    const commentCards = Object.keys(comments).filter(c => (comments[c] || '').trim()).sort();
    if (commentCards.length > 0) {{
      lines.push('== CARD COMMENTS ==');
      lines.push('');
      commentCards.forEach(c => {{
        const meta = cardMeta[c] || {{}};
        lines.push(`${{c}} — ${{meta.title || ''}}:`);
        comments[c].trim().split('\\n').forEach(l => lines.push(`  ${{l}}`));
        lines.push('');
      }});
    }}
    lines.push('(paste back to me)');
    lines.push('- Minor / no red flags → auto-route picked angles to script drafting');
    lines.push('- Major rework → produce v4 cards');
    return lines.join('\\n');
  }}
  function updatePanel() {{
    let totalAngles = 0, cardsWithPicks = 0;
    Object.keys(picks).forEach(c => {{
      if (picks[c].length > 0) {{ totalAngles += picks[c].length; cardsWithPicks++; }}
    }});
    const countEl = document.getElementById('pick-count');
    countEl.textContent = `${{totalAngles}} angle${{totalAngles === 1 ? '' : 's'}} picked`;
    countEl.classList.toggle('count-zero', totalAngles === 0);
    document.getElementById('card-count').textContent = cardsWithPicks;
    document.getElementById('panel-prompt').value = generatePrompt();
  }}
  function togglePanel() {{
    const panel = document.getElementById('bottom-panel');
    const toggle = document.getElementById('panel-toggle');
    panel.classList.toggle('collapsed');
    toggle.textContent = panel.classList.contains('collapsed') ? 'tap to expand' : 'tap to collapse';
  }}
  function copyPrompt() {{
    const ta = document.getElementById('panel-prompt');
    const btn = document.getElementById('btn-copy');
    const flash = () => {{
      btn.textContent = 'Copied'; btn.classList.add('copied');
      setTimeout(() => {{ btn.textContent = 'Copy prompt'; btn.classList.remove('copied'); }}, 1500);
    }};
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(ta.value).then(flash).catch(() => {{
        ta.select(); try {{ document.execCommand('copy'); flash(); }} catch(_) {{}}
      }});
    }} else {{
      ta.select(); try {{ document.execCommand('copy'); flash(); }} catch(_) {{}}
    }}
  }}
  function init() {{
    loadMeta(); loadState(); initUI(); attachHandlers(); attachFilters(); updatePanel();
  }}
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
</script>

</body>
</html>'''


def main():
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    html = render_html()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built: {out_path}")
    print(f"Total HTML size: {len(html)} chars")
    n_ready = sum(1 for c in CARDS if c['status'] == 'ready')
    n_pending = sum(1 for c in CARDS if c['status'] == 'pending')
    n_angles = sum(len(c.get('angles', [])) for c in CARDS)
    print(f"Cards: {len(CARDS)} ({n_ready} ready, {n_pending} pending) · {n_angles} angles")


if __name__ == "__main__":
    main()
