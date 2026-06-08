# dist/ — deliverable pronti all'uso

Tutto ciò che serve per **lanciare** Signing Agent HQ. Generato dagli script in
[`../build/`](../build/) — rigenera tutto con `python3 build/build_all.py`.
Guida operativa al lancio: [`../validation/notary-signing-agent-os/go-live-runbook.md`](../validation/notary-signing-agent-os/go-live-runbook.md).

## Mappa per stadio del funnel

### 🎣 Top-of-funnel (gratis → email)
| File | Uso |
|---|---|
| `lead-magnet/Notary-Mileage-Log.xlsx` | Lead magnet con formule live — il regalo che cattura l'email. |
| `lead-magnet/Notary-Mileage-Log-printable.pdf` | Versione stampabile per l'auto. |
| `marketing/ads/ad-square-1080.png` | Ad gruppi/feed Facebook. |
| `marketing/ads/ad-pin-1000x1500.png` | Pin Pinterest. |
| `marketing/ads/ad-story-1080x1920.png` | Cover Story/Reel. |
| `marketing/ads/README.md` | Caption pronte + note per canale. |

### 🛬 Conversione (landing → preordine)
| File | Uso |
|---|---|
| `landing/index.html` | Landing deployabile (self-contained). |
| `landing/README.md` | Istruzioni di deploy + cablaggio form/checkout. |
| `marketing/cover-2000.png` | Cover quadrata (Etsy/social/listing). |
| `marketing/hero-1600x900.png` | Hero wide (Gumroad/landing). |

### 📦 Il prodotto (cosa riceve chi compra a $19)
| File | Uso |
|---|---|
| `Signing-Agent-HQ.xlsx` | **Il sistema completo**: 9 fogli, formule live, Schedule C. Importabile in Google Sheets/Excel. |
| `notion/*.csv` + `notion/_README.md` | Versione Notion + guida di setup completa. |
| `Quick-Start-Guide.pdf` | Onboarding 5 pagine. |
| `bundle/First-90-Days-Launch-Checklist.pdf` | Bonus bundle per il nuovo agente. |

### 📊 Operatività (tu, venditore)
| File | Uso |
|---|---|
| `Validation-Tracker.xlsx` | Registra le metriche vs soglie Go/No-Go — verdetto automatico. |

## Integrità
Il prodotto è verificato da `build/verify_workbook.py` (ricalcolo indipendente:
fees $425 · net $299.90 · miglia 42 · deduzione $29.40 · 9 fogli · 0 errori).

## Licenza / disclaimer
Single-user license, non ridistribuire. I sistemi sono *organizer*, non consulenza
fiscale o legale — conferma il tasso IRS corrente e le deduzioni con un professionista.
