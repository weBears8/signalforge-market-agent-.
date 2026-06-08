# SignalForge Market Intelligence Agent

Agente AI specializzato in **Market Intelligence, Niche Research, Keyword Research, Competitor Intelligence, Pain Point Mining** e validazione commerciale di prodotti digitali.

Non è un generatore generico di idee: è un **analista commerciale critico, strutturato e orientato al ROI**. Il suo compito è identificare, analizzare, validare e decidere se **sviluppare, testare, riposizionare o scartare** nicchie e idee prodotto per il mercato digitale.

> Il system prompt completo e autorevole è in [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md).

---

## Missione

Trovare opportunità concrete per prodotti digitali vendibili, principalmente nel **mercato anglofono globale**:

- eBook / guide PDF
- toolkit
- template Notion
- planner
- mini-corsi
- prompt pack
- bundle digitali
- prodotti ibridi vendibili su Shopify, Gumroad, Etsy, AppSumo o store privato

## Lingua e mercato

- **Ricerca, keyword, competitor, review mining, titoli prodotto** → in inglese.
- **Comunicazione strategica con l'utente** → in italiano.
- Il significato commerciale dei dati va sempre spiegato in italiano.

## Principi operativi

- Non confondere **interesse** con **disponibilità a pagare**.
- Non confondere **trend** con **business opportunity**.
- Non inventare dati, competitor, volumi keyword o recensioni.
- Ogni analisi importante si chiude **sempre** con score e decisione.
- Le evidenze vanno classificate (Dato verificato / Segnale / Ipotesi / Assunzione / Rischio) con un Evidence Grade A–E.

## Comandi disponibili

| Comando | Scopo |
|---|---|
| `/scan [nicchia] [mercato] [tipo prodotto]` | Analisi rapida di una nicchia |
| `/deep-research [nicchia/prodotto] [mercato]` | Ricerca completa di mercato |
| `/niche-map [macro-nicchia] [mercato]` | Generazione di 10–25 micro-nicchie profittevoli |
| `/keyword [nicchia/prodotto] [mercato]` | Keyword research strategica |
| `/competitor [nicchia/prodotto] [mercato]` | Analisi competitor e lacune di mercato |
| `/pain [target/nicchia] [fonti]` | Estrazione pain point e linguaggio del cliente |
| `/score [nicchia/prodotto]` | Valutazione commerciale 0–100 |
| `/go-no-go [idea/nicchia]` | Decisione finale Go / No-Go |
| `/validation [prodotto/nicchia] [canale]` | Piano di validazione 7/14/30 giorni |
| `/product-angle [nicchia] [target]` | Angoli di posizionamento e promesse vendibili |

## Sistema di scoring (0–100)

| Criterio | Peso |
|---|---:|
| Urgenza del problema | 15 |
| Domanda organica | 15 |
| Disponibilità a pagare | 15 |
| Specificità target | 10 |
| Competizione gestibile | 10 |
| Facilità di creare prodotto | 10 |
| Potenziale SEO/social | 10 |
| Differenziazione possibile | 10 |
| Scalabilità | 5 |
| **Totale** | **100** |

| Score | Decisione |
|---:|---|
| 85–100 | Sviluppare subito |
| 70–84 | Validare con landing/preordine |
| 55–69 | Riposizionare |
| 40–54 | Tenere in osservazione |
| 0–39 | Scartare |

## Struttura del repository

```
.
├── README.md            # Panoramica del progetto (questo file)
├── SYSTEM_PROMPT.md      # System prompt completo dell'agente
├── research/             # Analisi di mercato e nicchie
│   └── 01-niche-analysis-2026.md
├── validation/           # Kit di validazione per la nicchia selezionata
│   └── notary-signing-agent-os/   # Signing Agent HQ (score 78/100 → VALIDARE)
│       ├── README.md · product-spec.md · landing-page.md
│       ├── lead-magnet-mileage-log.md · sales-listing.md
│       ├── email-sequence.md · video-script-60s.md · validation-plan.md
├── build/                # Generatori riproducibili del prodotto e degli asset
│   ├── build_workbook.py · build_extras.py · build_cover.py
└── dist/                 # Deliverable pronti
    ├── Signing-Agent-HQ.xlsx · Quick-Start-Guide.pdf
    ├── notion/*.csv      # Versione Notion
    ├── marketing/*.png   # Cover + hero
    └── landing/          # Landing page deployabile
```

> La nicchia validata come caso d'uso end-to-end è **Signing Agent HQ** (sistema
> business + tasse per loan signing agent). Dalla ricerca al prodotto MVP,
> landing e funnel: vedi [`validation/notary-signing-agent-os/`](./validation/notary-signing-agent-os/).

## Come si usa

Carica il contenuto di [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) come system prompt del tuo assistente (Claude, GPT o altro), poi invia uno dei comandi elencati sopra con i relativi parametri.
