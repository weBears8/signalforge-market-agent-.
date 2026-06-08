# Build — Signing Agent HQ (product MVP)

Generatori del prodotto digitale vero e proprio. Output in `../dist/`.

## Come rigenerare

```bash
pip install openpyxl reportlab
python3 build/build_workbook.py   # → dist/Signing-Agent-HQ.xlsx
python3 build/build_extras.py     # → dist/notion/*.csv + dist/Quick-Start-Guide.pdf
```

## Output (`dist/`)

| File | Cosa è |
|---|---|
| `Signing-Agent-HQ.xlsx` | Sistema completo: 9 fogli (START HERE, Settings, Companies, Signing Log, Mileage Log, Expenses, Invoice, Tax Summary, Dashboard) con **formule live**, dropdown, conditional formatting, 2 grafici e dati di esempio. Importabile in Google Sheets o Excel. |
| `notion/*.csv` | Database importabili in Notion (Signing Log, Mileage Log, Companies, Expenses) + `_README.md` con le formule Notion da aggiungere. |
| `Quick-Start-Guide.pdf` | Guida onboarding di 5 pagine. |

## Note prodotto
- Il **tasso IRS** è un singolo parametro in `Settings!B4`: aggiornandolo si ricalcola tutto (mileage, net profit, tax summary).
- Net profit per signing = `Fee paid − (Miles × IRS rate) − printing − other`.
- Tax Summary mappa le voci alla **Schedule C**.
- Disclaimer presente: organizer, non consulenza fiscale/legale.

Questo è l'**MVP** pronto da consegnare ai preordini della fase di validazione (vedi `../validation/notary-signing-agent-os/`).
