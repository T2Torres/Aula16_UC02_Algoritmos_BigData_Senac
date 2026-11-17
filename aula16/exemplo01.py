import pandas as pd
import numpy as np
import traceback
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Carregando dados
try:
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    
    # Delimitando as variáveis 'cisp', 'roubo_veiculo', 'recuperacao_veiculos'
    df_ocorrencias = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # Agrupar as ocorrências por 'cisp' e somar os valores de 'roubo_veiculo' e 'recuperacao_veiculos'
    df_total_veiculos = df_ocorrencias.groupby('cisp').agg({'roubo_veiculo': 'sum', 'recuperacao_veiculos': 'sum'}).reset_index()
    
    
    
    
    print(df_total_veiculos.head(10))  

except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    print('\nDetalhes Completos:\n')
    print(traceback.format_exc())



# Obtendo a correlação de pearson usando numpy
try:
    # Calculando a correlação de Pearson entre 'roubo_veiculo' e 'recuperacao_veiculos'
    correlacao_pearson = np.corrcoef(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])[0,1]
    
    print(f"\nCorrelação de Pearson entre roubo de veículos e recuperação de veículos: {correlacao_pearson:.2f}")

except Exception as e:
    print(f"Erro ao processar os dados: {e}")
    print('\nDetalhes Completos:\n')
    print(traceback.format_exc())


# Plotando a correlação
    
try:
    # PLOTANDO GRÁFICO DE DISPERSÃO
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'], color='blue', alpha=0.5)
    plt.title(f'Correlação entre Roubo de Veículos e Recuperação de Veículos: {correlacao_pearson:.2f}')
    plt.xlabel('Roubo de Veículos')
    plt.ylabel('Recuperação de Veículos')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Erro ao plotar o gráfico: {e}")
    print('\nDetalhes Completos:\n')
    print(traceback.format_exc())