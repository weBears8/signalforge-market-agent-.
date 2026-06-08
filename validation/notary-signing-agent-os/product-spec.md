# Product Spec — Signing Agent HQ

**The Complete Notary Business & Tax System** (Google Sheets + Notion, one-time purchase)

Promessa (EN): *"Track every signing, capture every mile, and walk into tax season ready — in one system."*
Meccanismo unico: dashboard che calcola **profitto netto per signing** + **export pronto per la Schedule C** (ciò che i printable monouso NON fanno).

---

## Architettura (doppia versione)

- **Versione A — Google Sheets** (primaria): tutto calcolato con formule, zero abbonamento.
- **Versione B — Notion** (per chi vive in Notion): stesse viste in database collegati.
- **Quick-Start PDF** (5 pagine): come duplicare, come inserire il primo signing, come fare l'export tasse.

---

## Moduli e schema dati

### 1. Signing Log / CRM (foglio principale)
Una riga = un appuntamento.

| Colonna | Tipo | Note / formula |
|---|---|---|
| Date | data | data del signing |
| Company | testo/dropdown | da "Companies" (modulo 6) |
| Order # | testo | riferimento title/escrow |
| Borrower | testo | nome firmatario |
| Appt type | dropdown | Refi / Purchase / Seller / HELOC / Apostille / RON / Inspection |
| Fee quoted | valuta | importo pattuito |
| Fee paid | valuta | incassato |
| Status | dropdown | Scheduled / Completed / Docs back / Invoiced / **Paid** / Cancelled |
| Miles round-trip | numero | per deduzione |
| Print pages | numero | costo stampa stimato |
| Notes | testo | parcheggio difficile, doc mancanti, ecc. |
| **Net profit** | formula | `Fee paid − (Miles×IRS_rate) − print − other` |
| Paid? | checkbox | filtro "da incassare" |

### 2. Mileage Log (IRS-compliant)
| Date | Purpose/Order # | Start | End | Miles | Deduction ($) |
- `Deduction = Miles × IRS_standard_rate` (cella parametro aggiornabile ogni anno).
- Totale annuo pronto per la dichiarazione.

### 3. Profit per Appointment (dashboard)
- Net profit medio per signing, per mese, per company.
- Migliori/peggiori title companies per redditività.
- Grafico income mensile + obiettivo.

### 4. Tax Summary (pronto-Schedule C)
Aggrega per categoria IRS:
- Gross income (somma Fee paid)
- Car/mileage deduction (da modulo 2)
- Supplies, E&O insurance, training/education, phone/internet %, NNA membership, software, marketing.
- Output: **riga per riga mappata alle voci Schedule C** → da consegnare al commercialista.
- ⚠️ Disclaimer in chiaro: *organizer, non consulenza fiscale.*

### 5. Invoice (template)
- Foglio fattura compilabile (logo, dati agente, voci, totale) → export PDF/stampa.
- Collegato al Signing Log per riempire automaticamente i campi.

### 6. Companies Rolodex (CRM title/escrow)
| Company | Contact | Phone/Email | Avg fee | Pay speed (gg) | Rating ★ | Notes |
- Permette di **scegliere i clienti migliori** (chi paga di più e prima). Differenziatore forte: nessun printable lo fa.

### 7. Expenses & Supplies Tracker
| Date | Category | Vendor | Amount | Deductible? |

### 8. Income Goal Dashboard
- Obiettivo mensile/annuo, signing necessari, gap, proiezione.

### 9. BONUS — First 90 Days Launch Checklist
Aggancia la **coorte di nuovi agenti**:
- Settimana 1: commissione notarile, E&O insurance, background check (NNA), journal.
- Settimana 2-4: certificazione signing agent, profili sui database (Snapdocs/SigningOrder), set up del sistema.
- Mese 2-3: primi 10 signing, richiesta recensioni, follow-up con title companies.

---

## Pricing & offerta

| Tier | Contenuto | Prezzo |
|---|---|---:|
| Core | Sheets + Notion + Quick-Start PDF | **$29–39** |
| Bundle | Core + Launch Checklist + 1 video walkthrough | **$49** |
| Founder (validazione) | Bundle a prezzo lancio | **$19** |

Upsell futuri: mini-corso "tasse per notai", versione "done-for-you" personalizzata, update annuale del tasso IRS.

## Canali
- **Vendita:** Etsy + Gumroad/Payhip (store proprio).
- **Traffico:** gruppi Facebook notai, affiliazioni con creator notary (YouTube/TikTok), Pinterest, SEO (`notary income tracker`, `loan signing agent taxes`).

## Build effort
- Google Sheets: ~2–3 giorni (formule + dashboard).
- Notion: ~1–2 giorni.
- Quick-Start PDF + Canva cover: ~1 giorno.
- **MVP consegnabile in ~1 settimana.**
