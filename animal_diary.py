#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Animal Health Diary - Sistema di monitoraggio salute animali
Accetta input su animale e fornisce consigli basati su regole IA semplici
"""

from datetime import datetime

class AnimalHealthDiary:
    def __init__(self):
        self.entries = []
    
    def raccolta_dati(self):
        """Raccoglie i dati dell'animale dall'utente"""
        print("\n=== DIARIO SALUTE ANIMALE ===")
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
        sintomi = input("Sintomi osservati (separati da virgola, o 'nessuno'): ").lower()
        
        dati = {
            'nome': nome,
            'specie': specie,
            'peso': peso,
            'eta': eta,
            'alimentazione': alimentazione,
            'sintomi': sintomi,
            'data': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        return dati
    
    def analisi_ia(self, dati):
        """Analizza i dati con regole semplici e genera consigli"""
        consigli = []
        avvisi = []
        
        # Analisi peso
        if dati['specie'] == 'cane':
            if dati['peso'] < 5:
                consigli.append("Cane di taglia piccola: attenzione a non sovralimentare")
            elif dati['peso'] > 30:
                consigli.append("Cane di taglia grande: monitorare articolazioni e mobilità")
        elif dati['specie'] == 'gatto':
            if dati['peso'] < 3:
                avvisi.append("Peso sotto la media per un gatto adulto")
            elif dati['peso'] > 6:
                avvisi.append("Possibile sovrappeso - consultare veterinario")
        
        # Analisi età
        if dati['eta'] < 1:
            consigli.append("Cucciolo/giovane: necessarie vaccinazioni e controlli frequenti")
        elif dati['eta'] > 10:
            consigli.append("Animale anziano: raccomandati controlli veterinari ogni 6 mesi")
            consigli.append("Considerare dieta senior e integratori per articolazioni")
        
        # Analisi alimentazione
        if dati['alimentazione'] == 'casalinga':
            consigli.append("Dieta casalinga: assicurarsi che sia bilanciata e completa")
        elif dati['alimentazione'] == 'crocchette':
            consigli.append("Crocchette: verificare qualità ingredienti e adeguatezza all'età")
        
        # Analisi sintomi
        sintomi_gravi = ['vomito', 'diarrea', 'sangue', 'letargia', 'febbre', 'convulsioni']
        sintomi_moderati = ['tosse', 'starnuti', 'prurito', 'perdita appetito', 'sete eccessiva']
        
        sintomi_lista = [s.strip() for s in dati['sintomi'].split(',')]
        
        if 'nessuno' not in dati['sintomi']:
            for sintomo in sintomi_lista:
                if any(grave in sintomo for grave in sintomi_gravi):
                    avvisi.append(f"⚠️  SINTOMO GRAVE: {sintomo.upper()} - CONSULTARE URGENTEMENTE IL VETERINARIO")
                elif any(mod in sintomo for mod in sintomi_moderati):
                    avvisi.append(f"Sintomo da monitorare: {sintomo} - se persiste, consultare veterinario")
        else:
            consigli.append("✓ Nessun sintomo rilevato - continuare monitoraggio regolare")
        
        return consigli, avvisi
    
    def genera_report(self, dati, consigli, avvisi):
        """Genera e stampa il report finale"""
        print("\n" + "="*60)
        print("         REPORT SALUTE ANIMALE")
        print("="*60)
        print(f"\nData: {dati['data']}")
        print(f"\n📋 DATI ANIMALE:")
        print(f"  Nome: {dati['nome'].capitalize()}")
        print(f"  Specie: {dati['specie'].capitalize()}")
        print(f"  Peso: {dati['peso']} kg")
        print(f"  Età: {dati['eta']} anni")
        print(f"  Alimentazione: {dati['alimentazione'].capitalize()}")
        print(f"  Sintomi: {dati['sintomi'].capitalize()}")
        
        if avvisi:
            print(f"\n🚨 AVVISI IMPORTANTI:")
            for avviso in avvisi:
                print(f"  • {avviso}")
        
        if consigli:
            print(f"\n💡 CONSIGLI:")
            for consiglio in consigli:
                print(f"  • {consiglio}")
        
        print("\n" + "="*60)
        print("Nota: Questi consigli sono indicativi. Per diagnosi precise,")
        print("consultare sempre un veterinario professionista.")
        print("="*60 + "\n")
    
    def esegui(self):
        """Metodo principale per eseguire il diario"""
        dati = self.raccolta_dati()
        
        if dati is None:
            return
        
        self.entries.append(dati)
        consigli, avvisi = self.analisi_ia(dati)
        self.genera_report(dati, consigli, avvisi)

def main():
    """Funzione principale"""
    diario = AnimalHealthDiary()
    diario.esegui()

if __name__ == "__main__":
    main()
