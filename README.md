# Análise de Limite de Crédito

Este projeto tem como objetivo analisar o limite de crédito de diferentes pessoas, destacando fatores como **salário**, **profissão**, **histórico de inadimplência**, e outros, para identificar os principais impulsionadores de limite de crédito elevado.

## Descrição

O código utiliza a biblioteca **Pandas** para manipulação dos dados, **Seaborn** e **Matplotlib** para gerar visualizações gráficas. Ele apresenta três análises principais:

1. **Relação entre Salário e Limite de Crédito**: Um gráfico de dispersão que destaca médicos como uma categoria especial, identificando suas posições no gráfico em relação ao limite de crédito.
   
2. **Média do Limite de Crédito por Profissão**: Um gráfico de barras que compara a média de limite de crédito para diferentes profissões, permitindo uma visão clara de quais profissões têm os maiores limites.

3. **Distribuição do Limite de Crédito por Profissão**: Um boxplot que mostra a variação do limite de crédito dentro de cada profissão, destacando a dispersão dos limites de crédito.

## Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

- **Pandas**
- **Matplotlib**
- **Seaborn**

Você pode instalar as dependências usando o seguinte comando:

```bash
pip install pandas matplotlib seaborn
```

## Uso

1. **DataFrame**: O código começa criando um DataFrame fictício com dados sobre nome, idade, profissão, salário, limite de crédito, histórico de inadimplência, estado civil e imóvel próprio.

2. **Análise Gráfica**:
   - **Gráfico de Dispersão**: Mostra a relação entre o salário e o limite de crédito, destacando os médicos em vermelho. O gráfico também inclui o nome dos médicos ao lado de seus pontos.
   
   - **Gráfico de Barras - Média de Limite de Crédito por Profissão**: Agrupa as pessoas por profissão e mostra a média do limite de crédito em cada categoria.
   
   - **Boxplot - Distribuição de Limite de Crédito por Profissão**: Exibe a distribuição de limite de crédito entre diferentes profissões, visualizando a dispersão dos valores.

## Visualizações

### Gráfico de Dispersão: Relação entre Salário e Limite de Crédito (Médicos Destacados)
Esse gráfico mostra os médicos destacados em vermelho, com seus nomes exibidos, comparando o salário e o limite de crédito de cada pessoa.

### Gráfico de Barras: Média de Limite de Crédito por Profissão
Compara o limite de crédito médio entre profissões, ajudando a identificar as profissões que tendem a ter limites mais altos.

### Boxplot: Distribuição do Limite de Crédito por Profissão
Mostra a variação do limite de crédito dentro de cada profissão, permitindo identificar profissões que têm maior dispersão nos valores de crédito.

## Exemplo de Saída

- Médicos são destacados com maiores limites de crédito.
- Profissões como médicos e engenheiros têm limites de crédito mais altos, em média.
- O histórico de inadimplência e o salário têm impacto direto no limite de crédito.
