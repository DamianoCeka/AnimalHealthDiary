# 📱 PWA Setup Guide - AnimalHealthDiary

## Cos'è una PWA (Progressive Web App)?

Una Progressive Web App è un'applicazione web che può essere installata sul tuo dispositivo (smartphone, tablet, o desktop) e funzionare come un'app nativa, con funzionalità offline e un'icona nella home screen.

## 🎯 Vantaggi della PWA

- **📥 Installabile**: Aggiungi l'app alla home screen senza passare dagli store
- **📴 Funzionamento offline**: Accedi ai contenuti anche senza connessione
- **⚡ Veloce**: Caricamento rapido grazie alla cache
- **📲 Esperienza app-like**: Schermo intero, senza barra del browser
- **🔔 Notifiche push**: Ricevi aggiornamenti importanti (coming soon)
- **💾 Leggera**: Occupa meno spazio rispetto alle app native

## 📁 File PWA Inclusi

La cartella `landingpage/` contiene tutti i file necessari per il funzionamento della PWA:

### 1. `manifest.json`
File di configurazione che definisce:
- Nome dell'app: "AnimalHealthDiary"
- Icone (192x192 e 512x512)
- Colore del tema: #667eea (gradiente viola)
- Modalità display: standalone
- Orientamento: portrait

### 2. `service-worker.js`
Script che gestisce:
- **Cache delle risorse**: Salva file per uso offline
- **Strategie di caching**: Cache-first con fallback alla rete
- **Aggiornamenti**: Pulizia automatica delle vecchie cache

### 3. Logo Icons
Devi aggiungere due icone nella cartella `landingpage/`:
- `logo192.png` (192x192 pixel)
- `logo512.png` (512x512 pixel)

**Come creare i loghi:**
1. Usa il logo SVG in `branding/logo_demo.svg` come base
2. Convertilo in PNG con tool online come [CloudConvert](https://cloudconvert.com/svg-to-png)
3. Ridimensiona a 192x192 e 512x512 pixel
4. Salva nella cartella `landingpage/`

## 🔧 Come Aggiungere il PWA al tuo index.html

Per rendere la landing page una PWA completa, aggiungi questi tag nel `<head>` di `index.html`:

```html
<!-- PWA Meta Tags -->
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#667eea">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="AnimalHealth">
<link rel="apple-touch-icon" href="logo192.png">

<!-- Favicons -->
<link rel="icon" type="image/png" sizes="192x192" href="logo192.png">
<link rel="icon" type="image/png" sizes="512x512" href="logo512.png">
```

Poi, prima del tag di chiusura `</body>`, aggiungi lo script per registrare il service worker:

```html
<!-- PWA Service Worker Registration -->
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/service-worker.js')
        .then(registration => {
          console.log('✅ Service Worker registrato:', registration.scope);
        })
        .catch(error => {
          console.log('❌ Errore registrazione Service Worker:', error);
        });
    });
  }
</script>
```

## 📱 Come Installare la PWA

### Su Android (Chrome/Edge)
1. Apri il sito nel browser
2. Tocca il menu ⋮ (tre puntini)
3. Seleziona "Aggiungi a schermata Home" o "Installa app"
4. Conferma l'installazione
5. L'icona apparirà nella home screen

### Su iOS (Safari)
1. Apri il sito in Safari
2. Tocca il pulsante Condividi 📤
3. Scorri e seleziona "Aggiungi a Home"
4. Personalizza il nome (opzionale)
5. Tocca "Aggiungi"

### Su Desktop (Chrome/Edge)
1. Visita il sito
2. Cerca l'icona di installazione ➕ nella barra degli indirizzi
3. Clicca su "Installa"
4. L'app si aprirà in una finestra dedicata

## 🧪 Come Testare la PWA

### 1. Test Locale
```bash
cd landingpage
python -m http.server 8000
```
Apri `http://localhost:8000` nel browser

### 2. Chrome DevTools
1. Apri DevTools (F12)
2. Vai alla tab "Application"
3. Controlla:
   - **Manifest**: Verifica nome, icone, colori
   - **Service Workers**: Stato "activated and running"
   - **Cache Storage**: Risorse salvate

### 3. Lighthouse Audit
1. DevTools → Tab "Lighthouse"
2. Seleziona "Progressive Web App"
3. Click "Generate report"
4. Target: Score > 90/100

## 🚀 Deploy della PWA

### GitHub Pages
```bash
# Settings → Pages → Source: main branch → /landingpage folder
# URL: https://<username>.github.io/AnimalHealthDiary/
```

### Netlify
```bash
netlify deploy --dir=landingpage --prod
```

### Vercel
```bash
vercel --prod
```

**Importante**: Assicurati che il server serva i file con HTTPS (obbligatorio per le PWA).

## 🐛 Troubleshooting

### Service Worker non si registra
- ✅ Verifica che il sito sia su HTTPS (o localhost)
- ✅ Controlla la console per errori
- ✅ Verifica il path di `service-worker.js`

### Icone non appaiono
- ✅ Controlla che `logo192.png` e `logo512.png` esistano
- ✅ Verifica i path nel `manifest.json`
- ✅ Svuota la cache e ricarica

### Cache non funziona
- ✅ Apri DevTools → Application → Clear storage
- ✅ Aggiorna la versione cache in `service-worker.js` (es. `v2`)
- ✅ Ricarica la pagina

### App non si installa
- ✅ Verifica che il manifest sia valido (DevTools → Application → Manifest)
- ✅ Controlla che ci siano le icone minime (192x192)
- ✅ Assicurati che il sito sia su HTTPS

## 📚 Risorse Utili

- [Web.dev - PWA Guide](https://web.dev/progressive-web-apps/)
- [MDN - Progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [PWA Builder](https://www.pwabuilder.com/) - Test e validazione PWA
- [Manifest Generator](https://app-manifest.firebaseapp.com/) - Generatore manifest.json

## 🎨 Personalizzazione

### Cambiare Colori
Modifica in `manifest.json`:
```json
"theme_color": "#TUO_COLORE",
"background_color": "#TUO_COLORE"
```

### Cambiare Nome
Modifica in `manifest.json`:
```json
"name": "Il Tuo Nome App",
"short_name": "NomeBreve"
```

### Aggiungere Più Icone
```json
"icons": [
  {
    "src": "icon-72x72.png",
    "sizes": "72x72",
    "type": "image/png"
  },
  { ... }
]
```

## 💡 Best Practices

1. **Performance**: Mantieni il service worker leggero
2. **Cache Strategy**: Usa cache-first per asset statici, network-first per API
3. **Update**: Incrementa la versione cache quando aggiorni i file
4. **Icons**: Usa icone con sfondo per maskable icons
5. **Testing**: Testa su dispositivi reali, non solo emulatori

## 🔄 Aggiornamento della PWA

Quando modifichi i file:

1. Aggiorna la versione cache in `service-worker.js`:
   ```javascript
   const CACHE_NAME = 'animalhealthdiary-v2'; // v1 → v2
   ```

2. Il vecchio service worker verrà sostituito automaticamente
3. Gli utenti riceveranno l'aggiornamento al prossimo caricamento

## 📞 Supporto

Se hai problemi con la PWA:
- Apri una [issue su GitHub](https://github.com/DamianoCeka/AnimalHealthDiary/issues)
- Email: spekter99@gmail.com

---

**Ultima modifica**: 30 Settembre 2025  
**Versione**: 1.0.0
