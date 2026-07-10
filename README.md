# Rossmann Handler API

API Flask para servir predições do modelo de vendas Rossmann, hospedada no Render.

## Endpoints

### POST /rossmann/predict
Recebe dados em JSON e retorna a predição de vendas.

## Deploy
Hospedado no Render.com. Start command:

## Estrutura
- `handler.py` — servidor Flask
- `rossmann/` — pipeline de pré-processamento e feature engineering
- `model/model_rossmann.pkl` — modelo treinado
