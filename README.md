Repositório destinado aos códigos e arquivos referente ao processo seletivo (dividido em duas etapaas) para estágio em Ciência de Dados.

# Etapa 1

## Descrição
Este programa recebe um arquivo de anúncios de produtos como entrada e classifica cada um dos produtos como sendo "smartphone" ou "não-smartphone", a saída do programa é o arquivo "produtos_classificados.csv" que contém os dados do arquivo de entrada e a coluna referente a classe do produto.

## Pré-requisitos
* [python 3](https://www.python.org/download/releases/3.0/)
* [unidecode](https://docs.python.org/3/howto/unicode.html)

## Execução
Para executar o programa, basta passar o diretório do arquivo de anúncios como parâmetro na execução, caso o diretório não seja informado, o programa irá assumir que o arquivo de anúncios está no diretório raiz da execução com o nome de "data_estag_ds.tsv"
Exemplos de execução:
```bash
$ python3 psel_ds.py data_estag_ds.tsv
```
ou
```bash
$ python3 psel_ds.py
```

# Etapa 2

## Descrição
Todos ss títulos de anúncios utilizados nessa etapa (com excessão dos que foram fornecidos) foram crawleados no site [buscapé](https://www.buscape.com.br/), os cógigos produzidos estão divididos em três arquivos: 

* [smart_spider.py](etapa_2/crawler_prod/crawler_prod/spiders/smart_spider.py) - Responsável por crawlear todos os anuncios de ofertas de smartphones do site [buscapé](https://www.buscape.com.br/), os anúncios estão disponíveis no arquivo [smartphones.json](etapa_2/data/smartphones.json).
* [not_smart_spider.py](etapa_2/crawler_prod/crawler_prod/spiders/not_smart_spider.py) - Responsável por crawlear os anuncios de ofertas de não smartphones, os anúncios estão disponíveis no arquivo [nao_smartphones.json](etapa_2/data/nao_smartphones.json). É válido destacar que esse crawler percorre o mapa do site, crawleando uma página de cada tipo de produto, com excessão dos acessórios de smartphone que são crawleados até a última página.
* [etapa_2.ipynb](etapa_2/etapa_2.ipynb) - Jupyter notebook que contém todos os códigos solicitados na tarefa, para uma melhor visualização recomendo que seja visualizado clicando [aqui](https://colab.research.google.com/drive/1h4XN05ONt32LrkzFvb_sq8l2bon6_cDT).

Os arquivos gerados pelo notebook também são três:
* [produtos_classificados.csv](etapa_2/out/produtos_classificados.csv) - CSV que contém o id, título e categoria (smartphone ou não-smartphone) de todos os anúncios do arquivo de entrada ([data_estag_ds.tsv](etapa_2/data/data_estag_ds.tsv)).
* [smartphones_atributos.csv](etapa_2/out/smartphones_atributos.csv) - CSV que contém o id, título, marca, ram (quantidade), tela (tamanho) e cor dos smartphones do arquivo de entrada.
* [smartphones_duplicados.csv](etapa_2/out/smartphones_duplicados.csv) - CSV que contém os smartphones que foram considerados duplicados do arquivo de entrada, os campos são dividios em 'ID 1' e 'ID 2' (id's dos smartphones), 'TITLE 1' e 'TITLE 2' (títulos dos smartphones), 'Similaridade' (similaridade entre os títulos), 'Especificações iguais' (especificações em comum nos smartphones) e 'Especificações diferentes' (especificações que são distintas nos aparelhos 1 e 2 respectivamente).

## Pré-requisitos
* [python 3](https://www.python.org/download/releases/3.0/)
* [unidecode](https://docs.python.org/3/howto/unicode.html)
* [scrapy](https://scrapy.org/)
* [jupyter](https://jupyter.org/)