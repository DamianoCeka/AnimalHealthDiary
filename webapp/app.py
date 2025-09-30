#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Animal Health Diary - Flask Web Application
Applicazione web per monitoraggio salute animali con AI
"""

import os
import sys
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Aggiungi la directory parent al path per importare animal_diary_api
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from animal_diary_api import AnimalHealthDiaryAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Directory per salvare i dati
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# File per lo storico
HISTORY_FILE = os.path.join(DATA_DIR, 'health_history.json')


def load_history():
    """Carica lo storico delle visite dal file JSON"""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []


def save_history(history):
    """Salva lo storico delle visite nel file JSON"""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False


@app.route('/')
def index():
    """Pagina principale con form"""
    return render_template('index.html')


@app.route('/history')
def history():
    """Pagina storico visite"""
    history_data = load_history()
    return render_template('history.html', entries=history_data)


@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint per analisi AI dei dati animale"""
    try:
        # Ottieni i dati dal form
        dati = {
            'nome': request.form.get('nome', ''),
            'specie': request.form.get('specie', ''),
            'peso': float(request.form.get('peso', 0)),
            'eta': int(request.form.get('eta', 0)),
            'alimentazione': request.form.get('alimentazione', ''),
            'attivita': request.form.get('attivita', ''),
            'sintomi': request.form.get('sintomi', ''),
            'note': request.form.get('note', ''),
            'data': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        # Verifica che OPENAI_API_KEY sia configurata
        if not os.getenv('OPENAI_API_KEY'):
            return jsonify({
                'error': True,
                'message': 'OPENAI_API_KEY non configurata. Impostare la variabile d\'ambiente.'
            }), 400
        
        # Inizializza l'API e ottieni l'analisi
        api = AnimalHealthDiaryAPI()
        risposta_ai = api.analisi_ai(dati)
        
        # Crea l'entry per lo storico
        entry = {
            'id': datetime.now().strftime("%Y%m%d_%H%M%S"),
            'dati': dati,
            'analisi_ai': risposta_ai,
            'timestamp': datetime.now().isoformat()
        }
        
        # Salva nello storico
        history_data = load_history()
        history_data.insert(0, entry)  # Aggiungi all'inizio
        save_history(history_data)
        
        return jsonify({
            'success': True,
            'entry_id': entry['id'],
            'dati': dati,
            'analisi': risposta_ai
        })
        
    except ValueError as e:
        return jsonify({
            'error': True,
            'message': f'Errore nei dati inseriti: {str(e)}'
        }), 400
    except Exception as e:
        return jsonify({
            'error': True,
            'message': f'Errore durante l\'analisi: {str(e)}'
        }), 500


@app.route('/entry/<entry_id>')
def view_entry(entry_id):
    """Visualizza una singola entry"""
    history_data = load_history()
    entry = next((e for e in history_data if e['id'] == entry_id), None)
    
    if entry:
        return render_template('entry.html', entry=entry)
    else:
        return "Entry non trovata", 404


@app.route('/delete/<entry_id>', methods=['POST'])
def delete_entry(entry_id):
    """Elimina una entry dallo storico"""
    history_data = load_history()
    history_data = [e for e in history_data if e['id'] != entry_id]
    
    if save_history(history_data):
        return jsonify({'success': True})
    else:
        return jsonify({'error': True, 'message': 'Errore durante l\'eliminazione'}), 500


@app.route('/api/status')
def api_status():
    """Controlla lo stato dell'API OpenAI"""
    api_key = os.getenv('OPENAI_API_KEY')
    return jsonify({
        'api_configured': bool(api_key),
        'entries_count': len(load_history())
    })


if __name__ == '__main__':
    print("\n" + "="*70)
    print("  ANIMAL HEALTH DIARY - WEB APPLICATION")
    print("="*70)
    print("\n🌐 Avvio server Flask...\n")
    
    # Verifica configurazione API
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  ATTENZIONE: OPENAI_API_KEY non configurata!")
        print("   Per utilizzare l'analisi AI, impostare:")
        print("   export OPENAI_API_KEY='sk-...'  (Linux/Mac)")
        print("   set OPENAI_API_KEY=sk-...      (Windows)\n")
    else:
        print("✅ OPENAI_API_KEY configurata\n")
    
    print("📍 Applicazione disponibile su: http://127.0.0.1:5000")
    print("   Premi Ctrl+C per fermare il server\n")
    print("="*70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
