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

#### Output del report

Lo script genera un report dettagliato con:

- 📋 **Dati animale**: riepilogo delle informazioni inserite
- 🚨 **Avvisi importanti**: eventuali sintomi gravi che richiedono attenzione veterinaria
- 💡 **Consigli**: suggerimenti personalizzati basati su età, peso, specie e alimentazione

### 🌐 Web Application

La webapp offre un'interfaccia moderna e user-friendly con analisi AI tramite ChatGPT!

#### Installazione webapp

1. Naviga nella directory webapp:

```bash
cd webapp
```

2. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

3. Configura la tua chiave API OpenAI:

```bash
# Linux/Mac
export OPENAI_API_KEY='sk-your-api-key-here'

# Windows
set OPENAI_API_KEY=sk-your-api-key-here
```

#### Avvio della webapp

Esegui l'applicazione Flask:

```bash
python app.py
```

L'applicazione sarà disponibile su: http://127.0.0.1:5000

#### Funzionalità della webapp

**✨ Interfaccia Web Moderna**
- Form interattivo per inserimento dati
- Design responsive e user-friendly
- Validazione in tempo reale

**🤖 Analisi AI con ChatGPT**
- Analisi intelligente dei dati dell'animale
- Consigli personalizzati basati su AI
- Valutazioni professionali sulla salute

**📊 Storico Visite**
- Visualizzazione di tutte le analisi precedenti
- Ricerca e filtro delle visite
- Export dei dati in CSV/JSON

**💾 Persistenza Dati**
- Salvataggio automatico di ogni analisi
- Database locale in formato JSON
- Facile consultazione dello storico

### 🆕 Nuove Funzionalità Avanzate

#### 🚨 Sistema di Notifiche Automatiche

Quando vengono rilevati **sintomi critici**, il sistema genera automaticamente un alert:

- **Sintomi monitorati**: vomito, diarrea, sangue, letargia, febbre, convulsioni, difficoltà respiratorie
- **Alert immediato**: notifica visibile nell'interfaccia
- **Simulazione email**: log dell'alert con timestamp e dettagli
- **Raccomandazione**: invito urgente a consultare un veterinario

**Come funziona:**
- Il sistema analizza i sintomi inseriti
- Se rileva parole chiave critiche, genera un messaggio di allerta
- L'alert viene mostrato in modo prominente nella pagina dei risultati
- Viene salvato nello storico per riferimento futuro

#### 📈 Grafici e Visualizzazioni

La webapp ora genera automaticamente **grafici interattivi** usando Matplotlib:

**1. Grafico Andamento Peso**
- Visualizza l'evoluzione del peso nel tempo
- Disponibile nella sezione Storico
- Filtro per singolo animale
- Formato PNG incorporato nella pagina

**2. Grafico Distribuzione Attività**
- Mostra la frequenza dei diversi livelli di attività registrati
- Utile per monitorare i cambiamenti comportamentali
- Rappresentazione a barre colorata

**Come accedere:**
- Vai alla pagina "Storico Visite"
- Seleziona un animale dal menu (opzionale)
- I grafici vengono generati automaticamente se ci sono dati sufficienti

#### 📸 Gestione Foto

È ora possibile **allegare foto** a ogni visita:

**Formati supportati:**
- PNG, JPG, JPEG, GIF
- Dimensione massima consigliata: 5MB

**Funzionalità:**
- Upload durante la registrazione di una nuova visita
- Anteprima dell'immagine caricata
- Storage locale in `webapp/data/photos/`
- Visualizzazione nella pagina di dettaglio della visita

**Come usare:**
1. Nel form di inserimento dati, clicca su "Allega Foto"
2. Seleziona un'immagine dal tuo dispositivo
3. L'immagine verrà salvata con un nome unico
4. Visualizza la foto nella cronologia delle visite

#### 💾 Esportazione Dati

Ora puoi **esportare tutto lo storico** in due formati:

**1. Formato CSV**
- Compatibile con Excel, Google Sheets
- Colonne: ID, Data, Nome, Specie, Peso, Età, Alimentazione, Attività, Sintomi, Note
- Ideale per analisi e grafici personalizzati

**2. Formato JSON**
- Include tutti i dati inclusa l'analisi AI
- Formato strutturato per elaborazioni avanzate
- Backup completo del database

**Come esportare:**
- Nella pagina "Storico Visite", clicca su "Esporta Dati"
- Scegli il formato (CSV o JSON)
- Il file viene scaricato automaticamente
- Nome file: `animal_health_history.csv` o `animal_health_history.json`

#### 🌍 Supporto Multilingua

L'applicazione supporta **italiano e inglese**:

**Funzionalità:**
- Cambio lingua in tempo reale
- Interfaccia completamente tradotta
- Persistenza della preferenza lingua
- Supporto UTF-8 per caratteri speciali

**Come cambiare lingua:**
1. Clicca sull'icona della lingua nell'header (🇮🇹/🇬🇧)
2. Seleziona la lingua desiderata
3. L'interfaccia si aggiorna istantaneamente
4. La preferenza viene salvata per le visite future

**Lingue disponibili:**
- 🇮🇹 Italiano (predefinito)
- 🇬🇧 English

## Funzionalità di analisi

### Analisi del peso

- Valutazione basata sulla specie (cane/gatto)
- Identificazione di possibile sottopeso o sovrappeso

### Analisi dell'età

- Consigli specifici per cuccioli (< 1 anno)
- Raccomandazioni per animali anziani (> 10 anni)

### Analisi dei sintomi

- **Sintomi gravi**: vomito, diarrea, sangue, letargia, febbre, convulsioni → richiesta consulto veterinario urgente
- **Sintomi moderati**: tosse, starnuti, prurito, perdita appetito, sete eccessiva → monitoraggio consigliato

## Note importanti

⚠️ **Disclaimer**: I consigli forniti da questa applicazione sono indicativi e basati su regole generali. Per diagnosi precise e cure appropriate, consultare sempre un veterinario professionista.

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
