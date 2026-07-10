# Rossmann Handler API

API Flask para servir predições do modelo de vendas Rossmann, hospedada no Render.

## Endpoints

### POST /rossmann/predict
Recebe dados em JSON e retorna a predição de vendas.

**Exemplo de request:**
```json
{
  "Store": 1,
  "DayOfWeek": 5,
  "Date": "2015-07-31"
}
```

## Deploy
Hospedado no Render.com. Start command:## Estrutura
- `handler.py` — servidor Flask
- `rossmann/` — pipeline de pré-processamento e feature engineering
- `model/model_rossmann.pkl` — modelo treinado
