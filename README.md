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

## Requisiti

- Python 3.6 o superiore
- Nessuna dipendenza esterna richiesta (utilizza solo librerie standard)

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/DamianoCeka/AnimalHealthDiary.git
cd AnimalHealthDiary
```

2. Lo script è pronto all'uso, nessuna installazione aggiuntiva necessaria!

## Come usare

### Esecuzione base

Esegui lo script dalla riga di comando:

```bash
python3 animal_diary.py
```

oppure (su Windows):

```bash
python animal_diary.py
```

### Input richiesti

Lo script ti chiederà di inserire le seguenti informazioni:

1. **Nome animale**: il nome del tuo animale
2. **Specie**: cane, gatto o altro
3. **Peso (kg)**: peso in chilogrammi (numero decimale)
4. **Età (anni)**: età in anni (numero intero)
5. **Alimentazione**: crocchette, umido, mista o casalinga
6. **Sintomi**: sintomi osservati separati da virgola, o "nessuno" se non ci sono sintomi

### Esempio di utilizzo

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

### Output del report

Lo script genera un report dettagliato con:

- 📋 **Dati animale**: riepilogo delle informazioni inserite
- 🚨 **Avvisi importanti**: eventuali sintomi gravi che richiedono attenzione veterinaria
- 💡 **Consigli**: suggerimenti personalizzati basati su età, peso, specie e alimentazione

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

Il codice è organizzato in una classe `AnimalHealthDiary` con i seguenti metodi:

- `raccolta_dati()`: raccoglie input dall'utente
- `analisi_ia()`: analizza i dati con regole intelligenti
- `genera_report()`: crea e stampa il report finale
- `esegui()`: metodo principale che coordina l'esecuzione

## Contribuire

Contribuzioni, issue e feature request sono benvenuti! Sentiti libero di aprire una issue o una pull request.

## Licenza

Questo progetto è open source e disponibile per uso personale ed educativo.

## Contatti

Damiano Ceka - [@DamianoCeka](https://github.com/DamianoCeka)

Link progetto: [https://github.com/DamianoCeka/AnimalHealthDiary](https://github.com/DamianoCeka/AnimalHealthDiary)
