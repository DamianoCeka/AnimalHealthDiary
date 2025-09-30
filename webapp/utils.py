#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility functions for Animal Health Diary webapp
Funzioni per grafici, notifiche email, esportazione dati
"""
import os
import json
import csv
import io
import base64
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Backend non interattivo per server
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from flask import make_response

# Sintomi critici che richiedono notifica immediata
CRITICAL_SYMPTOMS = [
    'vomito', 'diarrea', 'sangue', 'letargia', 'febbre', 'convulsioni',
    'difficolta respiratorie', 'perdita coscienza', 'collasso'
]

class EmailAlert:
    """Simulatore di notifiche email per sintomi critici"""
    
    @staticmethod
    def check_critical_symptoms(sintomi_str):
        """
        Verifica se ci sono sintomi critici
        Ritorna: (has_critical, critical_list)
        """
        if not sintomi_str or sintomi_str.lower() == 'nessuno':
            return False, []
        
        sintomi = [s.strip().lower() for s in sintomi_str.split(',')]
        critical_found = []
        
        for sintomo in sintomi:
            for critical in CRITICAL_SYMPTOMS:
                if critical in sintomo:
                    critical_found.append(sintomo)
                    break
        
        return len(critical_found) > 0, critical_found
    
    @staticmethod
    def generate_alert_message(animal_name, sintomi_critici):
        """
        Genera il messaggio di alert per sintomi critici
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        message = {
            'tipo': 'ALLERTA SINTOMI CRITICI',
            'animale': animal_name,
            'sintomi': sintomi_critici,
            'timestamp': timestamp,
            'raccomandazione': 'CONSULTARE IMMEDIATAMENTE UN VETERINARIO',
            'simulazione': True  # Indica che è una simulazione
        }
        
        return message

class ChartGenerator:
    """Generatore di grafici con Matplotlib"""
    
    @staticmethod
    def generate_weight_chart(history_data, animal_name=None):
        """
        Genera grafico dell'andamento del peso nel tempo
        Ritorna: stringa base64 dell'immagine PNG
        """
        if not history_data:
            return None
        
        # Filtra per animale specifico se richiesto
        if animal_name:
            history_data = [e for e in history_data if e.get('dati', {}).get('nome') == animal_name]
        
        if not history_data or len(history_data) < 2:
            return None
        
        # Estrai date e pesi
        dates = []
        weights = []
        
        for entry in reversed(history_data):  # Dal più vecchio al più recente
            try:
                data = entry.get('dati', {})
                peso = float(data.get('peso', 0))
                timestamp = entry.get('timestamp', '')
                
                if peso > 0 and timestamp:
                    date = datetime.fromisoformat(timestamp)
                    dates.append(date)
                    weights.append(peso)
            except:
                continue
        
        if len(dates) < 2:
            return None
        
        # Crea il grafico
        plt.figure(figsize=(10, 6))
        plt.plot(dates, weights, marker='o', linestyle='-', linewidth=2, markersize=8)
        plt.xlabel('Data', fontsize=12)
        plt.ylabel('Peso (kg)', fontsize=12)
        title = f'Andamento Peso - {animal_name}' if animal_name else 'Andamento Peso'
        plt.title(title, fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Formatta asse x per date
        plt.gcf().autofmt_xdate()
        
        # Converti in base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return f"data:image/png;base64,{image_base64}"
    
    @staticmethod
    def generate_activity_chart(history_data, animal_name=None):
        """
        Genera grafico dell'attività registrata
        Ritorna: stringa base64 dell'immagine PNG
        """
        if not history_data:
            return None
        
        # Filtra per animale specifico se richiesto
        if animal_name:
            history_data = [e for e in history_data if e.get('dati', {}).get('nome') == animal_name]
        
        if not history_data:
            return None
        
        # Conta le attività
        activity_counts = {}
        
        for entry in history_data:
            data = entry.get('dati', {})
            attivita = data.get('attivita', 'Non specificata')
            activity_counts[attivita] = activity_counts.get(attivita, 0) + 1
        
        if not activity_counts:
            return None
        
        # Crea il grafico a barre
        plt.figure(figsize=(10, 6))
        activities = list(activity_counts.keys())
        counts = list(activity_counts.values())
        
        plt.bar(activities, counts, color='steelblue', alpha=0.8)
        plt.xlabel('Livello Attività', fontsize=12)
        plt.ylabel('Numero Registrazioni', fontsize=12)
        title = f'Distribuzione Attività - {animal_name}' if animal_name else 'Distribuzione Attività'
        plt.title(title, fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        
        # Converti in base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return f"data:image/png;base64,{image_base64}"

class DataExporter:
    """Esportatore dati in vari formati"""
    
    @staticmethod
    def export_to_csv(history_data):
        """
        Esporta lo storico in formato CSV
        Ritorna: Response Flask con il file CSV
        """
        output = io.StringIO()
        
        if not history_data:
            return None
        
        # Header CSV
        fieldnames = ['ID', 'Data', 'Nome', 'Specie', 'Peso (kg)', 'Età (anni)', 
                     'Alimentazione', 'Attività', 'Sintomi', 'Note']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        
        # Scrivi i dati
        for entry in history_data:
            dati = entry.get('dati', {})
            writer.writerow({
                'ID': entry.get('id', ''),
                'Data': dati.get('data', ''),
                'Nome': dati.get('nome', ''),
                'Specie': dati.get('specie', ''),
                'Peso (kg)': dati.get('peso', ''),
                'Età (anni)': dati.get('eta', ''),
                'Alimentazione': dati.get('alimentazione', ''),
                'Attività': dati.get('attivita', ''),
                'Sintomi': dati.get('sintomi', ''),
                'Note': dati.get('note', '')
            })
        
        # Crea la response
        csv_data = output.getvalue()
        output.close()
        
        response = make_response(csv_data)
        response.headers['Content-Type'] = 'text/csv; charset=utf-8'
        response.headers['Content-Disposition'] = 'attachment; filename=animal_health_history.csv'
        
        return response
    
    @staticmethod
    def export_to_json(history_data):
        """
        Esporta lo storico in formato JSON
        Ritorna: Response Flask con il file JSON
        """
        if not history_data:
            return None
        
        json_data = json.dumps(history_data, ensure_ascii=False, indent=2)
        
        response = make_response(json_data)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        response.headers['Content-Disposition'] = 'attachment; filename=animal_health_history.json'
        
        return response

class PhotoManager:
    """Gestore upload foto (simulazione)"""
    
    @staticmethod
    def save_photo(file, entry_id):
        """
        Salva una foto associata a un'entry
        Ritorna: (success, filename/error_message)
        """
        if not file:
            return False, "Nessun file fornito"
        
        # Verifica estensione
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        filename = file.filename
        
        if '.' not in filename:
            return False, "File senza estensione"
        
        ext = filename.rsplit('.', 1)[1].lower()
        if ext not in allowed_extensions:
            return False, f"Estensione non supportata. Usa: {', '.join(allowed_extensions)}"
        
        # Crea directory photos se non esiste
        photos_dir = os.path.join(os.path.dirname(__file__), 'data', 'photos')
        os.makedirs(photos_dir, exist_ok=True)
        
        # Genera nome file unico
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_filename = f"{entry_id}_{timestamp}.{ext}"
        filepath = os.path.join(photos_dir, safe_filename)
        
        try:
            file.save(filepath)
            return True, safe_filename
        except Exception as e:
            return False, str(e)
    
    @staticmethod
    def get_photo_path(filename):
        """
        Ottieni il path completo di una foto
        """
        photos_dir = os.path.join(os.path.dirname(__file__), 'data', 'photos')
        return os.path.join(photos_dir, filename) if filename else None
