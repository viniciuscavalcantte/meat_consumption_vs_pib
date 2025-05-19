# 📊 Consumo de Carne vs PIB per Capita

Este projeto analisa a relação entre o **consumo de carne per capita** e o **PIB per capita (PPC)** de diferentes países. Utilizando ferramentas de análise estatística e visualização de dados, buscamos entender se há uma correlação entre o poder econômico de um país e o consumo de carne de sua população.

## 📁 Sobre o Dataset

- **Fonte**: Our World in Data
- **Arquivo**: `meat-consumption-vs-gdp-per-capita.csv`
- Contém dados sobre:
  - Consumo de carne per capita (kg/ano)
  - PIB per capita ajustado pela paridade do poder de compra (PPC)

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Bibliotecas:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scipy.stats`
  - `sklearn.linear_model`

## 📌 Objetivos da Análise

1. **Estatísticas Descritivas**  
   Obter uma visão geral dos dados de consumo de carne e PIB per capita.

2. **Análise Gráfica**  
   Visualizar distribuições e padrões com histogramas e gráficos de dispersão.

3. **Correlação de Pearson**  
   Medir a força e a direção da relação linear entre as variáveis.

4. **Regressão Linear Simples**  
   Estimar o impacto do PIB per capita no consumo de carne.

5. **Teste de Hipótese**  
   Verificar se a correlação observada é estatisticamente significativa.

## 📈 Resultados

- **Correlação** entre PIB e consumo de carne: `r ≈ 0.XX` (valor exato depende dos dados)
- **Regressão Linear**:
  - Intercepto (α): `...`
  - Coeficiente (β): `...`
  - R²: `...`
- **Valor-p** da correlação: `...`
- **Conclusão**: (depende do p-valor — ex.: há evidência de correlação positiva com 99% de confiança)

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/consumo-carne-vs-pib.git
   cd consumo-carne-vs-pib
