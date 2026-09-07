# NetAI Guard v1.0
> Solution d'entreprise pour la surveillance réseau et la détection d'anomalies en temps réel.

**Développeur :** Mohamed Labbas  
**Projet :** Systèmes Numériques / CIEL

---

## 🚀 Architecture du Projet
1. **Agent Telemetry (`agent/collector.py`)** : Script Python qui collecte et génère les métriques du réseau en temps réel.
2. **Dashboard (`dashboard/index.html`)** : Interface utilisateur interactive développée en HTML/CSS/JavaScript avec intégration de Chart.js.
3. **Data Exchange (`dashboard/data.json`)** : Fichier JSON servant de pont de données dynamique entre le moteur Python et le Dashboard.

## 🛠️ Instructions d'exécution
1. Lancer l'agent de collecte :
   ```bash
   cd agent
   python collector.py
