#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Animal Health Diary - API Version with OpenAI Integration
Sistema di monitoraggio salute animali con intelligenza artificiale avanzata
"""

import os
import json
from datetime import datetime
from openai import OpenAI

class AnimalHealthDiaryAPI:
    def __init__(self, api_key=None):
        """
        Inizializza il diario con integrazione OpenAI
        
        Args:
            api_key: Chiave API OpenAI (se None, viene letta da variabile d'ambiente)
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError(
                "API Key mancante! Impostare OPENAI_API_KEY come variabile d'ambiente "
                "o passarla al costruttore."
            )
        
        self.client = OpenAI(api_key=self.api_key)
        self.entries = []
        self.model = "gpt-4o-mini"  # Modello economico e veloce
    
    def raccolta_dati(self):
        """Raccoglie i dati dell'animale dall'utente"""
        print("\n=== DIARIO SALUTE ANIMALE - AI VERSION ===")
        print("Inserisci i dati dell'animale:\n")
        
        nome = input("Nome animale: ")
        specie = input("Specie (cane/gatto/altro): ").lower()
        
        try:
            peso = float(input("Peso (kg): "))
            eta = int(input("Età (anni): "))
        except ValueError:
            print("Errore: inserire valori numerici validi per peso ed età")
            return None
        
        alimentazione = input("Alimentazione (crocchette/umido/mista/casalinga): ").lower()
        attivita = input("Livello di attività (basso/medio/alto): ").lower()
        sintomi = input("Sintomi osservati (descrizione dettagliata o 'nessuno'): ")
        note_aggiuntive = input("Note aggiuntive (opzionale): ")
        
        dati = {
            'nome': nome,
            'specie': specie,
            'peso': peso,
            'eta': eta,
            'alimentazione': alimentazione,
            'attivita': attivita,
            'sintomi': sintomi,
            'note': note_aggiuntive,
            'data': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        return dati
    
    def crea_prompt(self, dati):
        """Crea il prompt per l'AI basato sui dati dell'animale"""
        prompt = f"""Sei un assistente veterinario esperto. Analizza i seguenti dati di un animale e fornisci:
1. Valutazione dello stato di salute generale
2. Consigli specifici per alimentazione e cura
3. Avvisi su eventuali sintomi preoccupanti
4. Raccomandazioni su quando consultare un veterinario

Dati dell'animale:
- Nome: {dati['nome']}
- Specie: {dati['specie']}
- Peso: {dati['peso']} kg
- Età: {dati['eta']} anni
- Alimentazione: {dati['alimentazione']}
- Livello di attività: {dati['attivita']}
- Sintomi: {dati['sintomi']}
- Note aggiuntive: {dati['note']}

Fornisci una risposta strutturata, professionale ma comprensibile, in italiano.
Ricorda di specificare sempre che questi sono consigli generali e non sostituiscono una visita veterinaria.
"""
        return prompt
    
    def analisi_ai(self, dati):
        """
        Invia i dati all'API OpenAI e ottiene una risposta intelligente
        
        Args:
            dati: Dizionario con i dati dell'animale
            
        Returns:
            Risposta dell'AI come stringa
        """
        print("\n🤖 Analisi AI in corso...")
        
        try:
            prompt = self.crea_prompt(dati)
            
            # Chiamata all'API OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Sei un assistente veterinario esperto e premuroso. "
                                   "Fornisci consigli utili e professionali sulla salute degli animali."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            risposta_ai = response.choices[0].message.content
            return risposta_ai
            
        except Exception as e:
            return f"Errore nella chiamata API: {str(e)}"
    
    def genera_report(self, dati, risposta_ai):
        """Genera e stampa il report finale con l'analisi AI"""
        print("\n" + "="*70)
        print("         REPORT SALUTE ANIMALE - ANALISI AI")
        print("="*70)
        print(f"\nData: {dati['data']}")
        print(f"\n📋 DATI ANIMALE:")
        print(f"  Nome: {dati['nome'].capitalize()}")
        print(f"  Specie: {dati['specie'].capitalize()}")
        print(f"  Peso: {dati['peso']} kg")
        print(f"  Età: {dati['eta']} anni")
        print(f"  Alimentazione: {dati['alimentazione'].capitalize()}")
        print(f"  Attività: {dati['attivita'].capitalize()}")
        print(f"  Sintomi: {dati['sintomi']}")
        if dati['note']:
            print(f"  Note: {dati['note']}")
        
        print(f"\n🤖 ANALISI INTELLIGENTE AI:")
        print("-" * 70)
        print(risposta_ai)
        print("-" * 70)
        
        print("\n" + "="*70)
        print("Nota: Questi consigli sono indicativi e generati da AI.")
        print("Per diagnosi precise, consultare sempre un veterinario professionista.")
        print("="*70 + "\n")
    
    def salva_entry(self, dati, risposta_ai):
        """Salva l'entry in formato JSON"""
        entry = {
            'dati': dati,
            'analisi_ai': risposta_ai,
            'timestamp': datetime.now().isoformat()
        }
        self.entries.append(entry)
        
        # Salva su file
        try:
            filename = f"health_diary_{dati['nome']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)
            print(f"✅ Entry salvata in: {filename}")
        except Exception as e:
            print(f"⚠️  Errore nel salvataggio: {str(e)}")
    
    def esegui(self, salva=True):
        """Metodo principale per eseguire il diario con AI"""
        dati = self.raccolta_dati()
        
        if dati is None:
            return
        
        risposta_ai = self.analisi_ai(dati)
        self.genera_report(dati, risposta_ai)
        
        if salva:
            self.salva_entry(dati, risposta_ai)


def test_api_connection():
    """Test di connessione all'API OpenAI"""
    print("\n=== TEST CONNESSIONE API OpenAI ===")
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY non trovata!")
        print("\nPer impostarla:")
        print("  Linux/Mac: export OPENAI_API_KEY='la-tua-chiave-api'")
        print("  Windows: set OPENAI_API_KEY=la-tua-chiave-api")
        return False
    
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Test"}],
            max_tokens=5
        )
        print("✅ Connessione API riuscita!")
        print(f"   Modello: gpt-4o-mini")
        return True
    except Exception as e:
        print(f"❌ Errore connessione: {str(e)}")
        return False


def main():
    """Funzione principale"""
    import sys
    
    # Se viene passato --test, esegue solo il test di connessione
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_api_connection()
        return
    
    try:
        diario = AnimalHealthDiaryAPI()
        diario.esegui()
    except ValueError as e:
        print(f"\n❌ Errore: {str(e)}")
        print("\nPer impostare la chiave API:")
        print("  export OPENAI_API_KEY='sk-...'  # Linux/Mac")
        print("  set OPENAI_API_KEY=sk-...      # Windows")
    except KeyboardInterrupt:
        print("\n\nInterrotto dall'utente.")
    except Exception as e:
        print(f"\n❌ Errore inaspettato: {str(e)}")


if __name__ == "__main__":
    main()
