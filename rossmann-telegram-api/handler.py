import os
import json
import pandas as pd
import sys
import time

from flask import Flask, request, Response
from xgboost import XGBRegressor
from rossmann.Rossmann import Rossmann


def log(msg):
    # print + flush garante que a linha aparece IMEDIATAMENTE nos logs do Render
    # (sem flush, o Python pode bufferizar e você só veria tudo de uma vez no final)
    print(f"[BOOT] {msg}", flush=True)

t0 = time.time()
log("iniciando handler.py")
log(f"python version: {sys.version}")
log(f"cwd: {os.getcwd()}")
log(f"arquivos na raiz: {os.listdir('.')}")

log("carregando modelo...")
#loading model
model = XGBRegressor()
model.load_model('model/model_rossmann.json')
log(f"modelo carregado em {time.time() - t0:.2f}s")

log("inicializando Flask app...")
#initialize API
app = Flask(__name__)
log("Flask app criado")


@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():

    try:
        test_json = request.get_json(silent=True)

        log(f"Content-Type: {request.content_type}")
        log(f"JSON recebido: {test_json}")

        if not test_json:
            return Response(
                response='{"erro": "JSON não informado ou inválido"}',
                status=400,
                mimetype='application/json'
            )

        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(
                test_json,
                columns=test_json[0].keys()
            )

        log(f"Dados recebidos: {test_raw.to_dict(orient='records')}")

        pipeline = Rossmann()

        # Data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # Feature engineering
        df2 = pipeline.feature_engineering(df1)

        # Data preparation
        df3 = pipeline.data_preparation(df2)

        # Prediction
        df_response = pipeline.get_prediction(
            model,
            test_raw,
            df3
        )

        return Response(
            response=df_response,
            status=200,
            mimetype='application/json'
        )

    except Exception as e:

        log(f"ERRO: {type(e).__name__}: {e}")

        return Response(
            response=str(e),
            status=500,
            mimetype='application/json'
        )

# rota simples para o Render confirmar que o serviço está de pé
@app.route('/', methods=['GET'])
def health():
    return Response('ok', status=200)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    log(f"chamando app.run na porta {port}")
    app.run(host='0.0.0.0', port=port)