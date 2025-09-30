# Animal Health Diary - Versione AI 🤖🐾

## Panoramica

Questa è la versione avanzata di Animal Health Diary che integra l'**API OpenAI (ChatGPT)** per fornire analisi intelligenti e personalizzate sulla salute dei tuoi animali domestici. A differenza della versione base che utilizza regole predefinite, questa versione sfrutta la potenza dell'intelligenza artificiale per offrire consigli più dettagliati e contestualizzati.

## 🆚 Differenze tra Versioni

### Versione Base (`animal_diary.py`)
- ✅ Gratuita, nessun costo
- ✅ Funziona offline
- ✅ Analisi basata su regole predefinite
- ❌ Consigli limitati e generici
- ❌ Non adatta a situazioni complesse

### Versione AI (`animal_diary_api.py`) 🌟
- ✅ Analisi intelligente avanzata con GPT-4
- ✅ Consigli personalizzati e dettagliati
- ✅ Comprensione del contesto complesso
- ✅ Risposte in linguaggio naturale
- ✅ Salvataggio automatico delle analisi in JSON
- ⚠️ Richiede API Key OpenAI (costi minimi)
- ⚠️ Richiede connessione internet

## 📋 Requisiti

### Software
- Python 3.7 o superiore
- Libreria `openai` (versione 1.0+)

### API Key OpenAI
- Account OpenAI (gratuito per iniziare)
- API Key attiva
- Crediti API (circa $0.001-0.01 per analisi con gpt-4o-mini)

## 🚀 Installazione

### 1. Clona il repository
```bash
git clone https://github.com/DamianoCeka/AnimalHealthDiary.git
cd AnimalHealthDiary
```

### 2. Installa le dipendenze
```bash
pip install openai
```

Oppure con un virtual environment (consigliato):
```bash
python3 -m venv venv
source venv/bin/activate  # Su Linux/Mac
venv\Scripts\activate     # Su Windows

pip install openai
```

### 3. Ottieni una API Key OpenAI

1. Vai su [platform.openai.com](https://platform.openai.com/)
2. Crea un account o accedi
3. Naviga in **API Keys** nel menu utente
4. Clicca su **"Create new secret key"**
5. Copia la chiave (inizia con `sk-...`)
6. **IMPORTANTE**: Salva la chiave in un posto sicuro! Non la vedrai più dopo la creazione

### 4. Configura la API Key

#### Opzione A: Variabile d'ambiente (consigliata)

**Linux/Mac:**
```bash
export OPENAI_API_KEY='sk-la-tua-chiave-qui'
```

Per renderla permanente, aggiungi la riga sopra al file `~/.bashrc` o `~/.zshrc`:
```bash
echo "export OPENAI_API_KEY='sk-la-tua-chiave-qui'" >> ~/.bashrc
source ~/.bashrc
```

**Windows (CMD):**
```cmd
set OPENAI_API_KEY=sk-la-tua-chiave-qui
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY='sk-la-tua-chiave-qui'
```

Per renderla permanente su Windows:
1. Cerca "Variabili d'ambiente" nel menu Start
2. Aggiungi una nuova variabile utente:
   - Nome: `OPENAI_API_KEY`
   - Valore: `sk-la-tua-chiave-qui`

#### Opzione B: Passare la chiave direttamente al codice

Modifica lo script per passare la chiave al costruttore:
```python
diario = AnimalHealthDiaryAPI(api_key="sk-la-tua-chiave-qui")
```

⚠️ **ATTENZIONE**: Non condividere mai la tua API Key e non caricarla su repository pubblici!

## 🧪 Test della Connessione

Prima di usare l'applicazione completa, testa la connessione all'API:

```bash
python3 animal_diary_api.py --test
```

Output atteso:
```
=== TEST CONNESSIONE API OpenAI ===
✅ Connessione API riuscita!
   Modello: gpt-4o-mini
```

Se ricevi un errore, verifica:
- La API Key è corretta e attiva
- Hai crediti disponibili nel tuo account OpenAI
- La connessione internet funziona

## 📖 Come Usare

### Esecuzione Standard
```bash
python3 animal_diary_api.py
```

### Esempio di Sessione Completa

```
=== DIARIO SALUTE ANIMALE - AI VERSION ===
Inserisci i dati dell'animale:

Nome animale: Max
Specie (cane/gatto/altro): cane
Peso (kg): 28.5
Età (anni): 8
Alimentazione (crocchette/umido/mista/casalinga): crocchette
Livello di attività (basso/medio/alto): medio
Sintomi osservati (descrizione dettagliata o 'nessuno'): sembra un po' stanco ultimamente, dorme più del solito
Note aggiuntive (opzionale): ha iniziato a bere più acqua del normale

🤖 Analisi AI in corso...

==================================================================
         REPORT SALUTE ANIMALE - ANALISI AI
==================================================================

Data: 2025-09-30 11:15

📋 DATI ANIMALE:
  Nome: Max
  Specie: Cane
  Peso: 28.5 kg
  Età: 8 anni
  Alimentazione: Crocchette
  Attività: Medio
  Sintomi: sembra un po' stanco ultimamente, dorme più del solito
  Note: ha iniziato a bere più acqua del normale

🤖 ANALISI INTELLIGENTE AI:
----------------------------------------------------------------------
### Valutazione Stato di Salute Generale

Max è un cane di 8 anni, quindi sta entrando nella fase senior...
[L'AI fornirà un'analisi dettagliata e personalizzata]
----------------------------------------------------------------------

✅ Entry salvata in: health_diary_Max_20250930_111530.json
```

## 🔧 Funzionalità Avanzate

### Salvataggio Automatico

Ogni analisi viene salvata automaticamente in un file JSON con formato:
```
health_diary_[NOME]_[DATA]_[ORA].json
```

Esempio di contenuto:
```json
{
  "dati": {
    "nome": "Max",
    "specie": "cane",
    "peso": 28.5,
    "eta": 8,
    ...
  },
  "analisi_ai": "[Risposta completa dell'AI]",
  "timestamp": "2025-09-30T11:15:30.123456"
}
```

### Personalizzazione del Modello

Puoi modificare il modello AI nel codice:

```python
# Nel costruttore della classe AnimalHealthDiaryAPI
self.model = "gpt-4o-mini"  # Economico e veloce
# self.model = "gpt-4o"      # Più potente ma più costoso
```

## 💰 Costi Stimati

Con il modello `gpt-4o-mini` (default):
- Costo per analisi: **~$0.001 - $0.01**
- 100 analisi: **~$0.10 - $1.00**
- Ideale per uso personale

Con il modello `gpt-4o`:
- Costo per analisi: **~$0.01 - $0.05**
- Maggiore qualità e dettaglio
- Consigliato per casi complessi

Verifica i prezzi aggiornati su [openai.com/pricing](https://openai.com/pricing)

## 🛡️ Sicurezza e Privacy

### Best Practices
- ✅ Non condividere mai la tua API Key
- ✅ Usa variabili d'ambiente, non hardcode la chiave
- ✅ Aggiungi `.env` al `.gitignore` se usi file di configurazione
- ✅ Monitora l'uso della tua API Key sul dashboard OpenAI
- ✅ Imposta limiti di spesa sul tuo account OpenAI

### Privacy dei Dati
- I dati inviati all'API OpenAI sono soggetti alla loro [Privacy Policy](https://openai.com/policies/privacy-policy)
- OpenAI non usa i dati delle API per training (per API standard)
- I file JSON salvati localmente contengono dati sensibili - proteggili adeguatamente

## 🐛 Risoluzione Problemi

### Errore: "API Key mancante"
**Soluzione**: Verifica che la variabile d'ambiente sia impostata correttamente:
```bash
echo $OPENAI_API_KEY  # Linux/Mac
echo %OPENAI_API_KEY% # Windows CMD
```

### Errore: "Incorrect API key provided"
**Soluzione**: La chiave è sbagliata o non valida. Genera una nuova chiave su platform.openai.com

### Errore: "You exceeded your current quota"
**Soluzione**: Hai esaurito i crediti. Aggiungi crediti al tuo account OpenAI.

### Errore: "Connection error"
**Soluzione**: Verifica la connessione internet o controlla lo stato dei servizi OpenAI su [status.openai.com](https://status.openai.com)

## 📚 Codice di Esempio

### Uso Programmatico

```python
from animal_diary_api import AnimalHealthDiaryAPI

# Inizializza con API key
diario = AnimalHealthDiaryAPI(api_key="sk-...")

# Crea dati manualmente
dati_test = {
    'nome': 'Luna',
    'specie': 'gatto',
    'peso': 4.2,
    'eta': 5,
    'alimentazione': 'umido',
    'attivita': 'alto',
    'sintomi': 'nessuno',
    'note': 'gatto molto attivo',
    'data': '2025-09-30 11:00'
}

# Ottieni analisi AI
risposta = diario.analisi_ai(dati_test)
print(risposta)

# Genera report
diario.genera_report(dati_test, risposta)
```

## 🔄 Integrazione con la Versione Base

Entrambe le versioni possono coesistere:

```bash
# Usa la versione base (offline, gratuita)
python3 animal_diary.py

# Usa la versione AI (online, con API)
python3 animal_diary_api.py
```

## 📄 Licenza e Disclaimer

⚠️ **DISCLAIMER MEDICO IMPORTANTE**:

Questa applicazione fornisce **consigli informativi generali** e **NON sostituisce** in alcun modo una visita veterinaria professionale. 

- ❌ Non usare per diagnosi mediche
- ❌ Non ritardare cure veterinarie basandosi su questa app
- ✅ Usa come strumento di monitoraggio supplementare
- ✅ Consulta sempre un veterinario per problemi di salute

L'AI può commettere errori - verifica sempre le informazioni con un professionista.

## 🤝 Contribuire

Contributi, suggerimenti e segnalazioni di bug sono benvenuti!

## 📞 Supporto

Per domande o problemi:
- Apri una issue su GitHub
- Contatta [@DamianoCeka](https://github.com/DamianoCeka)

## 🔗 Link Utili

- [Documentazione OpenAI API](https://platform.openai.com/docs)
- [OpenAI Pricing](https://openai.com/pricing)
- [OpenAI Status](https://status.openai.com)
- [Repository del Progetto](https://github.com/DamianoCeka/AnimalHealthDiary)

---

**Versione**: 1.0.0  
**Ultimo aggiornamento**: Settembre 2025  
**Autore**: Damiano Ceka
