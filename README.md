# AnimalHealthDiary 🐾

App diario salute per animali con monitoraggio sintomi, peso e consigli IA.

## Descrizione

AnimalHealthDiary è un'applicazione Python per tenere traccia della salute dei tuoi animali domestici. Lo script raccoglie informazioni sul tuo animale e fornisce consigli personalizzati basati su un sistema di analisi con regole intelligenti.

## Caratteristiche

✅ **Raccolta dati completa**: nome, specie, peso, età, alimentazione e sintomi  
✅ **Analisi intelligente**: valutazione automatica dei dati inseriti  
✅ **Consigli personalizzati**: suggerimenti basati sulla specie, età e condizioni dell'animale  
✅ **Rilevamento sintomi**: identifica sintomi gravi e moderati con avvisi  
✅ **Report dettagliato**: output formattato con tutte le informazioni e raccomandazioni  
✅ **Web App con AI**: interfaccia web moderna con analisi AI tramite ChatGPT (OpenAI)  
✅ **🆕 Notifiche automatiche**: alert per sintomi critici (simulazione email)  
✅ **🆕 Grafici interattivi**: visualizzazione peso e attività con Matplotlib  
✅ **🆕 Upload foto**: possibilità di allegare foto per ogni visita  
✅ **🆕 Export dati**: esportazione storico in formato CSV/JSON  
✅ **🆕 Multilingua**: supporto italiano/inglese selezionabile

## Requisiti

- Python 3.6 o superiore
- Nessuna dipendenza esterna richiesta per script base
- Per la webapp: Flask, OpenAI, Matplotlib, Flask-Babel (vedi `webapp/requirements.txt`)

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/DamianoCeka/AnimalHealthDiary.git
cd AnimalHealthDiary
```

2. Lo script base è pronto all'uso, nessuna installazione aggiuntiva necessaria!

## Come usare

### Script da riga di comando

#### Esecuzione base

Esegui lo script dalla riga di comando:

```bash
python3 animal_diary.py
```

oppure (su Windows):

```bash
python animal_diary.py
```

#### Input richiesti

Lo script ti chiederà di inserire le seguenti informazioni:

1. **Nome animale**: il nome del tuo animale
2. **Specie**: cane, gatto o altro
3. **Peso (kg)**: peso in chilogrammi (numero decimale)
4. **Età (anni)**: età in anni (numero intero)
5. **Alimentazione**: crocchette, umido, mista o casalinga
6. **Sintomi**: sintomi osservati separati da virgola, o "nessuno" se non ci sono sintomi

#### Esempio di utilizzo

```
=== DIARIO SALUTE ANIMALE ===
Inserisci i dati dell'animale:

Nome animale: Luna
Specie (cane/gatto/altro): gatto
Peso (kg): 4.5
Età (anni): 7
Alimentazione (crocchette/umido/mista/casalinga): mista
Sintomi osservati (separati da virgola, o 'nessuno'): nessuno
```

[... rest of existing content ...]

## 🎨 Branding e Asset

Nella directory `branding/` trovi tutti gli asset visivi del progetto:

### Logo Demo
- **File**: `branding/logo_demo.svg`
- **Descrizione**: Logo con zampa e croce della salute, stile moderno tech-friendly
- **Uso**: Header, favicon, materiale promozionale

### Palette Colori
- **File**: `branding/color_palette.txt`
- **Contenuto**: Colori primari (Verde Salute #2ECC71, Blu Tech #3498DB), colori di supporto, gradienti
- **Uso**: Mantenere coerenza visiva nell'interfaccia

### Font Suggeriti
- **File**: `branding/fonts_suggested.txt`
- **Raccomandazioni**:
  - **Headings**: Poppins (Google Fonts)
  - **Body**: Inter (Google Fonts)
  - **Code**: JetBrains Mono
- **Dettagli**: Include dimensioni, line-height, implementazione CSS

### Come Usare gli Asset

1. **Logo**: Incorpora il file SVG nei tuoi template HTML
2. **Colori**: Usa i codici HEX forniti per mantenere coerenza visiva
3. **Font**: Importa da Google Fonts come indicato nel file

## 🌐 Landing Page

Nella directory `landingpage/` trovi una pagina pronta per il deploy:

### File Inclusi
- **index.html**: Landing page completa con tutte le sezioni

### Sezioni Disponibili
1. **Hero**: Titolo principale con CTA
2. **Features**: Grid di funzionalità principali
3. **Demo**: Placeholder per video/GIF dimostrative
4. **FAQ**: Domande frequenti
5. **Contact**: Form e informazioni di contatto
6. **Privacy Policy**: Link alla policy GDPR

### Deploy della Landing Page

**Opzione 1: GitHub Pages**
```bash
# La landing page è già pronta, attiva GitHub Pages:
# Settings > Pages > Source: main branch > /landingpage folder
```

**Opzione 2: Netlify/Vercel**
```bash
# Deploy diretto dalla cartella landingpage/
netlify deploy --dir=landingpage
```

**Opzione 3: Server statico**
```bash
cd landingpage
python -m http.server 8000
# Visita http://localhost:8000
```

### Personalizzazione

- Sostituisci `[Insert your email]` con il tuo indirizzo email
- Aggiungi video/GIF nella sezione demo
- Personalizza i colori utilizzando la palette in `branding/color_palette.txt`

## 📄 Privacy Policy

Il file `PRIVACY_POLICY.txt` contiene un'informativa privacy compliant GDPR che include:

- Raccolta e utilizzo dei dati
- Diritti dell'interessato (accesso, rettifica, cancellazione, portabilità)
- Base giuridica del trattamento
- Informazioni su storage locale e API OpenAI
- Disclaimer medico
- Contatti per esercitare i diritti

**Come usare**: Personalizza le sezioni con [Inserire...] con i tuoi dati di contatto.

## Struttura del codice

### Script base

Il codice è organizzato in una classe `AnimalHealthDiary` con i seguenti metodi:

- `raccolta_dati()`: raccoglie input dall'utente
- `analisi_ia()`: analizza i dati con regole intelligenti
- `genera_report()`: crea e stampa il report finale
- `esegui()`: metodo principale che coordina l'esecuzione

### Web Application

```
webapp/
├── app.py                 # Applicazione Flask principale
├── utils.py              # Utility: grafici, export, foto, notifiche
├── requirements.txt       # Dipendenze Python
├── templates/            # Template HTML
│   ├── index.html       # Form inserimento dati
│   ├── history.html     # Storico visite con grafici
│   └── entry.html       # Dettaglio singola visita
├── translations/         # File traduzione (i18n)
│   ├── it/              # Italiano
│   └── en/              # Inglese
└── data/                # Database locale
    ├── health_history.json  # Storico visite
    └── photos/              # Foto caricate
```

### Moduli utility (utils.py)

**EmailAlert**
- Controllo sintomi critici
- Generazione messaggi di alert
- Simulazione notifiche email

**ChartGenerator**
- Grafici andamento peso
- Grafici distribuzione attività
- Conversione immagini in base64

**DataExporter**
- Export CSV
- Export JSON
- Generazione response Flask

**PhotoManager**
- Validazione upload
- Storage foto
- Gestione nomi file univoci

## Contribuire

Contribuzioni, issue e feature request sono benvenuti! Sentiti libero di aprire una issue o una pull request.

## Licenza

Questo progetto è open source e disponibile per uso personale ed educativo.

## Contatti

Damiano Ceka - [@DamianoCeka](https://github.com/DamianoCeka)

Link progetto: [https://github.com/DamianoCeka/AnimalHealthDiary](https://github.com/DamianoCeka/AnimalHealthDiary)
