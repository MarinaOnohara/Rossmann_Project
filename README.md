# Rossmann Project

## Previsão de vendas diárias por 6 semanas
![Rossmann_Store](/img/ROSSMANN.png "Rossmann Store")

### 1. Problema de negócio

Previsão de vendas diárias de 6 semanas para 1.115 lojas espalhadas pela Alemanha. Os dados distribuídos em 3 arquivos no Kaggle permite o desenvolvimento de um modelo de previsão robusto para ajudar os gerentes de loja a manter o foco no que é mais importante para eles: seus clientes e suas equipes!


#### Base de Dados

train.csv - dados históricos, incluindo vendas recentes
test.csv - dados históricos excluindo vendas recentes
store.csv - informações complementares sobre as lojas

[Kaggle](https://www.kaggle.com/competitions/rossmann-store-sales/data)


#### Campos de Dados

- ID - ID que representa uma loja (Store, Date) concatenado dentro do conjunto de teste.
- Store - ID único para cada loja.
- Sales - o volume de vendas em um determinado dia (este é o dado a ser predito).
- Customers - o número de clientes em um determinado dia.
- Open - indicador para saber se a loja estava aberta: 0 = fechada, 1 = aberta.
- StateHoliday - indica um feriado estadual. Normalmente todas as lojas, com poucas exceções, fecham nos feriados estaduais. Observe que todas as escolas fecham nos feriados e finais de semana. a = feriado, b = feriado da Páscoa, c = Natal, 0 = Nenhum.
- SchoolHoliday - indica se (Store, Date) foi afetada pelo fechamento de escolas públicas.
- StoreType - diferencia entre 4 modelos de loja diferentes: a, b, c, d.
- Assortment - descreve um nível de sortimento: a = básico, b = extra, c = estendido.
- CompetitionDistance - distância em metros até a loja concorrente mais próxima.
- CompetitionOpenSince[Month/Year] - apresenta o ano e mês aproximados em que o concorrente mais próximo foi aberto.
- Promo - indica se uma loja está fazendo uma promoção naquele dia.
- Promo2 - Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando
- Promo2Since[Year/Week] - descreve o ano e a semana em que a loja começou a participar da Promo2.
- PromoInterval - descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja.


### Premissa de Negócio

- Apenas consideradas lojas com vendas superior a 0.
- Foram descartados os dias em que as lojas foram fechadas.
- Lojas em que não possuíam dados de competidores próximos tiveram o seu valor fixado em 200.000 metros.


### Estratégia de Solução

O objetivo do projeto é prever as vendas das 1.115 lojas para planejamento orçamentário de cada loja de modo a facilitar o trabalho da gestão. O modelo adotado busca prever as vendas diárias das 6 semanas seguintes.

O formato de entrega contém informações de total de vendas da rede de loja, vendas por unidade de loja e vendas diárias.


#### Planejamento do Processo de Análise

O processo de desenvolvimento do projeto teve como base o método CRSIP-DM, aplicando os seguintes passos:
![Rossmann_Process](/img/processo.png "Processo CRISP")

1. Questão do negócio:
Identificação e entendimento do problema de negócio. Identificar potencial previsão de demandapor loja para ajudar os gerentes de ponto de venda a manter o foco no que é mais importante para eles: seus clientes e suas equipes!

2. Entendimento do negócio:
Entendimento do core business do negócio a fim de identificar estratégia de análise a ser implementada e foco na resolução do problema.

3. Coleta de dados:
Seleção de dados disponibilizados em 3 bases em formato csv (train.csv, test.csv e store.csv) no site Kaggle. Rossmann Store Sales. Disponível em: <https://www.kaggle.com/competitions/rossmann-store-sales/data>. Acesso em: 25 mai. 2026.

4. Limpeza de dados:
Foram realizadas limpeza e tratamento de formatação dos dados de acordo com padrões documentados; padronização do formato dos títulos das variáveis; formatação do tipos e grandezas dos campos de análise; remoção de dados dias com lojas fechadadas; remoção de lojas sem vendas; inclusão de valor de maior distância observada no conjunto de dados cujas lojas não apresentassem informações no campo "Competition Distance"; tratamento ou remoção de campos vazios e remoção de atributo “customers” cuja dimenssão é irrelevante para a análise atual.

5. Exploração de dados:
A etapa de exploração de dados consistiu no levantamento das hipóteses e análise descritiva dos dados para visão do cenário inicial de informações, volume de dados e seleção de variáveis numéricas e categóricas para análise univariada.
Foi desenvolvido mapa mental de hipóteses para levantamento de trinte e uma hipóteses a serem validadas ou refutadas através da análise exploratória dos dados (EDA) em 5 campos do fenômeno analisado vendas: loja, localização, clientes, produtos e período.

![mind_map](/img/MindmapHypothesis.png "Mind Map")

Elementos de mapa mental de hipóteses:
    - Fenômeno: campo a ser medido ou modelado (variável resposta = y);
    - Agentes: agentes que impactam seu fenômeno (variáveis independentes = x);
    - Atributos do agente: características dos atributos.

Hipóteses são geradas por:
    - Surpresa: insight com hipóteses não analisadas;
    - Teste de crença: verificar se a contraposição da crença é validada ou não. Isto é, validação da hipótese nula (H₀) ou da hipótese alternativa (H₁).

Das 31 hipóteses levantadas, 13 foram selecionadas para validação através de análises univariadas, bivariadas e multivariadas de variáveis numéricas e categóricas do conjunto.

#### 13 Hipóteses:
    1. Lojas com maior sortimento devem vender mais.
    2. Lojas com concorrentes mais próximos devem vender menos.
    3. Lojas com concorrentes mais antigos devem vender mais.
    4. Lojas onde os produtos custam menos por mais tempo (promoções ativas) devem vender mais.
    5. Lojas com mais dias de promoção devem vender mais.
    6. Lojas com promoções mais estendidas devem vender mais.
    7. Lojas abertas no feriado de Natal devem vender mais.
    8. Lojas devem vender mais ao longo dos anos.
    9. Lojas devem vender mais no segundo semestre.
    10. As lojas devem vender mais após o dia 10 de cada mês.
    11. Lojas devem vender menos nos finais de semana.
    12. Lojas devem vender menos durante as férias escolares.
    13. Lojas que abrem aos domingos devem vender mais.

#### Top 3 Insights

    H2. Lojas com competidores mais próximos deveriam vender menos.
        FALSA. Lojas com competidores MAIS PRÓXIMOS vendem MAIS
![Hitótese 1](/img/H2.png "Lojas com competidores MAIS PROXIMOS vendem MAIS")

    H4. Lojas com promoções ativas por mais tempo deveriam vender mais.
        FALSA Lojas vendem MENOS depois de um certo período de promoção
![Hitótese 4](/img/H4.png "Lojas vendem menos depois de um certo período de promoção")

    H11. lojas deveriam vender menos aos finais de semana.
        VERDADEIRA. Lojas vendem MENOS aos finais de semana
![Hitótese 11](/img/H11.png "Lojas vendem MENOS aos finais de semana")

6. Modelagem de Dados:
A etapa de proparação dos dados consistiu em aplicar Rescaling para variáveis não Gaussianas, isto é, variáveis sem distribuição normal. Já para a transformação de variáveis categóricas em numéricas mantendo a natureza do conjunto de dados foram utilizados encodings a fim de torná-las mensuráveis.
One hot Encoding para categorização binária (0,1) para cada tipo de resposta positiva da categoria "state_holiday" ser identificada com 1 na label da variável.
Label Encoding para categorização em número aleatório cada tipo de resposta positiva da variável "store_type".
Ordinal Encoding para categorização ordinal de acordo com a graduação da categoria "assortment".
A distribuição das variáveis foi realizada na etapa anterior de análise univariada e como não há variável com distribuição normal, nenhuma das variáveis foi normalizada.
Para seleção de variáveis relevantes para o modelo, foi aplocado método para cálculo de correlação para variáveis numéricas e Cramer's V, uma medida de associação entre duas variáveis categóricas baseada no teste Qui-Quadrado para variáveis categóricas.

Matriz de Correlação - variáveis numéricas

![Matriz de Correlação - variáveis numérica](/img/correlacao.png "Matriz de Correlação")


Cramer's V - variáveis categóricas

![Cramer V - variáveis categórica](/img/cramer_v.png "Cramer's V")


Para o treinamento do modelo foram selecionadas as variáveis independentes (features) mais relevantes pelo método Boruta a fim de obter a melhor acurácia para o modelo.

### Modelo de Machile Learning

O modelo foi treinado na base de dados train.csv e validado na base de teste.csv de mesma estrutura com dados novos.
Foram treinados cinco métodos de modelos: Random Forest Regressor, Average Model, XGBoost Regressor, Linear Regression e Linear Regression - Lasso. Sendo o Average Model (modelo de média) o modelo de referência para performance de comparação dos demais modelos.

#### Single Performance

|         Model Name         |     MAE     |    MAPE   |     RMSE    |
|----------------------------|-------------|-----------|-------------|
| Random Forest Regressor    | 678.546030  | 9.981612  | 1008.892840 |
| Average Model              | 1354.800353 | 45.505116 | 1835.135542 |
| XGBoost Regressor          | 1693.859561 | 25.159246 | 2472.602486 |
| Linear Regression          | 1867.089774 | 29.269403 | 2671.049215 |
| Linear Regression - Lasso  | 1891.704881 | 28.910566 | 2744.451737 |

#### Real Performance - Cross Validation

|         Model Name         |      MAE CV      |    MAPE CV   |      RMSE CV     |
|----------------------------|------------------|--------------|------------------|
| Random Forest Regressor    | 837.21+/-217.56  | 11.61+/-2.31 | 1255.74+/-318.1  |
| XGBoost Regressor          | 1864.01+/-290.82 | 25.51+/-1.33 | 2687.23+/-427.74 |
| Linear Regression          | 2081.73+/-295.63 | 30.26+/-1.66 | 2952.52+/-468.37 |
| Linear Regression - Lasso  | 2116.38+/-341.5  | 29.2+/-1.18  | 3057.75+/-504.26 |

Foi aplicado método de Cross Validation sobre o conjunto de dados train.csv que foi dividido em cinco partes para que o modelo fosse treinado e avaliado repetidamente. Nesse processo a performance real do modelo foi o resultado da média de 5 cortes e desvio padrão do treino e teste. O que fornece uma estimativa mais robusta da capacidade de generalização do modelo.

Após análise dos modelos com menores valores de erro, a Random Forest e o XGBoost foram  osque apresentaram melhores performances. Apesar do Random Forest ter menor erro, optei pelo modelo de XGBoost por sua capacidade de otimização de recursos se comparado ao modelo Random Forest.


### Machine Learning Performance

#### Hyperparameter Fine Tuning

A estratégia para definição do conjunto valores de hiperparâmetros (Hyperparameter Fine Tuning) do modelo escolhido, XGBoots, para maximizar o aprendizado escolhida foi o Random Search. Essa estratégia consiste em testar combinações aleatórias no modelo de forma rápida e exige menor capacidade de processamento se comparado às estratégias Grid Search e Bayesian Search.

Os hiperparâmetros de melhor performance para o XGBoost foram:

|Parâmetro         |Valor|
|------------------|-----|
| n_estimators     |3000 |
| eta              |0.03 |
| max_depth        |5    |
| subsample        |0.7  |
| colsample_bytree |0.7  |
| min_child_weight |3    |


#### Performance do Modelo

O resultado do modelo XGBoot Single Performance com os valores de Fine Tunning foi:
|        Model Name         |      MAE     |     MAPE    |     RMSE    |
|---------------------------|--------------|-------------|-------------|
| XGBoost Regressor         | 776.013223   | 11.621024   | 1122.124425 |

![Performance XGBoost](/img/performance.png "Performance XGBoost")

A análise gráfica demonstram flutuações nas previsão por período, portanto é possível que hajam oscilações em mudanças bruscas de valores.
Já os gráficos inferiores demonstram resultados generalizados em conformidade muito próxima à normal no que tange a distribuição de erros e consequentemente a acertividade da previsão do modelo.

### Resultado de Negócios
O modelo apresenta capacidade de generalização com erro de variação de 776 unidade de vendas em média, o que representa 11,62% para mais ou para menos em relação aos valores reais de venda.

#### Deploy
Hospedado no Render.com.
- `handler.py` — servidor Flask
- `rossmann/` — pipeline de pré-processamento e feature engineering
- `model/model_rossmann.pkl` — modelo treinado

### Conclusões
Pude concluir que para um primeiro ciclo de projeto o modelo tem capacidade de generalização e acertividade muito próxima à normal. Para que seja mais efetivo são necessários testes recorrentes a fim de ajustar os parâmetros do modelo à realidade.