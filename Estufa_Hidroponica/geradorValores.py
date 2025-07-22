import requests
import random
import time
from datetime import datetime

API_URL = "http://localhost:8000/estufa"

# Estado inicial
dados_atuais = {
    "estufa_id": "1",
    "temperatura_ar": 25.0,
    "temperatura_agua": 22.0,
    "umidade_ar": 65.0,
    "luminosidade": 70.0,
    "ph_agua": 6.5,
    "nutrientes": 400,
    "ventilacao": 1,
    "iluminacao": 1,
    "bomba_agua": 1
}

def variar(valor, min_val, max_val, passo=1):
    novo_valor = valor + random.uniform(-passo, passo)
    return round(max(min(novo_valor, max_val), min_val), 2)

def gerar_dados():
    global dados_atuais
    dados_atuais["temperatura_ar"] = variar(dados_atuais["temperatura_ar"], 15.0, 35.0)
    dados_atuais["temperatura_agua"] = variar(dados_atuais["temperatura_agua"], 15.0, 30.0)
    dados_atuais["umidade_ar"] = variar(dados_atuais["umidade_ar"], 30.0, 90.0)
    dados_atuais["luminosidade"] = variar(dados_atuais["luminosidade"], 0.0, 100.0)
    dados_atuais["ph_agua"] = variar(dados_atuais["ph_agua"], 5.5, 8.5, passo=0.1)
    dados_atuais["nutrientes"] = max(min(dados_atuais["nutrientes"] + random.randint(-10, 10), 800), 200)
    dados_atuais["ventilacao"] = random.choice([0, 1])
    dados_atuais["iluminacao"] = random.choice([0, 1])
    dados_atuais["bomba_agua"] = random.choice([0, 1])
    return dados_atuais

if _name_ == "_main_":
    while True:
        payload = gerar_dados()
        print(f"[{datetime.now().isoformat()}] Enviando: {payload}")
        try:
            response = requests.post(API_URL, json=payload)
            print(f"Resposta: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")
        time.sleep(5)  # envia a cada 5 segundos