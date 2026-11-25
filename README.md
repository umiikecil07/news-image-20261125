# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/umiikecil07/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/umiikecil07/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

The World Today — 25 November 2026: one-page news front page. A Python program draws the day's world news — Asia markets plunge on a fresh US tariff threat, the Houthi drone strike on Riyadh's PIF Tower, the CIA/ODNI hack, Iran's rial at a record low, Iraq's move on Kurdish oilfields, the Indonesian mine rescue, and Real Madrid's 5-1 win — into a single 1024×1024 image.

## Run it

```sh
python3 main.py
```

The program writes `entry.png` (1024×1024, deterministic) to `/output`, or to `$MAKEFUN_OUTPUT_DIR` when set. If Pillow is unavailable it copies the shipped `entry.png` instead. Fonts ship in `fonts/` (DejaVu) so rendering is identical anywhere.

---

<sub>Entered on [make.fun](https://make.fun/?ref=umiikecil07&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
