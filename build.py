#!/usr/bin/env python3
"""SEA brand channel — unified production cards page.
Each banked piece = one card with brainstorm hooks + research findings + writing angles + draft action.
"""
import os, json
from html import escape

# Topic 01 is researched. The rest have placeholder content until run.

CARDS = [
    # ===== Topic 01 — CNY rails (RESEARCHED) =====
    {
        "id": "P1-A1", "format": "LF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "Money in and out of China: the operator's full picture",
        "format_spec": "Long-form 15-20 min · bilingual EN + Mandarin · Hui Mei lead",
        "hooks": [
            "How money actually enters and leaves China when you're an operator. The full picture, end to end.",
            "Most explainers cover one direction. Operators need both: paying in, getting paid out.",
            "China money flow for operators: 4 inbound channels, 3 outbound, and the rules for each.",
        ],
        "findings": [
            "CIPS processed ¥175.49 trillion in 2024 (+42.6% YoY). The CNY rail is now real-scale infrastructure, not theoretical.",
            "80% of CIPS transactions still use SWIFT for messaging — mixed-rail reality, not a clean replacement.",
            "ASEAN remittance used to cost >6% in fees; PromptPay-PayNow now seconds at fraction of cost. The SEA backdrop has shifted.",
            "Bidirectional flow (in + out) is rarely covered as one piece — SEO + audience gap.",
            "WF SG public page does NOT name MYbank partnership. Script around this. Use 'dedicated CNY rail' / 'specialised cross-border infrastructure' framing.",
        ],
        "angles": [
            {"name": "Sequential — in then out", "blurb": "Pay suppliers (8 min) → marketplace payouts (6 min) → synthesis (2 min). Best for SEO; ranks for both directions."},
            {"name": "Problem-led — 3 things break", "blurb": "Wire rejections, FX gaps, routing delays. Each as an act. Strongest emotional pull."},
            {"name": "Day-in-the-life — 24 hours", "blurb": "9am marketplace payout, 10am supplier wire, 11am FX check, 2pm bulk transfer, 4pm receivables. Most relatable; needs an operator case."},
            {"name": "Cost-decomposition — $100K/month leaks", "blurb": "Leak 1 ($1,800 FX margin), leak 2 ($150-400 wire+intermediary), leak 3 ($1,500 payout conversion). Total $3,500-5,000/month."},
            {"name": "Question-led — 5 operator questions", "blurb": "How to pay, why supplier asks for more, how fast, marketplace payouts in CNY, when to switch off your bank. Each Q = one SF cut."},
        ],
    },
    {
        "id": "P1-A2", "format": "SF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "3 ways CNY actually reaches your supplier",
        "format_spec": "Short-form 60s · bilingual",
        "hooks": [
            "There are 3 ways your CNY reaches a Chinese supplier. Only one is same-day.",
            "Same wire, three possible paths, three different speeds.",
            "Three definitions of 'CNY transfer' in banking. Only one means CNY actually moves CNY.",
        ],
        "findings": [
            "The 3 ways: SWIFT-routed via correspondent banks; CIPS direct clearing; MYbank/Alipay corporate (for 1688).",
            "Most operators treat all three as one mechanism. The differences are speed, cost, and supplier-side amount received.",
            "1688's bank-transfer route uses MYbank cooperation for 'large-amount fund collection.'",
        ],
        "angles": [
            {"name": "Curiosity-led", "blurb": "Open with 'There are 3 ways...'. Reveal each. Best hook for TikTok."},
            {"name": "Pain-led", "blurb": "Open with 'Your supplier received USD when you sent CNY.' Then explain it's the rail."},
            {"name": "Mechanism-led demo", "blurb": "Visual: trace a $10K CNY payment through each of the 3 rails. Strongest for IG carousel + reel."},
            {"name": "Comparison-led", "blurb": "Two banks, same 'CNY transfer' label, two different outcomes."},
            {"name": "Authority-led", "blurb": "'CIPS processed $24T in 2024. Here's what it actually does.' Numbers-first."},
        ],
    },
    {
        "id": "P1-A7", "format": "SF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "Two banks offer 'CNY transfer'. Only one moves CNY.",
        "format_spec": "Short-form 45s · bilingual",
        "hooks": [
            "Two banks both say 'CNY transfer'. Only one actually sends CNY. Your supplier knows the difference.",
            "Your bank said 'CNY transfer'. Your supplier received USD. Here's what went wrong.",
            "Two definitions of 'CNY transfer' in banking. Only one matches what your supplier needs.",
        ],
        "findings": [
            "Bank A: routes via SWIFT to USD-clearing correspondent; conversion happens at correspondent end → supplier receives USD.",
            "Bank B: routes via CIPS or MYbank direct; supplier receives true CNY.",
            "Same label, different infrastructure. Marketing claims don't match operational reality.",
        ],
        "angles": [
            {"name": "Pain-first", "blurb": "Open with 'You sent CNY. Your supplier got USD. Both banks called it CNY transfer.'"},
            {"name": "Comparison split-screen", "blurb": "Visual: same wire animated through both bank flows. End frame: supplier-side amounts differ."},
            {"name": "Curiosity-led", "blurb": "'There are two definitions of CNY transfer floating around in banking.' Reveal each."},
            {"name": "Authority-led", "blurb": "'What a supplier's bank actually sees when you send CNY.' Banking-insider tone."},
            {"name": "Demo-led", "blurb": "Live screen-share: same wire, two banks, supplier-side receipt comparison."},
        ],
    },
    {
        "id": "P1-A8", "format": "SF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "The 3-letter code that decides if your wire is same-day",
        "format_spec": "Short-form 45s · bilingual",
        "hooks": [
            "There's a 3-letter code on your wire that decides if it clears same-day or in 5 business days.",
            "Your wire's SWIFT message has a routing code 99% of senders never see.",
            "One field on your wire confirmation predicts whether your supplier sees the money today or Friday.",
        ],
        "findings": [
            "Field 71A of SWIFT MT103 holds the OUR/SHA/BEN code.",
            "OUR = sender pays all; supplier gets full amount. SHA = shared; intermediaries deduct. BEN = beneficiary pays.",
            "Each intermediary bank can charge $15-50. Multiple intermediaries possible per wire.",
            "Priority SWIFT before 14:00 GMT can clear same-day; otherwise 1-5 days.",
        ],
        "angles": [
            {"name": "Curiosity-led", "blurb": "'There's a 3-letter code...'. Reveal it. Show how to find it on your confirmation."},
            {"name": "Pain-led", "blurb": "'Your supplier got $200 less. The reason is a code you didn't choose.'"},
            {"name": "Tutorial-led", "blurb": "How to switch from SHA to OUR — supplier receives full amount. Step by step."},
            {"name": "Comparison-led", "blurb": "OUR vs SHA vs BEN on a real $50K wire to Shenzhen. Three outcomes, three amounts."},
            {"name": "Authority-led", "blurb": "'Field 71A of SWIFT MT103.' Banking literacy framing. Builds trust."},
        ],
    },
    {
        "id": "P1-A9", "format": "SF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "Supplier said wire didn't arrive. Bank says it did.",
        "format_spec": "Short-form 60s · bilingual",
        "hooks": [
            "Your supplier says the wire didn't arrive. Your bank's confirmation says it did. Both can be true. Here's why.",
            "Three places your wire can sit between 'sent' and 'received'. Most operators check none of them.",
            "When your supplier and your bank disagree on whether the money arrived, here's where to actually look.",
        ],
        "findings": [
            "Wires can sit between intermediary correspondents for hours to days.",
            "Currency conversion windows add up to 2 working days.",
            "Local bank holidays in CN or SEA cause silent delays.",
            "AML/fraud thresholds can hold wires above certain amounts without notifying sender.",
            "Sender confirmation ≠ supplier receipt. The bank confirms when it sent. Receiving bank confirms when it received.",
        ],
        "angles": [
            {"name": "Pain-first", "blurb": "Open with 'Your bank says sent. Your supplier says nothing. Both right.'"},
            {"name": "Mechanism-led", "blurb": "Three places your wire can sit. Walk through each."},
            {"name": "Tutorial-led", "blurb": "How to track a missing wire to China step by step."},
            {"name": "Story-led", "blurb": "'I sent $42K Friday. Supplier got nothing by Monday. Here's what I found.'"},
            {"name": "Authority-led", "blurb": "'What sent actually means on a SWIFT wire.'"},
        ],
    },
    {
        "id": "P1-A10", "format": "SF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "The routing decision that quietly changes your fee 1%",
        "format_spec": "Short-form 45s · bilingual",
        "hooks": [
            "Your bank makes one decision on every China wire that changes your fee by up to 1%. They don't tell you.",
            "There's a routing fork on every cross-border wire. Wrong fork = 1% more.",
            "One silent backend choice can cost you $1,000 on a $100K wire to China.",
        ],
        "findings": [
            "Banks choose correspondent routing path per wire, silently.",
            "Wrong correspondent = extra intermediary = extra fee.",
            "1% on $100K = $1,000 silently extracted.",
            "Each intermediary in the chain can charge $15-50; multiple intermediaries compound.",
        ],
        "angles": [
            {"name": "Curiosity-led", "blurb": "'Your bank makes one silent decision...'"},
            {"name": "Pain-led", "blurb": "'Where did $1,000 go on your $100K wire?'"},
            {"name": "Authority-led", "blurb": "'The correspondent banks your money passes through. Most banks won't show you.'"},
            {"name": "Mechanism-led", "blurb": "Animation: wire routes through correspondents; fees deduct in real time."},
            {"name": "Comparison-led", "blurb": "Same $100K wire, two routing paths, $1,000 difference at the supplier end."},
        ],
    },
    {
        "id": "P1-A11", "format": "SF", "pillar": "P1", "topic": "01",
        "topic_name": "CNY rails + money flow to/from China", "status": "ready",
        "title": "Why your CNY payment sometimes arrives in USD",
        "format_spec": "Short-form 60s · bilingual",
        "hooks": [
            "You sent CNY. Your supplier received USD. The bank quietly converted at their rate.",
            "Sending CNY doesn't always mean your supplier gets CNY. There's a rail dependency most operators miss.",
            "When 'CNY transfer' becomes 'USD transfer' mid-flight: the routing trap.",
        ],
        "findings": [
            "Conversion can happen at sender side, correspondent, or beneficiary bank.",
            "If no CNY-direct correspondent in chain, USD conversion happens by default.",
            "Supplier ends up holding USD when expecting CNY.",
            "Supplier then converts USD → CNY at their bank → double conversion cost.",
            "Cost gets pushed back to the operator on the next quote.",
        ],
        "angles": [
            {"name": "Pain-first", "blurb": "'You sent CNY. Your supplier got USD. Their bank converted at their rate.'"},
            {"name": "Mechanism-led", "blurb": "Three places where your CNY can become USD. Visual: trace the conversion points."},
            {"name": "Curiosity-led", "blurb": "'When CNY transfer becomes USD transfer mid-flight.'"},
            {"name": "Cost-led", "blurb": "'Double conversion: who pays? Spoiler: your supplier, then you on the next order.'"},
            {"name": "Authority-led", "blurb": "'Why CIPS exists — to keep CNY as CNY end-to-end.'"},
        ],
    },

    # ===== Topic 02 — FX margin + hidden costs (PENDING, 9 cards) =====
    {"id": "P1-A12", "format": "SF", "pillar": "P1", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "$1,200 gone from a $50K supplier wire. Where.",
     "format_spec": "Short-form 45s · bilingual",
     "hooks": ["You sent $50,000. Your supplier received $48,800. The $1,200 wasn't on the wire confirmation.",
               "$1,200 silently extracted from a $50K supplier payment. Not as a fee. As FX margin.",
               "The 'no fee' wire that cost $1,200."]},
    {"id": "P1-A13", "format": "SF", "pillar": "P1", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "Bank says no fee. You still paid $300.",
     "format_spec": "Short-form 30s · bilingual",
     "hooks": ["Your bank confirmed 'no transfer fee'. Your statement shows $300 less than expected.",
               "'No fee' is one of the most expensive phrases in international banking.",
               "Fee-free transfers cost more than fee-included ones, in most cases."]},
    {"id": "P1-A14", "format": "SF", "pillar": "P1", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "Three operators, same $50K wire, three different supplier-end amounts",
     "format_spec": "Short-form 60s",
     "hooks": ["Same supplier, same $50K send, three providers. Supplier received $48,800, $49,100, $49,650.",
               "We ran the same supplier payment with three banks. The difference at the supplier end was $850.",
               "How three providers process the same wire and produce three different totals."]},
    {"id": "P1-A15", "format": "SF", "pillar": "P1", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "What 'no fee' costs you per $10K to China",
     "format_spec": "Short-form 60s · bilingual",
     "hooks": ["'No transfer fee' on a $10K wire to China typically costs $80-$120 in FX margin.",
               "The cost of free: what 'no fee' wires actually take from you per $10K.",
               "Three banks all market 'no fee' on China transfers. None are free."]},
    {"id": "P1-A16", "format": "SF", "pillar": "P1", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "Receipt says $50K. Statement says $51.2K.",
     "format_spec": "Short-form 60s",
     "hooks": ["Your wire receipt says you sent $50,000. Your account statement says $51,200 left. The $1,200 isn't a fee.",
               "When wire receipt and statement disagree by $1,200, here's which is closer to the truth.",
               "Why your wire confirmation and account statement don't match."]},
    {"id": "P2-A1", "format": "SF", "pillar": "P2", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "How a 2% bank-to-rail gap compounds over a year",
     "format_spec": "Short-form 60s",
     "hooks": ["Your local bank vs a dedicated cross-border rail: 2% gap per transaction. Run it 12 times.",
               "2% sounds small. Annual compounding on $1M of cross-border payments makes it $24K.",
               "Bank-to-rail FX gap of 2% means: a year of imports costs you a hire."]},
    {"id": "P2-A7", "format": "SF", "pillar": "P2", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "Your sourcing budget shrinks 4% a year (silent compound)",
     "format_spec": "Short-form 60s",
     "hooks": ["If you import $500K/year on a 0.4% FX margin, you're losing $2,000 silently. Per year.",
               "Three FX margin levels, same import volume. Year 3 = a holiday. Year 5 = a hire.",
               "Why every Chinese-sourcing SME should run the FX-margin math once a year."]},
    {"id": "P2-A8", "format": "SF", "pillar": "P2", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "How to read FX margin off your wire confirmation",
     "format_spec": "Short-form 60s tutorial",
     "hooks": ["Your bank's FX margin is hidden in plain sight on every wire confirmation.",
               "Two numbers on your wire confirmation can be combined to reveal your bank's FX margin.",
               "The 60-second test to see if your bank is making 0.5% or 2% on your wire FX."]},
    {"id": "P2-A9", "format": "SF", "pillar": "P2", "topic": "02", "topic_name": "FX margin + hidden costs", "status": "pending",
     "title": "Good rate quoted vs real interbank rate",
     "format_spec": "Short-form 45s",
     "hooks": ["Your bank quoted you a 'competitive rate'. The real rate was 1.4% better.",
               "How to check your bank's FX quote against the real interbank rate.",
               "The free tool that tells you if your bank's 'good rate' is actually good."]},

    # ===== Topic 03 — WF product mechanics + financial stack (PENDING, 3 cards incl. 2nd LF) =====
    {"id": "P3-A2", "format": "LF", "pillar": "P3", "topic": "03", "topic_name": "WorldFirst product mechanics", "status": "pending",
     "title": "World Account setup, end-to-end in 8 minutes",
     "format_spec": "Long-form 8-10 min tutorial · Hui Mei lead",
     "hooks": ["How to set up your World Account for cross-border payouts. 8 minutes, end-to-end.",
               "From sign-up to first payout: every step, in order.",
               "Set this up once and your marketplace payouts stop costing you 2.5%."]},
    {"id": "P3-A10", "format": "SF", "pillar": "P3", "topic": "03", "topic_name": "WorldFirst product mechanics", "status": "pending",
     "title": "Why SMEs are building a financial stack (not relying on one bank)",
     "format_spec": "Short-form 60s",
     "hooks": ["Modern SMEs don't have one bank. They have a financial stack. Here's what's in it.",
               "Local bank + cross-border specialist + marketplace tool + hedging instrument = standard 2026 setup.",
               "The 5-piece financial stack every cross-border SME should have."]},
    {"id": "P2-A3", "format": "SF", "pillar": "P2", "topic": "03", "topic_name": "WorldFirst product mechanics", "status": "pending",
     "title": "Bank wire vs WorldFirst on the same $50K payment",
     "format_spec": "Short-form 60s comparison",
     "hooks": ["Bank wire vs WorldFirst on the same $50K supplier payment. Apples to apples.",
               "Two operators, same $50K payment, two providers. Side by side.",
               "We ran the same payment with three providers. Where each one extracts cost."]},

    # ===== Topic 04 — Personal vs business tools (PENDING, 5 cards) =====
    {"id": "P2-A12", "format": "SF", "pillar": "P2", "topic": "04", "topic_name": "Personal vs business tools", "status": "pending",
     "title": "Personal cross-border tools weren't built for business",
     "format_spec": "Short-form 60s",
     "hooks": ["Cross-border money apps were built for travellers and freelancers. Once you're paying suppliers weekly, the design gaps show.",
               "Personal-tier FX tools work fine when you send money abroad sometimes.",
               "Three categories of features your business cross-border setup needs that personal tools don't offer."]},
    {"id": "P2-A13", "format": "SF", "pillar": "P2", "topic": "04", "topic_name": "Personal vs business tools", "status": "pending",
     "title": "How much PayPal actually costs you on a $20K supplier payment",
     "format_spec": "Short-form 60s",
     "hooks": ["PayPal's 'flat fee' on a $20K supplier payment is closer to 5% once you add cross-border and FX.",
               "Use PayPal for B2B and you pay three times: visible fee, cross-border surcharge, FX margin.",
               "PayPal for collecting client payments: fine. PayPal for paying suppliers: expensive."]},
    {"id": "P2-A14", "format": "SF", "pillar": "P2", "topic": "04", "topic_name": "Personal vs business tools", "status": "pending",
     "title": "Credit cards for international supplier payments: the gap",
     "format_spec": "Short-form 60s",
     "hooks": ["Why your credit card mostly doesn't work for paying Chinese suppliers.",
               "3% credit card fee on a $20K supplier order = $600. Before FX.",
               "The credit card workaround SEA importers use, and the better path."]},
    {"id": "P2-A18", "format": "SF", "pillar": "P2", "topic": "04", "topic_name": "Personal vs business tools", "status": "pending",
     "title": "Personal vs business FX rate: the spread",
     "format_spec": "Short-form 60s",
     "hooks": ["Personal cross-border tools quote retail rates. Business tools quote near-interbank. The spread can be 1.5%.",
               "Why the FX rate on a personal app is different from what your business should expect.",
               "1.5% spread × $500K cross-border = $7,500/year."]},
    {"id": "P2-A24", "format": "SF", "pillar": "P2", "topic": "04", "topic_name": "Personal vs business tools", "status": "pending",
     "title": "When CAN you pay a Chinese supplier by card?",
     "format_spec": "Short-form 60s",
     "hooks": ["There are 4 scenarios where a credit card actually works for paying a Chinese supplier.",
               "Card payment to China: small set of cases where it's an option.",
               "Trading companies that accept cards: a checklist."]},

    # ===== Topic 05 — Paying in CNY economics (PENDING, 1 card) =====
    {"id": "P1-A6", "format": "SF", "pillar": "P1", "topic": "05", "topic_name": "Paying in CNY economics", "status": "pending",
     "title": "Why paying your supplier in CNY actually wins",
     "format_spec": "Short-form 60s · bilingual",
     "hooks": ["Paying in USD feels safer. Paying in CNY costs less and lands faster.",
               "Three reasons your supplier prefers CNY. One quietly lowers your unit cost.",
               "USD to your supplier means two conversions. CNY means one."]},

    # ===== Topic 06 — Wire rejection / failure modes (PENDING, 2 cards) =====
    {"id": "P1-A4", "format": "SF", "pillar": "P1", "topic": "06", "topic_name": "Wire rejection failure modes", "status": "pending",
     "title": "Your supplier asked you to pay the $200 they didn't receive",
     "format_spec": "Short-form 60s · bilingual",
     "hooks": ["Your supplier received $200 less than you sent. They're asking you to pay the difference.",
               "Sent $10K. Supplier got $9,800. The bank took fee on both ends of the same payment.",
               "Why does anyone pay the bank's FX margin in the first place?"]},
    {"id": "P1-A5", "format": "SF", "pillar": "P1", "topic": "06", "topic_name": "Wire rejection failure modes", "status": "pending",
     "title": "SWIFT vs the alternatives: which actually pays your supplier faster",
     "format_spec": "Short-form 60s · bilingual",
     "hooks": ["SWIFT is the bank's default for international payments. Here's how it works, then here's what beats it.",
               "Your bank sends through SWIFT. That's why your payment takes 3-5 days.",
               "First, what SWIFT actually does. Then, why faster rails exist."]},

    # ===== Topic 07 — Switch-point math KOL (PENDING, 1 card) =====
    {"id": "P2-A6", "format": "KOL", "pillar": "P2", "topic": "07", "topic_name": "Switch-point math (KOL)", "status": "pending",
     "title": "The break-even: when should you switch providers?",
     "format_spec": "KOL distributed · math/decision-led",
     "hooks": ["At what monthly import volume does staying with your bank cost more than switching?",
               "Below $X/month in supplier payments, your bank is fine. Above $X, you're paying for sticking.",
               "The break-even point where 'inconvenience of switching' costs more than 'price of staying'."]},
]

TOPIC_STATUS = {
    "01": ("done", "CNY rails + money flow", "https://socialworldfirst.github.io/sea-listen-cny-rails/"),
    "02": ("pending", "FX margin + hidden costs", None),
    "03": ("pending", "WorldFirst product mechanics", None),
    "04": ("pending", "Personal vs business tools", None),
    "05": ("pending", "Paying in CNY economics", None),
    "06": ("pending", "Wire rejection failure modes", None),
    "07": ("pending", "Switch-point math (KOL)", None),
}


def render_card(c):
    fmt_class = f"fmt-{c['format'].lower()}"
    status_class = "ready" if c['status'] == 'ready' else "pending"
    hooks_html = "\n".join(f'<li>{escape(h)}</li>' for h in c['hooks'])

    if c['status'] == 'ready':
        findings_html = "\n".join(f'<li>{escape(f)}</li>' for f in c.get('findings', []))
        findings_block = f'''
        <div class="card-section findings-block">
          <h4 class="section-h">Research findings</h4>
          <ul class="findings">{findings_html}</ul>
        </div>'''
        angles_html = "\n".join(
            f'''<div class="angle">
              <div class="angle-name">{escape(a['name'])}</div>
              <div class="angle-blurb">{escape(a['blurb'])}</div>
            </div>'''
            for a in c.get('angles', [])
        )
        angles_block = f'''
        <div class="card-section angles-block">
          <h4 class="section-h">Writing angles ({len(c.get('angles', []))})</h4>
          <div class="angles">{angles_html}</div>
        </div>'''
        action_text = f"Draft script ({c['format']})"
        action_disabled = ""
    else:
        topic_info = TOPIC_STATUS.get(c['topic'])
        topic_label = topic_info[1] if topic_info else c['topic']
        findings_block = f'''
        <div class="card-section findings-pending">
          <h4 class="section-h">Research findings</h4>
          <p class="pending-note">Pending — research run for Topic {c['topic']} ({escape(topic_label)}) not yet executed. Findings will appear here when the topic batch completes.</p>
        </div>'''
        angles_block = f'''
        <div class="card-section angles-pending">
          <h4 class="section-h">Writing angles</h4>
          <p class="pending-note">Generated after research run.</p>
        </div>'''
        action_text = "Awaiting research"
        action_disabled = " disabled"

    return f'''
<article class="card status-{status_class}" id="{c['id']}" data-format="{c['format'].lower()}" data-status="{c['status']}" data-topic="{c['topic']}">
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

  <div class="card-section hooks-block">
    <h4 class="section-h">Hook variants ({len(c['hooks'])})</h4>
    <ul class="hooks">{hooks_html}</ul>
  </div>

  {findings_block}
  {angles_block}

  <footer class="card-foot">
    <button class="draft-btn{action_disabled}">{action_text}</button>
  </footer>
</article>
'''


def render_template_sample(format_type):
    if format_type == "LF":
        return '''
<div class="template-card">
  <div class="template-head"><span class="template-tag fmt-lf">LF</span><h4>Long-form script template</h4></div>
  <div class="template-body">
    <div class="template-row"><span class="template-time">0:00-0:30</span><span class="template-beat"><strong>Hook</strong> — opening line, frame the piece, why watch</span></div>
    <div class="template-row"><span class="template-time">0:30-X:XX</span><span class="template-beat"><strong>Act 1</strong> — section name · 3-4 beats · transition</span></div>
    <div class="template-row"><span class="template-time">X:XX-X:XX</span><span class="template-beat"><strong>Act 2</strong> — section name · 3-4 beats · transition</span></div>
    <div class="template-row"><span class="template-time">X:XX-X:XX</span><span class="template-beat"><strong>Act 3 / Synthesis</strong> — section name · bring it together</span></div>
    <div class="template-row"><span class="template-time">X:XX-end</span><span class="template-beat"><strong>Close + CTA</strong> — final takeaway · subscribe / follow</span></div>
  </div>
  <div class="template-extras">
    <div class="template-extra"><strong>B-roll cues:</strong> per beat</div>
    <div class="template-extra"><strong>On-screen text:</strong> per beat</div>
    <div class="template-extra"><strong>Bilingual notes:</strong> EN + Mandarin same-day record where flagged</div>
  </div>
</div>'''
    else:  # SF
        return '''
<div class="template-card">
  <div class="template-head"><span class="template-tag fmt-sf">SF</span><h4>Short-form script template</h4></div>
  <div class="template-body">
    <div class="template-row"><span class="template-time">0-5s</span><span class="template-beat"><strong>Hook</strong> — opening line · scroll-stop visual</span></div>
    <div class="template-row"><span class="template-time">5-50s</span><span class="template-beat"><strong>Body</strong> — beat 1 · beat 2 · beat 3 (max) · payoff</span></div>
    <div class="template-row"><span class="template-time">50-60s</span><span class="template-beat"><strong>Close</strong> — one-line tag · CTA</span></div>
  </div>
  <div class="template-extras">
    <div class="template-extra"><strong>Hook variants:</strong> 3 alternatives drafted, pick on test</div>
    <div class="template-extra"><strong>Visual direction:</strong> shot list, on-screen text moments</div>
    <div class="template-extra"><strong>Caption:</strong> platform-native variants (TikTok / IG / FB)</div>
  </div>
</div>'''


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
  --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
}
html, body { margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif; background: var(--bg); color: var(--fg); -webkit-font-smoothing: antialiased; line-height: 1.6; font-size: 16px; }
a { color: var(--fg); }

.layout { max-width: 1200px; margin: 0 auto; padding: 32px 24px 120px; }

.hero { padding-bottom: 28px; border-bottom: 1px solid var(--hairline); margin-bottom: 32px; }
.eyebrow { font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--fg-soft); margin-bottom: 14px; }
.hero h1 { font-size: 32px; line-height: 1.15; font-weight: 600; letter-spacing: -0.02em; margin: 0 0 14px; }
.lede { font-size: 16px; line-height: 1.55; color: var(--fg-muted); max-width: 720px; margin: 0 0 18px; }
.meta { display: flex; flex-wrap: wrap; gap: 14px 28px; font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fg-soft); }

/* Filters */
.filters { position: sticky; top: 0; z-index: 40; background: var(--bg); padding: 12px 0 14px; margin: 0 -24px 24px; padding-left: 24px; padding-right: 24px; border-bottom: 1px solid var(--hairline); }
.filter-row { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-bottom: 6px; }
.filter-row:last-child { margin-bottom: 0; }
.filter-label { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fg-soft); margin-right: 6px; }
.chip { font-size: 12px; padding: 6px 12px; border: 1px solid var(--hairline); border-radius: 100px; background: var(--bg-paper); cursor: pointer; color: var(--fg-muted); font-family: inherit; min-height: 30px; }
.chip:hover { border-color: rgba(0,0,0,0.3); color: var(--fg); }
.chip-active { background: var(--fg); color: #fff; border-color: var(--fg); }

/* Topic strip */
.topic-strip { margin-bottom: 28px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
.topic-strip-card { padding: 14px 16px; border: 1px solid var(--hairline); border-radius: 8px; background: var(--bg-paper); font-size: 13px; }
.topic-strip-num { font-family: var(--mono); font-size: 10px; color: var(--fg-soft); letter-spacing: 0.06em; }
.topic-strip-name { font-weight: 600; margin-top: 2px; font-size: 14px; }
.topic-strip-status { font-family: var(--mono); font-size: 10px; padding: 3px 8px; border-radius: 100px; letter-spacing: 0.06em; text-transform: uppercase; font-weight: 600; margin-top: 6px; display: inline-block; }
.topic-strip-status.done { background: var(--dot); color: #fff; }
.topic-strip-status.pending { background: var(--pending); color: var(--fg-soft); }

/* Cards grid */
.cards-grid { display: grid; grid-template-columns: 1fr; gap: 14px; }
.card { background: var(--bg-paper); border: 1px solid var(--hairline); border-radius: 10px; padding: 22px 20px; }
.card.hidden { display: none; }
.card.status-ready { border-color: rgba(10,109,47,0.25); }
.card-head { margin-bottom: 18px; padding-bottom: 14px; border-bottom: 1px solid var(--hairline-soft); }
.card-meta { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-bottom: 8px; }
.card-id { font-family: var(--mono); font-size: 11px; color: var(--fg-soft); font-weight: 600; letter-spacing: 0.03em; }
.card-fmt, .card-pillar, .card-topic, .card-status { font-family: var(--mono); font-size: 10px; padding: 3px 8px; border-radius: 100px; letter-spacing: 0.05em; }
.card-fmt.fmt-lf { background: rgba(148,97,0,0.08); color: #946100; }
.card-fmt.fmt-sf { background: rgba(10,109,47,0.08); color: var(--dot); }
.card-fmt.fmt-kol { background: rgba(107,58,160,0.08); color: #6b3aa0; }
.card-pillar, .card-topic { border: 1px solid var(--hairline); color: var(--fg-muted); }
.card-status { background: var(--pending); color: var(--fg-soft); font-weight: 600; }
.card.status-ready .card-status { background: var(--dot); color: #fff; }
.card-title { margin: 6px 0 6px; font-size: 18px; font-weight: 600; line-height: 1.35; letter-spacing: -0.01em; }
.card-format-spec { font-family: var(--mono); font-size: 11px; color: var(--fg-soft); letter-spacing: 0.04em; }

.card-section { padding: 14px 0 4px; border-top: 1px solid var(--hairline-soft); margin-top: 12px; }
.card-section:first-of-type { border-top: none; padding-top: 4px; margin-top: 0; }
.section-h { font-family: var(--mono); font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--fg-soft); margin: 0 0 10px; font-weight: 600; }

.hooks, .findings { padding-left: 22px; margin: 0; }
.hooks li, .findings li { font-size: 13px; color: var(--fg); line-height: 1.55; margin-bottom: 6px; }
.findings li { color: var(--fg-muted); }

.angles { display: grid; grid-template-columns: 1fr; gap: 10px; }
.angle { padding: 10px 12px; background: rgba(0,0,0,0.025); border-radius: 6px; }
.angle-name { font-size: 13px; font-weight: 600; color: var(--fg); margin-bottom: 3px; }
.angle-blurb { font-size: 12px; color: var(--fg-muted); line-height: 1.5; }

.pending-note { font-size: 12px; color: var(--fg-soft); font-style: italic; margin: 4px 0 0; line-height: 1.5; padding: 8px 12px; background: rgba(0,0,0,0.02); border-radius: 6px; border-left: 2px dashed var(--hairline); }

.card-foot { padding-top: 16px; margin-top: 14px; border-top: 1px solid var(--hairline-soft); }
.draft-btn { padding: 9px 16px; font-size: 13px; font-family: inherit; background: var(--fg); color: #fff; border: none; border-radius: 8px; cursor: pointer; min-height: 38px; font-weight: 500; }
.draft-btn:hover { background: #333; }
.draft-btn:disabled, .draft-btn.disabled { background: var(--pending); color: var(--fg-soft); cursor: not-allowed; }

/* TEMPLATES SECTION */
.templates { margin-top: 56px; padding-top: 36px; border-top: 1px solid var(--hairline); }
.templates h2 { font-size: 24px; font-weight: 600; margin: 0 0 8px; letter-spacing: -0.015em; }
.templates p { font-size: 14px; color: var(--fg-muted); margin: 0 0 22px; max-width: 640px; line-height: 1.55; }
.templates-grid { display: grid; grid-template-columns: 1fr; gap: 14px; }
.template-card { background: var(--bg-paper); border: 1px solid var(--hairline); border-radius: 10px; padding: 22px 20px; }
.template-head { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.template-head h4 { margin: 0; font-size: 15px; font-weight: 600; }
.template-tag { font-family: var(--mono); font-size: 10px; padding: 3px 8px; border-radius: 100px; letter-spacing: 0.05em; font-weight: 600; }
.template-tag.fmt-lf { background: rgba(148,97,0,0.12); color: #946100; }
.template-tag.fmt-sf { background: rgba(10,109,47,0.12); color: var(--dot); }
.template-body { border: 1px solid var(--hairline-soft); border-radius: 6px; overflow: hidden; }
.template-row { display: grid; grid-template-columns: 100px 1fr; gap: 14px; padding: 10px 14px; border-bottom: 1px solid var(--hairline-soft); }
.template-row:last-child { border-bottom: none; }
.template-time { font-family: var(--mono); font-size: 11px; color: var(--fg-soft); padding-top: 2px; }
.template-beat { font-size: 13px; line-height: 1.5; }
.template-extras { margin-top: 14px; padding-top: 14px; border-top: 1px dashed var(--hairline); display: grid; grid-template-columns: 1fr; gap: 6px; }
.template-extra { font-size: 12px; color: var(--fg-muted); }
.template-extra strong { color: var(--fg); }

/* FOOT */
.foot { margin-top: 60px; padding-top: 24px; border-top: 1px solid var(--hairline); font-family: var(--mono); font-size: 11px; color: var(--fg-soft); text-transform: uppercase; letter-spacing: 0.06em; }
.foot p { margin: 4px 0; }

@media (min-width: 720px) {
  .layout { padding: 40px 32px 140px; }
  .hero h1 { font-size: 38px; }
  .cards-grid { grid-template-columns: 1fr; }
  .topic-strip { grid-template-columns: repeat(4, 1fr); }
  .templates-grid { grid-template-columns: 1fr 1fr; }
  .angles { grid-template-columns: 1fr 1fr; }
}
@media (min-width: 1024px) {
  .topic-strip { grid-template-columns: repeat(7, 1fr); }
}
"""


def render_topic_strip():
    cards_per_topic = {}
    for c in CARDS:
        cards_per_topic.setdefault(c["topic"], 0)
        cards_per_topic[c["topic"]] += 1
    out = []
    for topic_num, (status, name, _) in TOPIC_STATUS.items():
        count = cards_per_topic.get(topic_num, 0)
        status_class = "done" if status == "done" else "pending"
        out.append(f'''
<div class="topic-strip-card">
  <div class="topic-strip-num">TOPIC {topic_num}</div>
  <div class="topic-strip-name">{escape(name)}</div>
  <div class="topic-strip-status {status_class}">{status.upper()}</div>
  <div style="font-size: 11px; color: var(--fg-soft); margin-top: 4px; font-family: var(--mono);">{count} cards</div>
</div>''')
    return "\n".join(out)


def render_html():
    cards_html = "\n".join(render_card(c) for c in CARDS)
    n_total = len(CARDS)
    n_ready = sum(1 for c in CARDS if c["status"] == "ready")
    n_pending = n_total - n_ready
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>SEA brand channel — production cards</title>
<style>{CSS}</style>
</head>
<body>
<div class="layout">

  <header class="hero">
    <div class="eyebrow">Sparkloop · production cards · SEA v4</div>
    <h1>SEA brand channel — production cards</h1>
    <p class="lede">All 30 banked pieces in one place. Each card has its hooks (from brainstorm), research findings (from /spark_listen), writing angles (suggested approaches), and a draft button. When research lands for a topic, every card in that topic unlocks. Two script templates at the bottom — Long-form and Short-form drafting paths.</p>
    <div class="meta">
      <span>2026-05-13</span>
      <span>{n_total} pieces</span>
      <span>{n_ready} ready · {n_pending} awaiting research</span>
    </div>
  </header>

  <div class="topic-strip">
    {render_topic_strip()}
  </div>

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
    <div class="filter-row">
      <span class="filter-label">Topic</span>
      <button class="chip chip-active" data-filter-topic="all">All</button>
      <button class="chip" data-filter-topic="01">01</button>
      <button class="chip" data-filter-topic="02">02</button>
      <button class="chip" data-filter-topic="03">03</button>
      <button class="chip" data-filter-topic="04">04</button>
      <button class="chip" data-filter-topic="05">05</button>
      <button class="chip" data-filter-topic="06">06</button>
      <button class="chip" data-filter-topic="07">07</button>
    </div>
  </div>

  <div class="cards-grid">
    {cards_html}
  </div>

  <section class="templates">
    <h2>Script templates</h2>
    <p>When you click "Draft script" on a card, it routes into one of these two templates. Long-form needs structural acts, pacing, B-roll. Short-form needs tight hook + body + payoff. Different drafting flows for each.</p>
    <div class="templates-grid">
      {render_template_sample("LF")}
      {render_template_sample("SF")}
    </div>
  </section>

  <footer class="foot">
    <p>SEA brand channel · production cards · v0</p>
    <p>Generated 2026-05-13 · Hooks from brainstorm · Findings + angles from /spark_listen runs</p>
  </footer>

</div>

<script>
  const statusChips = document.querySelectorAll('[data-filter-status]');
  const formatChips = document.querySelectorAll('[data-filter-format]');
  const topicChips = document.querySelectorAll('[data-filter-topic]');
  let activeStatus = 'all', activeFormat = 'all', activeTopic = 'all';
  function apply() {{
    document.querySelectorAll('.card').forEach(card => {{
      let show = true;
      if (activeStatus !== 'all' && card.dataset.status !== activeStatus) show = false;
      if (activeFormat !== 'all' && card.dataset.format !== activeFormat) show = false;
      if (activeTopic !== 'all' && card.dataset.topic !== activeTopic) show = false;
      card.classList.toggle('hidden', !show);
    }});
  }}
  function attach(chips, key) {{
    chips.forEach(c => c.addEventListener('click', () => {{
      chips.forEach(x => x.classList.remove('chip-active'));
      c.classList.add('chip-active');
      const val = c.dataset[key];
      if (key === 'filterStatus') activeStatus = val;
      else if (key === 'filterFormat') activeFormat = val;
      else if (key === 'filterTopic') activeTopic = val;
      apply();
    }}));
  }}
  attach(statusChips, 'filterStatus');
  attach(formatChips, 'filterFormat');
  attach(topicChips, 'filterTopic');
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
    print(f"Cards: {len(CARDS)} ({sum(1 for c in CARDS if c['status']=='ready')} ready, {sum(1 for c in CARDS if c['status']=='pending')} pending)")


if __name__ == "__main__":
    main()
