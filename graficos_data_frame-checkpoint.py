import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrame
data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}

df = pd.DataFrame(data)
df.head(5)

# Convertendo colunas 'Salário' e 'Limite_Credito' para numérico
df['Salário'] = pd.to_numeric(df['Salário'])
df['Limite_Credito'] = pd.to_numeric(df['Limite_Credito'])

# Definindo uma cor diferente para médicos
colors = ['red' if prof == 'Médico' else 'skyblue' for prof in df['Profissão']]

# Gráfico de Dispersão
plt.figure(figsize=(8, 6))
plt.scatter(df['Salário'], df['Limite_Credito'], color='Skyblue', alpha=0.7)

# Adicionando rótulos para os médicos
for i in range(len(df)):
    if df['Profissão'][i] == 'Médico':
        plt.text(df['Salário'][i], df['Limite_Credito'][i], df['Nome'][i], fontsize=9, ha='right')

# Rótulos e Títulos
plt.title('Relação entre Salário e Limite de Crédito - Médicos Destacados', fontsize=16)
plt.xlabel('Salário', fontsize=12)
plt.ylabel('Limite de Crédito', fontsize=12)

# Mostrando o gráfico
plt.show()

# Agrupando por histórico de inadimplência e calculando a média do limite de crédito
credito_por_inadimplencia = df.groupby('Historico_Inadimplencia')['Limite_Credito'].mean()

# Gráfico de barras
# Agrupando por profissão e calculando a média do limite de crédito
credito_por_profissao = df.groupby('Profissão')['Limite_Credito'].mean()

# Criando gráfico de barras para comparar limite de crédito médio por profissão
plt.figure(figsize=(10, 6))
plt.bar(credito_por_profissao.index, credito_por_profissao, color='lightgreen')

# Adicionando títulos e rótulos
plt.title('Média de Limite de Crédito por Profissão', fontsize=16)
plt.xlabel('Profissão', fontsize=12)
plt.ylabel('Média do Limite de Crédito', fontsize=12)

# Rotacionando os rótulos do eixo x para melhorar a legibilidade
plt.xticks(rotation=45)
plt.show()

# Converter coluna 'Limite_Credito' de string para int
df['Limite_Credito'] = pd.to_numeric(df['Limite_Credito'])

# Gráfico Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Profissão', y='Limite_Credito', data=df)

# Títulos
plt.title('Distribuição do Limite de Crédito por Profissão', fontsize=16)
plt.xlabel('Profissão', fontsize=12)
plt.ylabel('Limite de Crédito', fontsize=12)

# Rotacionando os rótulos no eixo x
plt.xticks(rotation=45)
plt.show()