# Landing page — Signing Agent HQ

Landing statica, self-contained, pronta al deploy per la **fase di validazione**
(raccolta email del lead magnet + preordine a $19). Copy in inglese (mercato USA),
basata su [`../../validation/notary-signing-agent-os/landing-page.md`](../../validation/notary-signing-agent-os/landing-page.md).

## File
- `index.html` — pagina completa, CSS inline, zero dipendenze.
- `assets/hero.png` — screenshot prodotto nella hero.
- `assets/cover.png` — immagine social (`og:image`).

## Deploy (scegline uno)
- **Netlify Drop** — trascina la cartella `landing/` su https://app.netlify.com/drop. Online in ~30s.
- **Vercel** — `vercel deploy` dentro `dist/landing/` (o importa da GitHub puntando a questa dir).
- **GitHub Pages** — pubblica `dist/landing/` come root del sito.
- **Carrd/Gumroad** — usa `index.html` come riferimento per ricostruire il layout.

## Prima di pubblicare (2 cose obbligatorie)
1. **Collega il form.** In `index.html` sostituisci l'`action`:
   ```html
   <form action="https://formspree.io/f/your-form-id" method="POST">
   ```
   con il tuo endpoint reale (Formspree, ConvertKit, MailerLite, Beehiiv…).
   Il form invia `email` + `biggest_headache` (domanda qualitativa per il customer language).
   È già presente un honeypot anti-spam (`_gotcha`).
2. **Collega i pulsanti "Pre-order — $19"** alla tua pagina di checkout
   (Gumroad/Payhip) sostituendo gli `href="#offer"` del bottone d'acquisto finale.

## Note
- Responsive (breakpoint a 820px), accessibile, no tracker di terze parti.
- L'anno nel footer si aggiorna da solo.
- Rigenera gli asset con [`../../build/build_cover.py`](../../build/build_cover.py) se cambi il brand.
