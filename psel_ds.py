
# coding: utf-8

# In[200]:


import pandas as pd
import sys


# In[201]:


# tenta ler o arquivo de produtos pelo primeiro parâmetro do terminal
# se não conseguir tenta abrir com o nome 'data_estag_ds.tsv'

try:
    path = sys.argv[1]
    data = pd.read_csv(path, sep='\t')
except Exception as e:
    try:
        data = pd.read_csv('data_estag_ds.tsv', sep='\t')
    except:
        print('Erro ao abrir arquivo: ', e)
        sys.exit()


# In[202]:


# insere a coluna CLASSE que futuramente será preenchida com o rótulo 'smartphone' ou 'não-smartphone' 
data.insert(data.shape[1], 'CLASSE', '')


# In[203]:


from unidecode import unidecode

# Função que classifica um produto em 'smartphone' ou 'não-smartphone' com base em seu anúncio
# Parâmetros:
# * prod:      <str>         Anúncio do produto
# * kw_smart:  <list of str> Lista das palavras chave que um smartphone possívelmente contém
# * kw_nsmart: <list of str> Lista das palavras chave que um não smartphone possívelmente contém
# Retorno:
# * Retorna uma string que representa a classe do produto, 'smartphone' ou 'não-smartphone'
def classifica(prod, kw_smart, kw_nsmart):
    
    # substitui caracteres especiais e deixa em lowercase (o anuncio do produto)
    prod = unidecode( prod.lower() )
    
    # testa se o anuncio do produto contem alguma das palavras de um não smartphone
    if True in [kw in prod for kw in key_nsmart]:
        return 'não-smartphone'
    
    # testa se o anuncio do produto contem alguma das palavras de um smartphone
    elif True in [kw in prod for kw in key_smart]:
        return 'smartphone'
    
    # se não for smartphone, será não smartphone
    else:
        return 'não-smartphone'


# In[204]:


# lista das palavras chave que o anúncio de um não smartphone possívelmente contém
key_nsmart = ['capa',
             'capinha',
             'case',
             'pelicula',
             'acessorio',
             'tablet',
             'tab ',
             'relogio',
             'smartwatch',
             'bumper',
             'bumber',
             'protetores',
             'protetor',
             'suporte',
             'kit',
             'cabo',
             'bracadeira',
             'ipad',
             'adesivo',
             'lentes',
             'lente',
             'carregador',
             'repetidor',
             'espelhamento',
             'mirror',
             'antena',
             'watch',
             'interface']


# In[205]:


# lista das palavras chave que o anúncio de um smartphone possívelmente contém
key_smart = ['smartphone', 
              'celular', 
              'iphone', 
              'galaxy', 
              'samsung a', 
              'samsung j', 
              'moto ', 
              'xperia', 
              'zenfone', 
              'lg k', 
              'xiaomi mi', 
              'rom global', 
              'xiaomi redmi', 
              'oneplus', 
              'caterpillar cat', 
              'motorola nextel']


# In[207]:


# aplica a classificação a todas as instâncias e armazena na coluna 'classe'
data['CLASSE'] = data['TITLE'].apply(lambda x: classifica(x, key_smart, key_nsmart) )

# salva em csv os produtos e sua respectiva classe
data.to_csv("produtos_classificados.csv", index=False)

