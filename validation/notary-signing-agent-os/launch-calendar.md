# Launch Calendar — 14 giorni (validazione)

Calendario operativo che mappa gli asset pronti (3 ad, video, 5 email, lead magnet)
ai giorni, agganciato alle soglie Go/No-Go del [`validation-plan.md`](./validation-plan.md).
Setup tecnico in [`go-live-runbook.md`](./go-live-runbook.md).

**Cadenza:** ~20–30 min/giorno. Tutto organico (ads a pagamento facoltativi, giorni 8–14).

---

## Settimana 1 — Segnale di interesse (far crescere la lista)

| Giorno | Azione | Asset | Obiettivo |
|---|---|---|---|
| **1** | Go-live: landing + 2 prodotti Gumroad + funnel testato. Primo post in 2 gruppi FB notai (comment-to-get). | runbook · `ads/ad-square-1080.png` | funnel attivo |
| **2** | 2 pin Pinterest verso il lead magnet. Post in altri 2 gruppi FB. | `ads/ad-pin-1000x1500.png` | reach |
| **3** | Gira e pubblica il video 60s su TikTok/Reels. Cover = story ad. | `video-script-60s.md` · `ads/ad-story-1080x1920.png` | top-of-funnel video |
| **4** | 1 post su r/Notary (valore, no spam) + risposta ai commenti dei giorni 1–3. | — | conversazioni |
| **5** | 3 pin Pinterest aggiuntivi (varianti). Reposta lo square in 1–2 nuovi gruppi. | `ads/` | volume pin |
| **6** | Engagement: rispondi a *ogni* commento/DM, manda il log, annota il linguaggio del cliente. | — | qualitative |
| **7** | **Checkpoint W1.** Misura: click landing, opt-in %, risposte. | — | GO/NO-GO #1 |

**Soglia fine giorno 7 (GO):** click landing ≥ 50 · opt-in ≥ 20% · risposte qualitative ≥ 8.
La sequenza email parte in automatico a ogni nuovo opt-in (E1 subito → E2/E3 nei giorni successivi).

## Settimana 2 — Prova di pagamento (preordini)

| Giorno | Azione | Asset | Obiettivo |
|---|---|---|---|
| **8** | Invia **Email 4 (offerta $19)** a tutta la waitlist. Apri ufficialmente il preordine. | `email-sequence.md` → E4 | prime vendite |
| **9** | Story/Reel "founder price is live, first 30". Ripeti il video con nuovo hook (variante B). | `ads/ad-story` · `video-script` hook #2 | spinta |
| **10** | (Opz.) Micro-test ads $30–50 verso il **lead magnet** (non la vendita): Pinterest o FB. | `ads/` | traffico pagato |
| **11** | Posta una "behind the scenes" del dashboard nei gruppi (valore, mostra il prodotto). | `cover-2000.png` / screenshot | fiducia |
| **12** | Follow-up 1:1 a chi ha risposto "quanto costa?" in W1. Offerta diretta. | — | conversione calda |
| **13** | **Email 5 (chiusura founder price stasera)** alla waitlist. | `email-sequence.md` → E5 | urgency |
| **14** | **Checkpoint W2 — decisione.** Conta i preordini a $19. | — | **GO/NO-GO finale** |

**Soglia fine giorno 14 (la più importante):**
- **Preordini a $19 ≥ 5 → GO:** costruisci/rifinisci e consegna (il MVP in `dist/` è già pronto → consegna *subito*).
- Waitlist ≥ 20 ma preordini < 5 → **riposiziona** (wedge stretto "Notary Tax & Mileage Kit" a $12–15) prima di scartare.

---

## Tracking (tieni un foglio semplice)
| Metrica | Dove leggerla | Soglia GO |
|---|---|---:|
| Click landing | Netlify Analytics / bit.ly | ≥ 50 |
| Opt-in lead magnet | Gumroad (vendite gratuite) / Formspree | ≥ 20% |
| Email / waitlist | Gumroad / Formspree | ≥ 20 |
| **Preordini $19** | Gumroad | **≥ 5** |
| Risposte qualitative | DM / commenti | ≥ 8 |

## Regole d'oro
- **Valore prima della vendita.** Nei gruppi sei un collega che regala un tool, non un venditore.
- **Salva il linguaggio del cliente.** Ogni "il mio problema è…" diventa copy migliore (email, landing, listing).
- **Consegna già pronta.** A differenza del piano "vendi la promessa", qui il prodotto MVP esiste già in `dist/`: i primi preordini ricevono il sistema completo *subito* → testimonianze più veloci.
