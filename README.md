# Rossmann Project

## Previsão de vendas em Projeto Rossmann
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
Seleção de dados disponibilizados em 3 bases em formato csv (train.csv, test.csv e store.csv) no site Kaggle. Rossmann Store Sales. Disponível em:<https://www.kaggle.com/competitions/rossmann-store-sales/data>. Acesso em: 25 mai. 2026.

4. Limpeza de dados:
Foram realizadas limpeza e tratamento dos dados; remoção dos dados dos dias em que as lojas foram fechadadas; remoção de lojas cujas vendas fossem zero; inclusão de maior distância observada no conjunto de dados para as lojas que não sem informações no campo "Competition Distance" para efeito de cálculos posteriores e remoção da coluna “customers” pois não seria relevante para o dimensão analítica do trabalho atual.

5. Exploração de dados:
Foi realizada padronização do formato dos títulos das variáveis, formatação do tipos e grandezas dos campos de análise, tratamento ou remoção de campos vazios, análise descritiva exploratória para identificar cenário inicial e volume de dados, seleção de atributos numéricos e categórios para análise posterior e desenvolvimento de mapa mental de hipóteses a serem validadas ou refutadas posteriormente.

![mind_map](/img/MindmapHypothesis.png "Mind Map")

#### 13 Hipóteses validadas:
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

Com a exploração de dados é possível identificar insights e selecionar variáveis relevantes através de análises univariadas, biváriadas e multivariadas para seleção das variáveis numéricas e categóricas do conjunto.
Para seleção das variáveis numéricas foi realizado o Gráfico de Correlação e para seleção das variáveis categóricas foram analizadas Matriz de Confusão e Qui-quadrado (Cramer's V) para verificar se existe associação entre variáveis categóricas.

6. Modelagem de dados:
7. Algoritmo de Machine Learning:
8. Avaliação do açgoritmo:
9. Modelo em produção:


### Top 3 Insights

H1. Lojas com maior sortimentos deveriam vender mais.
FALSA. Lojas com MAIOR SORTIMENTO vendem MENOS.

H2. Lojas com competidores mais proximos deverima vender menos.
FALSA. Lojas com competidores MAIS PROXIMOS vendem MAIS

H11. lojas deveriam vender menos aos finais de semana.
VERDADEIRA. Lojas vendem MENOS aos finais de semana

### Modelo de Machile Learning

### Machine Learning Performance

### Resultado de Negócios

#### Deploy
Hospedado no Render.com.
- `handler.py` — servidor Flask
- `rossmann/` — pipeline de pré-processamento e feature engineering
- `model/model_rossmann.pkl` — modelo treinado

### Conclusões
