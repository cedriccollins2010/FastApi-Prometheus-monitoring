# FastAPI + Prometheus Monitoring

Ce projet montre comment monitorer une API **FastAPI** avec **Prometheus**, sans Docker ni Grafana.

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/cedriccollins2010/FastApi-Prometheus-monitoring.git
cd FastApi-Prometheus-monitoring
2. Installer les dépendances Python
bash
Copier
cd app
pip install -r requirements.txt
🚀 Lancer l'API
bash
Copier
python app.py
Accès API : http://localhost:8000

Métriques Prometheus : http://localhost:8000/metrics

📈 Démarrer Prometheus
Télécharger Prometheus ici : https://prometheus.io/download/

Placez prometheus.yml dans le dossier Prometheus

Lancer Prometheus :

bash
Copier
cd path\to\prometheus\
prometheus.exe --config.file=prometheus.yml
Interface Prometheus : http://localhost:9090

✅ Exemple de requête Prometheus
text
Copier
app_requests_total
📁 Arborescence
Copier
.
├── app/
│   ├── app.py
│   └── requirements.txt
├── prometheus/
│   └── prometheus.yml
└── README.md
