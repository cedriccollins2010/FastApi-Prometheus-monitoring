from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

# Définir un compteur Prometheus
REQUEST_COUNT = Counter("app_requests_total", "Total des requêtes reçues")

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()  # Incrémenter le compteur
    return {"message": "Hello, World!"}

@app.get("/metrics")
def get_metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
