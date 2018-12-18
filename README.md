## Descrição
Programa desenvolido como parte do processo seletivo para estágio em Ciência de Dados.

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