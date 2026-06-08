# Go-Live Runbook — Signing Agent HQ

Da kit a **online in ~1 giornata**, a costo zero. Segui in ordine.
Spunta ogni passo. Tutto in inglese lato cliente; note operative in italiano.

> Obiettivo della fase: **lista email + ≥ 5 preordini a $19** prima di rifinire il prodotto
> (vedi [`validation-plan.md`](./validation-plan.md)). Non serve nulla di perfetto, serve *live*.

---

## 0 · Prerequisiti (10 min)
- [ ] Crea un account **Gumroad** (gratis) — hosting prodotto + checkout + consegna file.
- [ ] Crea un account **Formspree** (free tier) *oppure* usa il form nativo di Gumroad per le email.
- [ ] Crea un account **Netlify** (gratis) per la landing.
- [ ] Tieni a portata i file in `dist/`: `Signing-Agent-HQ.xlsx`, `notion/`, `Quick-Start-Guide.pdf`, `bundle/`, `lead-magnet/`.

---

## 1 · Prodotto gratuito = lead magnet (15 min)
Su Gumroad: **Products → New product → "Call to action: I want this!"**, prezzo **$0** (o "pay what you want", minimo 0).
- [ ] Nome: **The Notary Mileage Log (Free)**
- [ ] Carica: `dist/lead-magnet/Notary-Mileage-Log.xlsx` + `Notary-Mileage-Log-printable.pdf`
- [ ] Descrizione: prendi la promessa dal [lead magnet](./lead-magnet-mileage-log.md).
- [ ] Cover: `dist/marketing/ads/ad-pin-1000x1500.png` (o `cover-2000.png`).
- [ ] In **Content/Receipt**: aggiungi un link "Upgrade to the full system → $19" che punta al prodotto a pagamento (passo 2).
- [ ] **Gumroad raccoglie l'email automaticamente** all'acquisto gratuito → è la tua lista.

> Alternativa form sulla landing: vedi passo 4.

## 2 · Prodotto a pagamento = $19 founder (20 min)
**New product → prezzo $19.**
- [ ] Nome: **Signing Agent HQ — Complete Notary Business & Tax System**
- [ ] Descrizione: incolla [`sales-listing.md`](./sales-listing.md).
- [ ] Carica (tutti):
  - `dist/Signing-Agent-HQ.xlsx`
  - `dist/notion/` (zippa la cartella: i 4 CSV + `_README.md`)
  - `dist/Quick-Start-Guide.pdf`
  - `dist/bundle/First-90-Days-Launch-Checklist.pdf`
- [ ] Cover: `dist/marketing/cover-2000.png`. Aggiungi `hero-1600x900.png` nella galleria.
- [ ] **Quantità limitata / scarsità onesta:** scrivi "Founder price for the first 30" in descrizione (Gumroad non ha countdown nativo affidabile — gestiscilo a mano alzando il prezzo a $34 dopo 30).
- [ ] Copia l'URL del prodotto → ti serve per i bottoni della landing (passo 4) e per la email 4.

## 3 · Deploy della landing (10 min)
- [ ] Vai su https://app.netlify.com/drop e **trascina la cartella `dist/landing/`**.
- [ ] Netlify ti dà un URL (es. `random-name.netlify.app`). Funziona già.
- [ ] (Opzionale) Rinomina il sito o collega un dominio.

## 4 · Cabla la landing (15 min)
Apri `dist/landing/index.html` e sostituisci **2 cose**, poi ri-trascina su Netlify Drop:
- [ ] **Form email:** cambia
  `action="https://formspree.io/f/your-form-id"`
  con il tuo endpoint Formspree reale (Forms → New form → copia l'ID).
  *Oppure* sostituisci tutto il form con il bottone "Get the free Mileage Log" che linka al prodotto gratuito Gumroad del passo 1.
- [ ] **Bottoni "Pre-order — $19":** cambia gli `href="#offer"` del bottone d'acquisto con l'URL del prodotto a pagamento (passo 2). Sono 3 punti: header, sezione OFFER, FINAL CTA.

## 5 · Test del funnel end-to-end (10 min)
- [ ] Apri la landing in incognito. Invia il form con una tua email → ricevi il mileage log?
- [ ] Clicca "Pre-order $19" → arrivi al checkout Gumroad corretto?
- [ ] Fai un acquisto di test del prodotto gratuito → ricevi i file + l'upsell?
- [ ] Controlla la landing su **mobile** (la maggior parte del traffico notai è mobile).

## 6 · Accendi il traffico (giorno 1 → vedi calendario)
- [ ] Posta `ad-square-1080.png` in 3–5 **gruppi Facebook per notai** come valore gratuito ("comment MILE"). *Non* come ad — gli admin bannano la vendita.
- [ ] Pubblica `ad-pin-1000x1500.png` su **Pinterest** con la caption pronta.
- [ ] Gira il [video 60s](./video-script-60s.md) e pubblicalo su TikTok/Reels con `ad-story-1080x1920.png` come cover.
- [ ] Ogni nuova email → parte la [sequenza](./email-sequence.md).

---

## Costi
Tutto **$0** fino alla prima vendita (Gumroad trattiene una fee per transazione; Netlify/Formspree/Pinterest free tier bastano per la validazione).

## Definizione di "fatto" per oggi
Landing live + 2 prodotti Gumroad + funnel testato + primo post nei gruppi. Da qui in poi è **traffico e misura** (→ [`launch-calendar.md`](./launch-calendar.md)).
