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

## 📈 Resultados da Análise

### 📌 Estatísticas Descritivas

**Consumo de Carne (kg/ano per capita)**  
- Média: 41.94  
- Mediana: 32.99  
- Mínimo: 2.21  
- Máximo: 179.95  
- Desvio Padrão: 31.26  

**PIB per Capita (PPC - dólares internacionais)**  
- Média: 21,567.90  
- Mediana: 12,562.89  
- Mínimo: 510.82  
- Máximo: 174,339.08  
- Desvio Padrão: 23,684.14  

### 🔗 Correlação de Pearson

- **Coeficiente de Correlação (r)**: `0.698`  
- **Valor-p**: `0.0000`  
- **Interpretação**: Correlação positiva moderadamente forte entre PIB e consumo de carne.

### 📉 Regressão Linear

Modelo de regressão linear simples:

- **Equação estimada**:  
  `Consumo de Carne ≈ 26.87 + 0.000986 × PIB per Capita`
- **Intercepto (α)**: 26.87  
- **Coeficiente Angular (β)**: 0.000986  
- **Coeficiente de Determinação (R²)**: 0.487  

### 🧪 Teste de Hipótese

- **H₀**: Não há correlação entre consumo de carne e PIB per capita (ρ = 0)  
- **H₁**: Há correlação positiva entre as variáveis (ρ > 0)  
- **Valor-p**: `0.0000000000`

**Conclusão**:  
> Rejeitamos a hipótese nula com 99% de confiança.  
> Há evidências estatísticas de uma **correlação positiva significativa** entre PIB per capita e consumo de carne.

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/consumo-carne-vs-pib.git
   cd consumo-carne-vs-pib
   
2. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   
3. Execute o script:
   python analise_consumo_pib.py
