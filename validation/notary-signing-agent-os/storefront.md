# Storefront — Signing Agent HQ (e-commerce live)

Negozio e-commerce costruito su **Lovable** (full-stack: React/TanStack + backend Cloud + Stripe).
Multi-pagina, brandizzato, con checkout per il prodotto a $19 e cattura email per il lead magnet.

## Link
- **Sito pubblicato (live):** https://signing-agent-hq.lovable.app
- **Editor (Lovable):** https://lovable.dev/projects/de98e26b-bea0-416d-8080-4e20017fd321
- **Preview:** https://preview--signing-agent-hq.lovable.app
- Progetto: *Signing Agent Suite* · workspace *Stefano's Lovable*

## Pagine (13 rotte, confermate)
`/` Home · `/product` · `/pricing` · `/free` (lead magnet) · `/faq` · `/about` ·
`/contact` · `/terms` · `/privacy` · `/refunds` · `/checkout` · `/success` · `/cancel`.
Brand: navy #1F2A44 · teal #1F7A8C · gold #E0A458 · green #3FA45B.

## Commerce (cablato)
- **Checkout Stripe** per "Signing Agent HQ" a **$19** one-time: `/checkout` → `createCheckoutSession` → Stripe → `/success` (o `/cancel`). Se `STRIPE_SECRET_KEY` non è impostata, fa fallback demo a `/success?demo=1` così il flusso è testabile end-to-end.
- **Backend (Lovable Cloud / Supabase):** tabella `leads` (email, biggest_headache, source, created_at) per gli opt-in del mileage log + `contact_messages` (name, email, message, created_at). RLS + insert anonimo, validazione Zod, toast.

## Per andare in produzione (owner) — 4 passi
1. **Collega Stripe (incassi reali):** nell'editor Lovable aggiungi il secret `STRIPE_SECRET_KEY` (Stripe Dashboard → Developers → API keys). Nessuna modifica al codice: il checkout passa da demo a pagamenti reali. Verifica che il prezzo sia $19.
2. **Carica i file reali del prodotto:** sostituisci i link "Download" placeholder (in `/success` e nello stato di successo di `/free`) con i file in `dist/`:
   - Prodotto a pagamento → `dist/Signing-Agent-HQ.xlsx`, `dist/notion/`, `dist/Quick-Start-Guide.pdf`, `dist/bundle/First-90-Days-Launch-Checklist.pdf` (zippa e carica su storage/Drive, poi incolla il link).
   - Lead magnet gratuito → `dist/lead-magnet/Notary-Mileage-Log.xlsx` + `…-printable.pdf`.
   - Consegna consigliata: email automatica post-acquisto/opt-in (connettore **Resend**/**Brevo** disponibili in Lovable) con il link al file.
3. **Pubblica:** in Lovable premi *Publish* → ottieni un dominio `*.lovable.app`. Collega un **dominio custom** se vuoi (es. `signingagenthq.com`).
4. **Collega il funnel:** punta i bottoni "Pre-order/Buy" degli asset (ad, email, landing statica in `dist/landing/`) all'URL pubblicato, e il "free log" a `/free`.

## Screenshot di prodotto (gallery)
Le 3 immagini reali in `dist/marketing/screenshots/` (Dashboard, Signing Log, Tax Summary, generate da `build/build_screenshots.py` con i numeri del trimestre) sono nella gallery di `/product` con lightbox, e la Dashboard apre la sezione "See inside" della home.

## Consegna file (download)
File serviti dallo store (sorgenti in `dist/delivery/`):
- **Gratis** (`/free`, dopo opt-in): `Notary-Mileage-Log.xlsx` + link al PDF stampabile.
- **A pagamento** (`/success`, dopo checkout): `Signing-Agent-HQ.zip` (workbook + Notion + Quick-Start + checklist).
- ⚠️ **Upgrade sicurezza:** il file a pagamento è servito come URL pubblico (ok per soft-launch ma indovinabile). Per la vendita seria → consegna via **email gated** (connettore Resend) dopo pagamento Stripe confermato.

## Brand
Azienda/venditore: **DigitaLAB Vision** (footer "© 2026 DigitaLAB Vision", meta/OG, pagine legali, About). Prodotto: **Signing Agent HQ** (nome prodotto invariato, logo nav invariato).
Dominio consigliato: **digitalabvision.com** ($11,25/anno) → da collegare in Lovable *Settings → Domains* con i record DNS forniti (richiede piano a pagamento Lovable).

## Nota
La landing statica in `dist/landing/` resta utile come pagina singola alternativa / per A/B test; lo store Lovable è la vetrina completa con checkout reale.
