import time
import json
import random
from datetime import datetime

# Agent de collecte de données réseau pour NetAI Guard
print("=== NetAI Guard Agent - Démarrage du système de surveillance ===")

def collect_network_metrics():
    """
    Simule la collecte des données réseau en temps réel
    """
    metrics = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "active_devices": random.randint(10, 15),
        "traffic_mbps": round(random.uniform(50.0, 150.0), 2),
        "status": "Opérationnel",
        "threat_level": "Faible"
    }
    return metrics

# Boucle de surveillance en continu
try:
    while True:
        data = collect_network_metrics()
        print(f"[{data['timestamp']}] Collecte réussie | Trafic: {data['traffic_mbps']} Mbps | Statut: {data['status']}")
        
        # Sauvegarde des métriques pour le Dashboard
        with open("../dashboard/data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        time.sleep(3) # Pause de 3 secondes entre chaque analyse

except KeyboardInterrupt:
    print("\n=== Arrêt de l'agent de surveillance ===")