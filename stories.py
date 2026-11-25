"""Story constants for The World Today — Wednesday 25 November 2026.

Every fact below was verified against live reporting on 25 November 2026
(Reuters, AP, CNN, New York Times via wire, Al Jazeera, BusinessWorld,
Hindu BusinessLine, NordFX market data). No story is reused from the
23 or 24 November editions except where it genuinely developed further
on 25 November.
"""

DATE_LINE = "WEDNESDAY, 25 NOVEMBER 2026"
MASTHEAD = "The World Today"
EDITION_LINE = "ONE PICTURE OF THE DAY  ·  No. 329"

LEAD_KICKER = "THE LEAD  —  MARKETS"
LEAD_HEADLINE = ["ASIA MARKETS PLUNGE", "AS TARIFF THREAT LOOMS"]
LEAD_SUMMARY = (
    "Asian shares plunged on Wednesday as a fresh US tariff threat hit "
    "sentiment and the AI rally fizzled: Seoul fell 6.4% and Taipei 8.6% "
    "at their worst, while Tokyo slid 3.6%. On Wall Street overnight the "
    "Dow closed above 50,000 for the first time, up 0.9%, even as the "
    "Nasdaq sank 1.5%."
)

# (label, percent change) — closes reported on 25 November 2026.
MARKET_BARS = [
    ("S&P 500", -0.5),
    ("Nasdaq", -1.5),
    ("Dow", 0.9),
    ("Nikkei", -3.6),
    ("KOSPI", -6.4),
    ("TAIEX", -8.6),
]

MARKETS_STRIP = (
    "S&P -0.5%  ·  Nasdaq -1.5%  ·  Dow +0.9%  ·  Nikkei -3.6%  ·  "
    "KOSPI -6.4%  ·  TAIEX -8.6%  ·  Gold -0.4%  ·  Oil -1.6%"
)

SECTION_LABEL = "MORE FROM THE DAY"

# (kicker, headline, body) — each body fits two lines at 14.5 pt.
CARDS = [
    (
        "MIDDLE EAST",
        "Houthi drone hits Riyadh tower, 11 hurt",
        "A drone struck the PIF Tower in Riyadh's financial district. "
        "The coalition hit back at Hodeidah port overnight.",
    ),
    (
        "UNITED STATES",
        "CIA and ODNI hit by hack of unclassified network",
        "Hackers broke into an unclassified intelligence network. "
        "Officials say no classified data was affected.",
    ),
    (
        "IRAN",
        "Iranian rial sinks to record low",
        "Iran's rial sank to a record low after fresh US sanctions, "
        "with the dollar past 2.85 million rials in Tehran.",
    ),
    (
        "IRAQ",
        "Iraq moves to seize Kurdish oilfields",
        "Baghdad ordered federal forces to seize oilfields and "
        "crossings in Kurdish-run regions, escalating a long dispute.",
    ),
    (
        "INDONESIA",
        "Rescue under way in Indonesian mine",
        "Rescuers are searching for dozens of miners trapped 100 "
        "metres down since Monday after heavy rain.",
    ),
    (
        "SPORT",
        "Real Madrid hit PSV for five",
        "Jude Bellingham starred and Kylian Mbappe scored twice as "
        "Real Madrid routed PSV 5-1 in the Champions League.",
    ),
]

TICKER = [
    "Nvidia slips in pre-market after its 30% rebound on Huang's return",
    "Britain sanctions the Houthis and four rebel officials",
    "Senegal's 2025 AFCON title restored by CAS ruling",
    "Vatican publishes Pope Francis' private diary",
    "US readies new tariff hikes on China and the EU",
]

FOOTER = (
    "The World Today  ·  Wednesday 25 November 2026  ·  "
    "Figures as reported on the day"
)
