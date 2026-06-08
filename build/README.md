# Build — Signing Agent HQ (product MVP)

Generatori del prodotto digitale vero e proprio. Output in `../dist/`.

## Come rigenerare

```bash
pip install openpyxl reportlab pillow
python3 build/build_workbook.py   # → dist/Signing-Agent-HQ.xlsx
python3 build/build_extras.py     # → dist/notion/*.csv + dist/Quick-Start-Guide.pdf
python3 build/build_cover.py      # → dist/marketing/cover-2000.png + hero-1600x900.png
python3 build/build_lead_magnet.py # → dist/lead-magnet/ (free mileage log: xlsx + printable PDF)
python3 build/build_checklist.py  # → dist/bundle/First-90-Days-Launch-Checklist.pdf
python3 build/build_ads.py        # → dist/marketing/ads/ (3 creative top-of-funnel)
```

## Output (`dist/`)

| File | Cosa è |
|---|---|
| `Signing-Agent-HQ.xlsx` | Sistema completo: 9 fogli (START HERE, Settings, Companies, Signing Log, Mileage Log, Expenses, Invoice, Tax Summary, Dashboard) con **formule live**, dropdown, conditional formatting, 2 grafici e dati di esempio. Importabile in Google Sheets o Excel. |
| `notion/*.csv` | Database importabili in Notion (Signing Log, Mileage Log, Companies, Expenses) + `_README.md` con le formule Notion da aggiungere. |
| `Quick-Start-Guide.pdf` | Guida onboarding di 5 pagine. |
| `marketing/cover-2000.png` · `hero-1600x900.png` | Cover quadrata (Etsy/social) e hero wide (Gumroad/landing). Generate con Pillow, palette brand. |
| `marketing/ads/*.png` | 3 creative top-of-funnel (feed quadrato, pin Pinterest, story/reel) con caption pronte in `ads/README.md`. |
| `landing/index.html` | Landing statica deployabile (vedi `../dist/landing/README.md`) — riusa l'hero come screenshot prodotto. |
| `lead-magnet/Notary-Mileage-Log.xlsx` · `…-printable.pdf` | **Lead magnet gratuito** (top-of-funnel): mileage log IRS con formule live + versione stampabile per l'auto. Bridge di upsell al prodotto a $19. |
| `bundle/First-90-Days-Launch-Checklist.pdf` | Bonus del bundle: checklist brandizzata e stampabile per il nuovo agente (commissione → primi 10 signing), agganciata al sistema. |

## Note prodotto
- Il **tasso IRS** è un singolo parametro in `Settings!B4`: aggiornandolo si ricalcola tutto (mileage, net profit, tax summary).
- Net profit per signing = `Fee paid − (Miles × IRS rate) − printing − other`.
- Tax Summary mappa le voci alla **Schedule C**.
- Disclaimer presente: organizer, non consulenza fiscale/legale.

Questo è l'**MVP** pronto da consegnare ai preordini della fase di validazione (vedi `../validation/notary-signing-agent-os/`).
