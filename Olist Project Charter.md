# Project Charter: Análise Preditiva da Satisfação do Cliente e Eficiência Operacional na Olist

-   **Data de Criação:** 22 de Agosto de 2025
-   **Versão:** 1.0
-   **Equipe do Projeto (Stakeholders):** Fernando Gomes Cruz
-   **Patrocinador (Sponsor):** PCD003 Projeto Integrador III - Curso de Ciência de Dados - Fatec Rubens Lara

#### 1. Justificativa do Projeto (Business Need)

A Olist, como uma importante plataforma de e-commerce no Brasil, opera em um ambiente competitivo onde a experiência do cliente é um diferencial chave. Atrasos na entrega e uma performance logística inconsistente podem levar a avaliações negativas, prejudicar a reputação da marca e, consequentemente, impactar a receita. Este projeto visa utilizar o dataset histórico (2016-2018) para extrair insights estratégicos, simulando como a ciência de dados poderia ter sido usada para otimizar a operação, segmentar clientes e mitigar proativamente os riscos que afetam a satisfação do cliente.

#### 2. Objetivos do Projeto

-   **Objetivo Geral:** Desenvolver uma compreensão profunda do ecossistema da Olist, segmentando clientes para entender seus comportamentos e construindo um modelo preditivo capaz de identificar pedidos com alto risco de atraso na entrega.
-   **Objetivos Específicos:**
    1.  Agrupar a base de clientes em clusters distintos com base no seu comportamento de compra (RFM).
    2.  Analisar e quantificar a relação entre tempo de entrega, tipo de produto e as notas de avaliação (reviews).
    3.  Mapear geograficamente o desempenho das entregas para identificar gargalos logísticos.
    4.  Construir um modelo de Machine Learning para prever a probabilidade de um pedido ser entregue com atraso.

#### 3. Escopo do Projeto

-   **Incluso no Escopo (In-Scope):**
    -   Utilização exclusiva do "Brazilian E-Commerce Public Dataset by Olist" disponível no Kaggle.
    -   Análise de dados cobrindo o período de 2016 a 2018.
    -   Limpeza, pré-processamento e engenharia de features dos dados.
    -   Aplicação do algoritmo K-Means para clusterização de clientes.
    -   Treinamento e avaliação de modelos de classificação (Regressão Logística, Random Forest/XGBoost).
    -   Criação de visualizações de dados (gráficos e mapas) para suportar os insights.

-   **Fora do Escopo (Out-of-Scope):**
    -   Análise de dados externos (dados econômicos, de tráfego, etc.).
    -   Análise de Processamento de Linguagem Natural (NLP) sobre os comentários textuais das avaliações.
    -   Criação de um sistema de previsão em tempo real ou uma aplicação web (API).
    -   Previsão de vendas ou receita futura, dado que o dataset é histórico.

#### 4. Entregáveis Principais

1.  **Código-Fonte:** Jupyter Notebook(s) completos, comentados e reprodutíveis, contendo todo o processo de análise, hospedados em um repositório Git.
2.  **Relatório Técnico:** Documento detalhando a metodologia CRISP-DM, as análises, os resultados dos modelos e as conclusões.
3.  **Apresentação Executiva:** Apresentação em slides com os principais insights, visualizações e recomendações estratégicas, focada em um público de negócios.

#### 5. Critérios de Sucesso

-   **Sucesso Técnico:** O modelo preditivo de atrasos deve atingir um F1-Score na classe "atrasado" igual ou superior a 0.75 no conjunto de teste.
-   **Sucesso de Negócio:** O projeto deve gerar e apresentar pelo menos 3 insights acionáveis claros e baseados em dados, que poderiam levar a melhorias operacionais ou estratégicas para a Olist.

#### 6. Metodologia

O projeto seguirá as seis fases da metodologia **CRISP-DM** (Cross-Industry Standard Process for Data Mining).

#### 7. Pressupostos e Restrições

-   **Pressupostos:**
    *   Os dados do dataset são um reflexo fiel da operação da Olist no período de 2016-2018.
    *   A coluna `customer_unique_id` é uma chave confiável para identificar clientes recorrentes.
-   **Restrições:**
    *   A análise está limitada ao escopo e à granularidade dos dados fornecidos.
    *   O projeto tem um prazo definido pelo cronograma acadêmico.
    *   Não há acesso a especialistas de negócio da Olist para validação das hipóteses.

