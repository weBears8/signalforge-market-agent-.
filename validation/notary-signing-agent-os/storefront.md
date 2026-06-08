# Storefront — Signing Agent HQ (e-commerce live)

Negozio e-commerce costruito su **Lovable** (full-stack: React/TanStack + backend Cloud + Stripe).
Multi-pagina, brandizzato, con checkout per il prodotto a $19 e cattura email per il lead magnet.

## Link
- **Editor (Lovable):** https://lovable.dev/projects/de98e26b-bea0-416d-8080-4e20017fd321
- **Preview live:** https://id-preview--de98e26b-bea0-416d-8080-4e20017fd321.lovable.app
- Progetto: *Signing Agent Suite* · workspace *Stefano's Lovable*

## Pagine
`/` Home · `/product` · `/pricing` · `/free` (lead magnet) · `/faq` · `/about` ·
`/contact` · `/terms` · `/privacy` · `/refunds` · `/success` · `/cancel`.
Brand: navy #1F2A44 · teal #1F7A8C · gold #E0A458 · green #3FA45B.

## Commerce
- **Checkout Stripe** per "Signing Agent HQ" a **$19** (founder). I bottoni "Buy — $19" creano una sessione di checkout → `/success` (o `/cancel`).
- **Backend (Lovable Cloud):** tabella `leads` (email, biggest_headache, source, created_at) per gli opt-in del mileage log gratuito + `messages` per il form contatti.

## Per andare in produzione (owner) — 4 passi
1. **Collega Stripe:** nell'editor Lovable, apri l'integrazione Stripe e collega il tuo account (chiavi live). Verifica che il prezzo del prodotto sia $19.
2. **Carica i file reali del prodotto:** sostituisci i link "Download" placeholder (in `/success` e nello stato di successo di `/free`) con i file in `dist/`:
   - Prodotto a pagamento → `dist/Signing-Agent-HQ.xlsx`, `dist/notion/`, `dist/Quick-Start-Guide.pdf`, `dist/bundle/First-90-Days-Launch-Checklist.pdf` (zippa e carica su storage/Drive, poi incolla il link).
   - Lead magnet gratuito → `dist/lead-magnet/Notary-Mileage-Log.xlsx` + `…-printable.pdf`.
   - Consegna consigliata: email automatica post-acquisto/opt-in (connettore **Resend**/**Brevo** disponibili in Lovable) con il link al file.
3. **Pubblica:** in Lovable premi *Publish* → ottieni un dominio `*.lovable.app`. Collega un **dominio custom** se vuoi (es. `signingagenthq.com`).
4. **Collega il funnel:** punta i bottoni "Pre-order/Buy" degli asset (ad, email, landing statica in `dist/landing/`) all'URL pubblicato, e il "free log" a `/free`.

## Nota
La landing statica in `dist/landing/` resta utile come pagina singola alternativa / per A/B test; lo store Lovable è la vetrina completa con checkout reale.
