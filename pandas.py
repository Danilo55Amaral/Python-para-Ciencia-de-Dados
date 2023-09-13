# Pandas 

# O Pandas também é uma biblioteca que é muito utilizada em Ciência de Dados
# Permite tratar dados tabulares e esses dados podem ser de tipos diferentes
# em diferentes colunas. Dados tabulares são dados em forma de linhas e colunas
# são semelhantes a uma planilha, o Pandas vai tratar esse tipo de dado. 
# Esse tipo de estrutura de Dados é a estrutura de dados mais comum em Ciência de Dados.
# O Pandas permite tratar dados com difentes colunas com diferentes tipos de dados.

# O Pandas tem dois objetos principais:

# DATA FRAME ==> Como uma tabela de um banco de dados. 
# SERIES ==> São dados em série, como uma coluna de um Data Frame.

# O Pandas possue métodos para importar e tratar, manipular esses dados
# de uma forma mais eficiente.

# Exemplificando na prática

# Importação da biblioteca Pandas.
import pandas as pd 

# Aqui vamos importar sempre um arquivo que é um arquivo de Dados, note que é um arquivo 
# csv que é um formato muito utilizado, é um arquivo do tipo texto.
# É necessário importar esse arquivo por que quando trabalhamos com o Pandas iportamos Dados.

## Criando um DataFrame 

# Carregando um arquivo para a criação de um dataframe Pandas / Foi colocado apenas o nome do arquivo por que estou 
# trabalhando com os arquivos que foram copiados diretamente para a pasta do Jubpter, caso contrário 
# seria necessário indicar todo o caimnho na importação dos dados. Foi utilizado o método read_csv que 
# ler o arquivo do tipo csv, então ele cria um arquivo como objeto Pandas e armazena nessa váriável chamada dados 
# que eu criei.
dados = pd.read_csv("Credit.csv") 
# formato, o método shape vai mostrar a estrutura do arquivo de Dados, como pdemos ver nessa saída esse 
# DataFrame possue 1000 linhas e 21 colunas.
dados.shape
# (1000, 21)


## Resumo Estatístico
# Resumo estatístico de colunas numéricas, para isso utilizamos o método describe, temos as  informações nas colunas 
# e os resumos, count = quantidade, mean = média, std = Desvio padrão, min = mínimo, 25% 50% 75% = cortes, max = máximo.
dados.describe()
# 	duration	credit_amount	installment_commitment	residence_since	age	existing_credits	num_dependents
# count	1000.000000	1000.000000	1000.000000	1000.000000	1000.000000	1000.000000	1000.000000
# mean	20.903000	3271.258000	2.973000	2.845000	35.546000	1.407000	1.155000
# std	12.058814	2822.736876	1.118715	1.103718	11.375469	0.577654	0.362086
# min	4.000000	250.000000	1.000000	1.000000	19.000000	1.000000	1.000000
# 25%	12.000000	1365.500000	2.000000	2.000000	27.000000	1.000000	1.000000
# 50%	18.000000	2319.500000	3.000000	3.000000	33.000000	1.000000	1.000000
# 75%	24.000000	3972.250000	4.000000	4.000000	42.000000	2.000000	1.000000
# max	72.000000	18424.000000	4.000000	4.000000	75.000000	4.000000	2.000000


## Buscando Primeiros Registros
# Primeiros registros, o método head permite visualizar os dados por completo dos 5 primeiros registros. 
# Diferente do describe que são apenas resumos estatísticos.
dados.head()
# 	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 0	<0	6	'critical/other existing credit'	radio/tv	1169	'no known savings'	>=7	4	'male single'	none	...	'real estate'	67	none	own	2	skilled	1	yes	yes	good
# 1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
# 2	'no checking'	12	'critical/other existing credit'	education	2096	<100	4<=X<7	2	'male single'	none	...	'real estate'	49	none	own	1	'unskilled resident'	2	none	yes	good
# 3	<0	42	'existing paid'	furniture/equipment	7882	<100	4<=X<7	2	'male single'	guarantor	...	'life insurance'	45	none	'for free'	1	skilled	2	none	yes	good
# 4	<0	24	'delayed previously'	'new car'	4870	<100	1<=X<4	3	'male single'	none	...	'no known property'	53	none	'for free'	2	skilled	2	none	yes	bad


## Buscando Ultimos Registros
# Últimos registros, com parâmetros, funciona como o head porém com os ultimos registros, e posso passar um valor 
# como paramtro de quantas linhas quero que sejam exibidas, esses parâmtros também funcionam no head.
dados.tail(2)
# 	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 998	<0	45	'existing paid'	radio/tv	1845	<100	1<=X<4	4	'male single'	none	...	'no known property'	23	none	'for free'	1	skilled	1	yes	yes	bad
# 999	0<=X<200	45	'critical/other existing credit'	'used car'	4576	100<=X<500	unemployed	3	'male single'	none	...	car	27	none	own	1	skilled	1	none	yes	good


## Filtrando por Coluna
# Filtrando por nome da coluna, basta passar o nome da coluna que quero que seja exibida passando colchetes duas vezes.
dados[["duration"]] 
# 	duration
# 0	6
# 1	48
# 2	12
# 3	42
# 4	24
# ...	...
# 995	12
# 996	30
# 997	12
# 998	45
# 999	45
# 1000 rows × 1 columns


## Filtrando Linhas por Índice
# Filtrando linhas por indice, é possivel fazer isso utilizando o método loc, aqui nesse exemplo estou filtrando 
# das linhas de 1 até a 3. Lembre que ele vai ignorar o ultimo valor do intervalo.
dados.loc[1:3]
# 	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
# 2	'no checking'	12	'critical/other existing credit'	education	2096	<100	4<=X<7	2	'male single'	none	...	'real estate'	49	none	own	1	'unskilled resident'	2	none	yes	good
# 3	<0	42	'existing paid'	furniture/equipment	7882	<100	4<=X<7	2	'male single'	guarantor	...	'life insurance'	45	none	'for free'	1	skilled	2	none	yes	good
# 3 rows × 21 columns


## Filtrando com Lista 
# Linhas 1 e 3, utilizando o mesmo método loc porém passando dois colchetes, esse segundo colchete informa que quero uma lista de valores 
# com as colunas informadas, no exemplo ele vai retornar uma lista com as colunas 1 e 3.
dados.loc[[1,3]]
# 	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
# 3	<0	42	'existing paid'	furniture/equipment	7882	<100	4<=X<7	2	'male single'	guarantor	...	'life insurance'	45	none	'for free'	1	skilled	2	none	yes	good


## Filtro com condição
# Filtro, aqui eu continuo utilizando o método loc para filtrar dados, no colchetes eu passo uma condição 
# que em dados a coluna purpose seja igual radio/tv, com  isso ele vai mostrar apenas as que essa condição 
# for verdadeira.
dados.loc[dados['purpose'] == "radio/tv"]
# 	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 0	<0	6	'critical/other existing credit'	radio/tv	1169	'no known savings'	>=7	4	'male single'	none	...	'real estate'	67	none	own	2	skilled	1	yes	yes	good
# 1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
# 8	'no checking'	12	'existing paid'	radio/tv	3059	>=1000	4<=X<7	2	'male div/sep'	none	...	'real estate'	61	none	own	1	'unskilled resident'	1	none	yes	good
# 12	0<=X<200	12	'existing paid'	radio/tv	1567	<100	1<=X<4	1	'female div/dep/mar'	none	...	car	22	none	own	1	skilled	1	yes	yes	good
# 15	<0	24	'existing paid'	radio/tv	1282	100<=X<500	1<=X<4	4	'female div/dep/mar'	none	...	car	32	none	own	1	'unskilled resident'	1	none	yes	bad
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 989	0<=X<200	24	'critical/other existing credit'	radio/tv	1743	<100	>=7	4	'male single'	none	...	'life insurance'	48	none	own	2	'unskilled resident'	1	none	yes	good
# 991	'no checking'	15	'all paid'	radio/tv	1569	100<=X<500	>=7	4	'male single'	none	...	car	34	bank	own	1	'unskilled resident'	2	none	yes	good
# 992	<0	18	'existing paid'	radio/tv	1936	'no known savings'	4<=X<7	2	'male mar/wid'	none	...	car	23	none	rent	2	'unskilled resident'	1	none	yes	good
# 997	'no checking'	12	'existing paid'	radio/tv	804	<100	>=7	4	'male single'	none	...	car	38	none	own	1	skilled	1	none	yes	good
# 998	<0	45	'existing paid'	radio/tv	1845	<100	1<=X<4	4	'male single'	none	...	'no known property'	23	none	'for free'	1	skilled	1	yes	yes	bad
# 280 rows × 21 columns


## Filtro com Condição
# Outra condição onde a coluna informada o valor tem que ser maior que 18000
dados.loc[dados['credit_amount'] >  18000]
# 	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 915	0<=X<200	48	'no credits/all paid'	other	18424	<100	1<=X<4	1	'female div/dep/mar'	none	...	'life insurance'	32	bank	own	1	'high qualif/self emp/mgmt'	1	yes	no	bad
# 1 rows × 21 columns


## Gerando outro DataFrame
## Podemos gerar outro DataFrame a partir do resultado desse filtro que foi utilizado no exemplo a cima
# atribuímos o resultado a variável, criando outro df
credito2 = dados.loc[dados['credit_amount'] >  18000]
print(credito2)
#     checking_status  duration         credit_history purpose  credit_amount  \
# 915        0<=X<200        48  'no credits/all paid'   other          18424   

#     savings_status employment  installment_commitment       personal_status  \
# 915           <100     1<=X<4                       1  'female div/dep/mar'   

#     other_parties  ...  property_magnitude age  other_payment_plans housing  \
# 915          none  ...    'life insurance'  32                 bank     own   

#     existing_credits                          job num_dependents  \
# 915                1  'high qualif/self emp/mgmt'              1   

#      own_telephone foreign_worker class  
# 915            yes             no   bad  

# [1 rows x 21 columns]

# definimos só algumas colunas, aplicando o mesmo filtro anterior porém filtrando também apenas duas colunas.
credito3 = dados[['checking_status','duration']].loc[dados['credit_amount'] >  18000]
print(credito3)
#     checking_status  duration
# 915        0<=X<200        48


## Série 
# séries, única coluna
# pode ser criada a partir de listas, array do numpy ou coluna de data frame
s1 = pd.Series([2,5,3,34,54,23,1,16])
print(s1)
# 0     2
# 1     5
# 2     3
# 3    34
# 4    54
# 5    23
# 6     1
# 7    16
# dtype: int64


## Série com Array
# Serie a partir de um array do numpy, importa o numpy, chama o método array do numpy, 
# cria o array e em seguida utiliza o método Series do Pandas para transformar o array 
# em uma Serie.
import numpy as np
array1 = np.array([2,5,3,34,54,23,1,16])
s2 = pd.Series(array1)
print(s2)
# 0     2
# 1     5
# 2     3
# 3    34
# 4    54
# 5    23
# 6     1
# 7    16
# dtype: int32


## Série com DataFrame
# Series a partir de um dataframe. É possivel também criar uma série a partir de um 
# Data Frame, chamamos o dataframe e passamos o nome da coluna. Se checarmos o tipo 
# Notamos que foi criada uma Serie do Pandas.
s3 = dados['purpose']
print(s3)
type(s3)
# 0                 radio/tv
# 1                 radio/tv
# 2                education
# 3      furniture/equipment
# 4                'new car'
#               ...         
# 995    furniture/equipment
# 996             'used car'
# 997               radio/tv
# 998               radio/tv
# 999             'used car'
# Name: purpose, Length: 1000, dtype: object
# pandas.core.series.Series

# note a diferença utilizando [[]], temos um data frame e não uma Serie.
d4= dados[['purpose']]
type(d4)
# pandas.core.frame.DataFrame


## Renomeando 
# Podemos renomear qualquer objeto do Pandas, utilizando o método rename, aqui passamos que queremos 
# renomear colunas, esse método utiliza o conceito de chave e valor e cada par chave e valor 
# tem o nome atual da coluna e o nome que queremos que seja colocado.
dados.rename(columns={"duration":"duração","purpose":"propósito"})

# PS ==> Essa alteração embora seja feita ela não será persistida em nosso DataFrame veja: 
dados.head(1)

# Para que as alterações sejam persistidas no DataFrame utilizamos um parâmetro adicional 
# chamado inplace. Isso não é exclusivo apenas desse método, outros métodos do Pandas 
# para que sejam persistidas as alterações é necessário passar esse parâmetro como True.
dados.rename(columns={"duration":"duração","purpose":"propósito"},inplace=True)


## Excluindo Coluna
# Excluir coluna, para isso utilizamos o método drop passando a coluna que queremos excluir 
# em seguida o eixo axis=1 para excluir a coluna, em seguida passei o inplace para que os 
# dados sejam persistidos. 
dados.drop('checking_status',axis=1,inplace=True)
print(dados)
#     duração                    credit_history            propósito  \
# 0          6  'critical/other existing credit'             radio/tv   
# 1         48                   'existing paid'             radio/tv   
# 2         12  'critical/other existing credit'            education   
# 3         42                   'existing paid'  furniture/equipment   
# 4         24              'delayed previously'            'new car'   
# ..       ...                               ...                  ...   
# 995       12                   'existing paid'  furniture/equipment   
# 996       30                   'existing paid'           'used car'   
# 997       12                   'existing paid'             radio/tv   
# 998       45                   'existing paid'             radio/tv   
# 999       45  'critical/other existing credit'           'used car'   

#      credit_amount      savings_status  employment  installment_commitment  \
# 0             1169  'no known savings'         >=7                       4   
# 1             5951                <100      1<=X<4                       2   
# 2             2096                <100      4<=X<7                       2   
# 3             7882                <100      4<=X<7                       2   
# 4             4870                <100      1<=X<4                       3   
# ..             ...                 ...         ...                     ...   
# 995           1736                <100      4<=X<7                       3   
# 996           3857                <100      1<=X<4                       4   
# 997            804                <100         >=7                       4   
# 998           1845                <100      1<=X<4                       4   
# 999           4576          100<=X<500  unemployed                       3   

#           personal_status other_parties  residence_since   property_magnitude  \
# 0           'male single'          none                4        'real estate'   
# 1    'female div/dep/mar'          none                2        'real estate'   
# 2           'male single'          none                3        'real estate'   
# 3           'male single'     guarantor                4     'life insurance'   
# 4           'male single'          none                4  'no known property'   
# ..                    ...           ...              ...                  ...   
# 995  'female div/dep/mar'          none                4        'real estate'   
# 996        'male div/sep'          none                4     'life insurance'   
# 997         'male single'          none                4                  car   
# 998         'male single'          none                4  'no known property'   
# 999         'male single'          none                4                  car   

#      age other_payment_plans     housing  existing_credits  \
# 0     67                none         own                 2   
# 1     22                none         own                 1   
# 2     49                none         own                 1   
# 3     45                none  'for free'                 1   
# 4     53                none  'for free'                 2   
# ..   ...                 ...         ...               ...   
# 995   31                none         own                 1   
# 996   40                none         own                 1   
# 997   38                none         own                 1   
# 998   23                none  'for free'                 1   
# 999   27                none         own                 1   

#                              job  num_dependents own_telephone foreign_worker  \
# 0                        skilled               1           yes            yes   
# 1                        skilled               1          none            yes   
# 2           'unskilled resident'               2          none            yes   
# 3                        skilled               2          none            yes   
# 4                        skilled               2          none            yes   
# ..                           ...             ...           ...            ...   
# 995         'unskilled resident'               1          none            yes   
# 996  'high qualif/self emp/mgmt'               1           yes            yes   
# 997                      skilled               1          none            yes   
# 998                      skilled               1           yes            yes   
# 999                      skilled               1          none            yes   

#     class  
# 0    good  
# 1     bad  
# 2    good  
# 3    good  
# 4     bad  
# ..    ...  
# 995  good  
# 996  good  
# 997  good  
# 998   bad  
# 999  good  

# [1000 rows x 20 columns]

# Checando e a coluna realmente foi excluida do nosso DataFrame.
dados.head(1)


## Verificando Dados Nulos
# verificar dados nulos, esse método vai verificar se existem dados nulos, é bastante utilizado em 
# limpeza de dados. O método isnull verifica se existem dados Nulos, ele vai retornar uma tabela 
# com dados lógicos informando True onde exixtir algum valor nulo.
dados.isnull()
# 	duração	credit_history	propósito	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	residence_since	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 0	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 1	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 2	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 3	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 4	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 995	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 996	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 997	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 998	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 999	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False	False
# 1000 rows × 20 columns

# Porém essa saída a cima pode não ser tão funcional se tivermos uma grande quantidade de dados
# e para resolver isso podemos utilizar também o método sum, Note que no retorno ele vai mostrar que 
# de todas as colunas nenhuma possue dados Nulos.
# verificar dados nulos
dados.isnull().sum()
# duração                   0
# credit_history            0
# propósito                 0
# credit_amount             0
# savings_status            0
# employment                0
# installment_commitment    0
# personal_status           0
# other_parties             0
# residence_since           0
# property_magnitude        0
# age                       0
# other_payment_plans       0
# housing                   0
# existing_credits          0
# job                       0
# num_dependents            0
# own_telephone             0
# foreign_worker            0
# class                     0
# dtype: int64


## Removando Coluna NaN
# retirar colunas com NaN, ele vai checar e retirar.
dados.dropna()
# 	duração	credit_history	propósito	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	residence_since	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
# 0	6	'critical/other existing credit'	radio/tv	1169	'no known savings'	>=7	4	'male single'	none	4	'real estate'	67	none	own	2	skilled	1	yes	yes	good
# 1	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	2	'real estate'	22	none	own	1	skilled	1	none	yes	bad
# 2	12	'critical/other existing credit'	education	2096	<100	4<=X<7	2	'male single'	none	3	'real estate'	49	none	own	1	'unskilled resident'	2	none	yes	good
# 3	42	'existing paid'	furniture/equipment	7882	<100	4<=X<7	2	'male single'	guarantor	4	'life insurance'	45	none	'for free'	1	skilled	2	none	yes	good
# 4	24	'delayed previously'	'new car'	4870	<100	1<=X<4	3	'male single'	none	4	'no known property'	53	none	'for free'	2	skilled	2	none	yes	bad
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 995	12	'existing paid'	furniture/equipment	1736	<100	4<=X<7	3	'female div/dep/mar'	none	4	'real estate'	31	none	own	1	'unskilled resident'	1	none	yes	good
# 996	30	'existing paid'	'used car'	3857	<100	1<=X<4	4	'male div/sep'	none	4	'life insurance'	40	none	own	1	'high qualif/self emp/mgmt'	1	yes	yes	good
# 997	12	'existing paid'	radio/tv	804	<100	>=7	4	'male single'	none	4	car	38	none	own	1	skilled	1	none	yes	good
# 998	45	'existing paid'	radio/tv	1845	<100	1<=X<4	4	'male single'	none	4	'no known property'	23	none	'for free'	1	skilled	1	yes	yes	bad
# 999	45	'critical/other existing credit'	'used car'	4576	100<=X<500	unemployed	3	'male single'	none	4	car	27	none	own	1	skilled	1	none	yes	good
# 1000 rows × 20 columns

# preencher dados faltantes que são os NaN, passamos o nome da coluna, com o método 
# fillna passando o valor que queremos que seja colocado.
dados['duração'].fillna(0,inplace = True)


# iloc podemos colocar intervalos de linhas e colunas, aqui eu informo que quero as linhas de 
# 0 a 3 e as colunas de 0 a 5.
dados.iloc[0:3,0:5]
# duração	credit_history	propósito	credit_amount	savings_status
# 0	6	'critical/other existing credit'	radio/tv	1169	'no known savings'
# 1	48	'existing paid'	radio/tv	5951	<100
# 2	12	'critical/other existing credit'	education	2096	<100


# Aqui eu quero uma lista de linhas e as colunas de 0 a 5 
dados.iloc[[0,1,2,3,7],0:5]
# 	duração	credit_history	propósito	credit_amount	savings_status
# 0	6	'critical/other existing credit'	radio/tv	1169	'no known savings'
# 1	48	'existing paid'	radio/tv	5951	<100
# 2	12	'critical/other existing credit'	education	2096	<100
# 3	42	'existing paid'	furniture/equipment	7882	<100
# 7	36	'existing paid'	'used car'	6948	<100