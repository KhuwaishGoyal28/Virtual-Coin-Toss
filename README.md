# Virtual Coin Toss

A desktop coin-flip app with an animated toss and running heads/tails statistics.

**Live demo:** https://virtual-coin-toss-web.vercel.app

## Features
- **Flip Coin** plays a 2-second flip animation, then shows Heads or Tails
- Results are picked uniformly at random
- Running counts with percentages, e.g. `Heads: 3 (60.0%) | Tails: 2 (40.0%)`
- **Reset** clears the statistics
- Dark theme

## Tech stack
- **Desktop app:** Python 3, PyQt6 (`coin_toss.py`)
- **Web version:** HTML, CSS (3D flip animation) and JavaScript (`web/`)

## Run locally
```bash
pip install PyQt6
python coin_toss.py
```
The desktop app looks for `coin_flip.gif`, `heads.png`, `tails.png` and `coin_icon.png` next to the script. Add your own images; the repository does not include them.

Web version: open `web/index.html`.

---

Portfolio: [khuwaish-portfolio.vercel.app](https://khuwaish-portfolio.vercel.app) · Built by **Khuwaish Goyal**
