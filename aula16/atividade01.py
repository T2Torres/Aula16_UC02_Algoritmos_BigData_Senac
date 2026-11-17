import pandas as pd
import numpy as np
import traceback
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Carregando dados
try:
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Delimitando as variáveis 'cisp', 'lesao_corp_dolosa', 'lesao_corp_morte'
    
    df_ocorrencias = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    # Totalizando por delegacias (CISPs) as ocorrências de lesão corporal dolosa e lesão corporal seguida de morte
    
    df_lesao = df_ocorrencias.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()

    # Ordernar pelo maior número de ocorrências de lesão corporal dolosa e lesão corporal seguida de morte
    df_lesao = df_lesao.sort_values(by=['lesao_corp_dolosa', 'lesao_corp_morte'], ascending=False)
    
    print(df_lesao.head(10))


except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    print('\nDetalhes Completos:\n')
    print(traceback.format_exc())


# Calculando a correlação entre as variáveis 'lesao_corp_dolosa' e 'lesao_corp_morte' usando numpy


try:
    correlacao_pearson = np.corrcoef(df_lesao['lesao_corp_dolosa'], df_lesao['lesao_corp_morte'])[0, 1]
    
    print(f"\nCorrelação de Pearson entre lesão corporal dolosa e lesão corporal seguida de morte: {correlacao_pearson:.2f}")

except Exception as e:
    print(f"Erro ao processar os dados: {e}")
    print('\nDetalhes Completos:\n')
    print(traceback.format_exc())


# Plotando gráfico de dispersão
try:
    plt.figure(figsize=(10, 6))
    plt.scatter(df_lesao['lesao_corp_dolosa'], df_lesao['lesao_corp_morte'], color='blue', alpha=0.5)
    plt.title(f'Correlação entre Lesão Corporal Dolosa e Lesão Corporal Seguido de Morte: {correlacao_pearson:.2f}')
    plt.xlabel('Lesão Corporal Dolosa')
    plt.ylabel('Lesão Corporal Seguido de Morte')
    plt.grid(True)
    plt.show()


except Exception as e:
    print(f"Erro ao plotar o gráfico: {e}")
    print('\nDetalhes Completos:\n')
    print(traceback.format_exc())
