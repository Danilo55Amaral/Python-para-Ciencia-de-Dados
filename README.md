# Python para Data Science 

Anotações sobre Python para Ciência de Dados do curso Formação Cientista de Dados do professor Fernando Amaral.
Aqui estão algumas anotações que fiz a respeito de bibliotecas como NumPy e Pandas utilizadas em Ciência de Dados.

## NumPy 

NumPy significa Python Numérico, é uma biblioteca de código aberto do Python que é muito utilizada em 
todos os campos da ciência de engenharias, é bastante utilizada também em Ciência de Dados.
A API do NumPy é bastante utilizada com o Pandas, Matplotlib, scikit-image, scikit-learn e em quase todos 
os pacotes utilizados em Ciência de Dados.

O NumPy trabalha utilizando estruturas de dados de Matriz e arrays multidimensionais, essa biblioteca pode 
ser utilizada para realizar várias operações matemáticas utilizando arrays, contém uma grande variedade de
funções matemáticas de alto nível capazes de operarem em arrays e matrizes.

Veja alguns exemplos práticos utilizando o NumPay rodando em ambiente do JupyterLab.

Importando a biblioteca NumPy e criando uma matriz unidimensional.

![numpy-01.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/numpy-01.PNG)

Gerando valores aleatórios, utilizados em processos com uso de aleatoriedade, processos não deterministicos.
Utiliza-se a criação de uma semente, é possível armazenar valores aleatórios nessas sementes e fazer o seu 
reuso.

![numpy-02.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/numpy-02.PNG)

Gerando uma matriz a partir de um teste lógico.

![numpy-03.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/numpy-03.PNG)

## Pandas

Pandas é uma biblioteca Python criada para análise de dados, é uma biblioteca amplamente utilizada 
em Ciência de Dados sendo assim possível fazer análise, Limpeza e tratadamento de dados. 
A biblioteca Pandas tem como principal objetivo a manipulação de conjuntos de dados, editar, excluir
substituir dados de um objeto  da classe DataFrame. 

O Pandas possue várias funções que ajudam nessas análises e manipulações dos dados, Veja alguns exemplos 
práticos utilizando o Pandas rodando em ambiente do JupyterLab.

Resumo estatístico de colunas numéricas, para isso utilizamos o método describe, temos as  informações nas colunas 
e os resumos, count = quantidade, mean = média, std = Desvio padrão, min = mínimo, 25% 50% 75% = cortes, max = máximo.

![pandas01.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/pandas01.PNG)

Séries, única coluna pode ser criada a partir de listas, array do numpy ou coluna de data frame.

![pandas02.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/pandas02.PNG)

verificando dados nulos, esse método vai verificar se existem dados nulos, é bastante utilizado em 
limpeza de dados. O método isnull verifica se existem dados Nulos, ele vai retornar uma tabela 
com dados lógicos informando True onde exixtir algum valor nulo.

![pandas03.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/pandas03.PNG)

Porém essa saída a cima pode não ser tão funcional se tivermos uma grande quantidade de dados
e para resolver isso podemos utilizar também o método sum, Note que no retorno ele vai mostrar que 
de todas as colunas nenhuma possue dados Nulos.

![pandas04.PNG](https://github.com/Danilo55Amaral/Python-para-Ciencia-de-Dados/blob/main/pandas04.PNG)