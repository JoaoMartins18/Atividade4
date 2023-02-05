import pandas as pd
from scipy import stats


data2021 = pd.read_csv('licitacoes-2021.csv', sep=',',
                       on_bad_lines='skip', low_memory=False)

data2022 = pd.read_csv('licitacoes-2022.csv', sep=',',
                       on_bad_lines='skip', low_memory=False)


data2021.dropna(subset=['VALORESTIMADO'], inplace=True)
data2022.dropna(subset=['VALORESTIMADO'], inplace=True)

data2021.dropna(subset=['SITUACAOLICITACAO'], inplace=True)
data2022.dropna(subset=['SITUACAOLICITACAO'], inplace=True)

# Valores totais

soma2021 = data2021["VALORESTIMADO"].sum()
soma2022 = data2022["VALORESTIMADO"].sum()

# Médias

media2021 = data2021['VALORESTIMADO'].mean()
media2022 = data2022['VALORESTIMADO'].mean()

# Maiores e Menores

valor_maximo2021 = data2021['VALORESTIMADO'].max()
valor_minimo2021 = data2021['VALORESTIMADO'].min()

valor_maximo2022 = data2022['VALORESTIMADO'].max()
valor_minimo2022 = data2022['VALORESTIMADO'].min()

# Variância

variancia2021 = data2021["VALORESTIMADO"].var()
variancia2022 = data2022["VALORESTIMADO"].var()

# Desvio Padrão

desvio_padrao2021 = data2021["VALORESTIMADO"].std()
desvio_padrao2022 = data2022["VALORESTIMADO"].std()

# Licitações Concluídas

concluidos2021 = (data2021['SITUACAOLICITACAO'] == "Concluído").sum()
concluidos2022 = (data2022['SITUACAOLICITACAO'] == "Concluído").sum()

# Teste T

t_stat, p_value = stats.ttest_ind(
    data2022['VALORESTIMADO'], data2021['VALORESTIMADO'], equal_var=False)


# Impressão - Valores totais

print("\n__________ VALORES TOTAIS DAS LICITAÇÕES __________\n")
print(f"Gasto total em Licitações no ano de 2021: R$ {round(soma2021,2)}")
print(f"Gasto total em Licitações no ano de 2022: R$ {round(soma2022,2)}")

if(soma2022 > soma2021):
    percentual_soma = ((soma2022 / soma2021) - 1) * 100
    print(f"\nO valor total em 2022 corresponde a um aumento de {round(percentual_soma,2)} % comparado com o ano de 2021.")

# Sei que essa condição não irá ser satisfeita, mas apenas automatizei para demonstrar que posso fazer essa análise também.
elif(soma2022 < soma2021):
    percentual_soma = ( (soma2022-soma2021) / soma2021 ) * (-100) 
    print(f"\nO valor total em 2022 corresponde a uma redução de {round(percentual_soma,2)} % comparado com o ano de 2021.")

# Impressão - Médias

print("\n__________ MÉDIAS DOS VALORES DAS LICITAÇÕES __________\n")
print(f"Média do ano de 2021: R$ {round(media2021,2)}")
print(f"Média do ano de 2022: R$ {round(media2022,2)}")

if(media2022 > media2021):
    percentual_media = ((media2022 / media2021) - 1) * 100
    print(f"\nA média em 2022 é {round(percentual_media,2)} % maior que a do ano de 2021.")

# Sei que essa condição não irá ser satisfeita, mas apenas automatizei para demonstrar que posso fazer essa análise também.
elif(media2022 < media2021):
    percentual_media = ( (media2022-media2021) / media2021 ) * (-100) 
    print(f"\n A média em 2022 é {round(percentual_media,2)} % menor que a do ano de 2021.")

# Impressão - Maiores e Menores

print("\n__________ MÁXIMOS E MÍNIMOS DOS VALORES DAS LICITAÇÕES __________\n")
print(f"MAIOR valor de 2021: R$ {round(valor_maximo2021,2)}")
print(f"MENOR valor de 2021: R$ {round(valor_minimo2021,2)}")
print(f"MAIOR valor de 2022: R$ {round(valor_maximo2022,2)}")
print(f"MENOR valor de 2022: R$ {round(valor_minimo2022,2)}")

if(valor_maximo2022 > valor_maximo2021):
    print(f"\nO maior valor de uma única licitação foi no ano de 2022, com um valor de R$ {round(valor_maximo2022,2)}")

elif(valor_maximo2022 < valor_maximo2021):
    maior = valor_maximo2021
    print(f"\nO maior valor de uma única licitação foi no ano de 2021, com um valor de R$ {round(valor_maximo2021,2)}")

if(valor_minimo2022 < valor_minimo2021):
    print(f"O menor valor de uma única licitação foi no ano de 2022, com um valor de R$ {round(valor_minimo2022,2)}")

elif(valor_minimo2022 > valor_minimo2021):
    print(f"O menor valor de uma única licitação foi no ano de 2021, com um valor de R$ {round(valor_minimo2021,2)}")

# Impressão - Variância

print("\n__________ VARIÂNCIA DOS VALORES DAS LICITAÇÕES __________\n")
print(f"Variância do ano de 2021: {variancia2021}")
print(f"Variância do ano de 2022: {variancia2022}")

if(variancia2022 > variancia2021):
    print("\nA maior variância corresponde ao ano de 2022.")

elif(variancia2022 < variancia2021):
    print("\nA maior variância corresponde ao ano de 2021.")

# Impressão - Desvio Padrão

print("\n__________ DESVIO PADRÃO DOS VALORES DAS LICITAÇÕES __________\n")
print(f"Desvio Padrão do ano de 2021: {desvio_padrao2021}")
print(f"Desvio Padrão do ano de 2022: {desvio_padrao2022}")

if(desvio_padrao2022 > desvio_padrao2021):
    print("\nO maior Desvio Padrão corresponde ao ano de 2022.")

elif(desvio_padrao2022 < desvio_padrao2021):
    print("\nO maior Desvio Padrão corresponde ao ano de 2021.")

# Impressão - Licitações Concluídas

print("\n__________ NÚMERO DE LICITAÇÕES CONCLUÍDAS __________\n")
print(f"Número de licitações concluídas no ano de 2021: {int(concluidos2021)}")
print(f"Número de licitações concluídas no ano de 2022: {int(concluidos2022)}")

if(concluidos2022 > concluidos2021):
    print("\nO ano de 2022 obteve o maior número de licitações concluídas.")

elif(concluidos2022 < concluidos2021):
    print("\nO ano de 2021 obteve o maior número de licitações concluídas.")

# Impressão - Teste T

print("\n__________ TESTE T (VALORES DAS LICITAÇÕES DE 2021 E 2022) __________\n")
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")
