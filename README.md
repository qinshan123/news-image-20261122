[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/qinshan123/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/qinshan123/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World Today — 22 November 2026 in one image

Entry for the make.fun bounty **"Sum up 22 November's world news in one image"**
(news-image-20261122).

## What it is

A newspaper front page that sums up Sunday 22 November 2026 in a single
1024×1024 picture:

- **Headline:** COP31 talks collapse in Antalya — after a record 48 hours of
  overtime, nearly 200 nations leave Türkiye with no deal, as the EU and
  climate-vulnerable states reject a text with no fossil-fuel phase-out.
- **Middle East:** Iran strikes Bahrain; two tankers hit near Hormuz.
- **Libya:** Russian corvette Merkury ablaze at Benghazi after a suspected
  Ukrainian sea-drone attack.
- **Mexico:** FBI most-wanted cartel kingpin 'El Chapo Isidro' captured.
- **Washington:** Hackers breach the FBI's NCIC crime database.
- **Ticker:** Russian Kh-101 missiles confirmed in Polish airspace ·
  Netanyahu–Eisenkot talks end without a deal · India–China border talks ·
  Liverpool rout Manchester United 4–0.

All stories were cross-checked across multiple international outlets on
the day.

## How it runs

`main.py` (Python 3.13, standard library only, no network) writes the
finished poster to `/output/entry.png`, byte for byte, so repeated runs
are identical. The poster is composed by `build_poster.py` (Pillow) from
the generated cover art in `assets/` and the day's headlines.

## License

MIT — see `LICENSE`.
