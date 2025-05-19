import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregar os dados
df = pd.read_csv('meat-consumption-vs-gdp-per-capita.csv')

# Renomear colunas para facilitar
df = df.rename(columns={
    'meat__total__00002943__food_available_for_consumption__0645pc__kilograms_per_year_per_capita': 'meat_consumption',
    'ny_gdp_pcap_pp_kd': 'gdp_per_capita'
})

# 1. Estatísticas Descritivas
print("\n=== Estatísticas Descritivas do Consumo de Carne ===")
print(df['meat_consumption'].describe())

print("\n=== Estatísticas Descritivas do PIB per Capita ===")
print(df['gdp_per_capita'].describe())

# 2. Análise Gráfica
plt.figure(figsize=(12, 6))

# Histograma do consumo de carne
plt.subplot(1, 2, 1)
sns.histplot(df['meat_consumption'].dropna(), bins=30, kde=True)
plt.title('Distribuição do Consumo de Carne')
plt.xlabel('kg/ano per capita')

# Histograma do PIB per capita
plt.subplot(1, 2, 2)
sns.histplot(df['gdp_per_capita'].dropna(), bins=30, kde=True)
plt.title('Distribuição do PIB per Capita')
plt.xlabel('Dólares internacionais')

plt.tight_layout()
plt.show()

# 3. Análise de Correlação
# Filtrar apenas linhas com ambos os valores disponíveis
df_complete = df.dropna(subset=['meat_consumption', 'gdp_per_capita'])

# Calcular correlação
corr, p_value = stats.pearsonr(df_complete['gdp_per_capita'], df_complete['meat_consumption'])
print(f"\nCorrelação entre PIB e Consumo de Carne: {corr:.3f}")
print(f"Valor-p: {p_value:.4f}")

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_complete, x='gdp_per_capita', y='meat_consumption', alpha=0.6)
plt.title('Relação entre PIB per Capita e Consumo de Carne')
plt.xlabel('PIB per Capita (PPC)')
plt.ylabel('Consumo de Carne (kg/ano)')

# Adicionar linha de tendência
sns.regplot(data=df_complete, x='gdp_per_capita', y='meat_consumption', 
            scatter=False, color='red', line_kws={'linestyle':'--'})

plt.show()

# 4. Regressão Linear
from sklearn.linear_model import LinearRegression

# Preparar dados
X = df_complete['gdp_per_capita'].values.reshape(-1, 1)
y = df_complete['meat_consumption'].values

# Modelo de regressão
model = LinearRegression()
model.fit(X, y)

# Coeficientes
print(f"\n=== Resultados da Regressão ===")
print(f"Intercepto (α): {model.intercept_:.2f}")
print(f"Coeficiente (β): {model.coef_[0]:.6f}")
print(f"R²: {model.score(X, y):.3f}")

# 5. Teste de Hipótese
print("\n=== Teste de Hipótese ===")
print("H₀: Não há correlação entre consumo de carne e PIB per capita (ρ = 0)")
print("H₁: Há correlação positiva entre as variáveis (ρ > 0)")
print(f"Valor-p: {p_value:.10f}")

if p_value < 0.01:
    print("\nConclusão: Rejeitamos a hipótese nula com 99% de confiança.")
    print("Há evidências estatísticas de uma correlação positiva significativa.")
else:
    print("\nConclusão: Não podemos rejeitar a hipótese nula.")