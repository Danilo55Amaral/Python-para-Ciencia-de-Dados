# NumPy

# O NumPy assim como o Pandas é uma biblioteca muito utlizada em 
# Ciência de Dados, é uma bilioteca muito importante para tratar dados.

# Computação Científica: facilitam operações matemáticas 
# avançadas e outros tipos de operações em muitos dados.

# Objeto de Matriz Multidimensional. 

# Variedade de rotinas para operações rápidas em matrizes. 

# Os arrays NumPy têm um tamanho fixo na criação, ao contrário 
# das listas  Python (que podem crescer dinamicamente). 

# Os elementos em uma matriz NumPy devem ser todos do mesmo tipo 
# de dados e, portanto, terão o mesmo tamanho na memória.

# Vamos ver na prática.

# Importando a biblioteca NumPy
import numpy as np 

# Criando uma matriz unidimensional
matriz_a = np.array([12,34,26,18,10])
print(matriz_a)
print(matriz_a.dtype)


## Criando uma matriz unidimensional.
matriz = np.array([12,34,26,18,10])
print(matriz)
print(type(matriz))
# [12 34 26 18 10]
# <class 'numpy.ndarray'>

# Note que foi utilizado o método array do numpy para criar um vetor.


# criando um array com um tipo específico
# criando um array como float de 64 bits
matriz_float = np.array([1, 2, 3], dtype = np.float64)
print(matriz_float)
print(type(matriz_float))
matriz_int = np.array([1, 2, 3], dtype = np.int32)
print(matriz_int)
print(type(matriz_int))
# [1. 2. 3.]
# <class 'numpy.ndarray'>
# [1 2 3]
# <class 'numpy.ndarray'>

# Note que no primeiro retorno ele retornou valores com . por que foi convertido para float.

## Fazendo uma conversão de tipo.
# mudar o tipo do array
# Podemos transformar tipos de dados de arrays
matriz_new = np.array([1.4, 3.6, -5.1, 9.42, 4.999999])
print(matriz_new)
# quando transformamos de float para int os valores são truncados, utilizei a função astype para 
# fazer a conversão de tipos, passando o np e passando para inteiro.
matriz_new_int = matriz_new.astype(np.int32)
print(matriz_new_int)
# [ 1.4       3.6      -5.1       9.42      4.999999]
# [ 1  3 -5  9  4]

# podemos fazer o inverso também, note que o ponto na saída desse código vai mostrar que foi 
# covertido para o tipo float.
matriz5 = np.array([1, 2, 3, 4])
print(matriz5)
matriz6 = matriz5.astype(float)
print(matriz6)
# [1 2 3 4]
# [1. 2. 3. 4.]


## Elementos com mais de uma Dimensão 
# mais de uma dimensão
# cria uma matriz bidimensional, aqui temos linhas e colunas.
matriz7 = np.array([[7,2,23],[12,27,4],[5,34,23]])
print(matriz7)
# [[ 7  2 23]
#  [12 27  4]
#  [ 5 34 23]]


# criar arrays vazios tipificados
# Nessas matrizes estamos passando os valores de linhas por colunas exemplo 4,3 => 4 linhas e 3 colunas.
# empty significa que não são inicializados, não que são vazios, embora gere valores vazios.
vazio = np.empty([3,2], dtype = int)
print(vazio)
print("-------")
# cria uma matriz 4x3 com valores zero, usando o método zeros.
zeros = np.zeros([4,3])
print(zeros)
print("-------")
# com valores igual a um, utilizando o método ones.
um = np.ones([5,7])
print(um)
print("-------")
# cria matriz quadrada com diagonal principal com valores 1 e os outros valores zero, para fazer isso 
# utilizamos o método eye passando o valor que será tanto de linhas como colunas.
diagonal = np.eye(5)
print(diagonal)
# [[         0 1072693248]
#  [         0 1073741824]
#  [         0 1074266112]]
# -------
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
# -------
# [[1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1.]]
# -------
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]


## Em Ciência de Dados é bastante comum se criar dados aleatórios. 
# Gerando valores aleatórios entre zero e um, eu utilizo o método random passando random passando a 
# quantidade de valores.
ale = np.random.random((5))
print(ale)
print("-------")
# valores aleatórios distribuição normal contendo valores negativos, caso seja necessario criar 
# uma distribuição normal com dados aleatórios utilizamos o metodo random passando randn. 
ale2= np.random.randn((5))
print(ale2)
print("-------")
# valores aleatórios 3 x 4 , porém estamos multiplicando por 10 ou seja esses valores aleatórios 
# que serão criados serão multiplicados por 10. 
ale3 = (10*np.random.random((3,4)))
print(ale3)
# [0.08101656 0.24734888 0.65729846 0.13106201 0.0375163 ]
# -------
# [ 0.04706145 -0.56114546  0.29454386  0.61667811  1.10180369]
# -------
# [[5.16396157 3.15404788 9.38182665 7.01014199]
#  [5.21595838 6.87588254 9.2813537  9.30786589]
#  [3.36332449 8.97622099 3.23065537 1.92491556]]


# Outra forma de gerar valores aleatórios.
# Uso de semente, quando se tem processos que se tem o uso de aleatoriedade, processos não deterministicos 
# em geral é necessário repetir experimentos ou repetir os números aleatorios da mesma forma que eles 
# foram gerados, para isso produzimos uma semente, com isso eu gero números aleatorios e se for necessário 
# eu consigo repetir esses números.
# Eu utilizo o método random passando default_rgn e passo um número que será a semente e essa semente vai 
# gerar esses valores aleatorios que poderão ser reutilizados.
gerando_numeros_ale = np.random.default_rng(1)
ale5 = gerando_numeros_ale.random(3)
print (ale5)

# Gerar inteiros, aqui eu utilizei a minha semente novamente passando para gerar inteiros, passando para gerar 
# números inteiros aleatórios até 10, em uma matriz com 3 linhas e 4 colunas.
# PS - se eu mudar o valor da semente lá onde eu definir, os valores que serão gerados mudam.
ale6 = gerando_numeros_ale.integers(10, size=(3, 4))
print(ale6)
# [0.51182162 0.9504637  0.14415961]
# [[8 9 2 3]
#  [8 4 2 8]
#  [2 4 6 5]]


## Método para Remover repetições.
# O método unique remove repetições, primeiramente criamos o array com vários 
# elementos repetidos, em seguida eu chamo o método unique passando esse mesmo objeto.
sem_repeticao = np.array([11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 18, 19, 20])
sem_repeticao = np.unique(sem_repeticao)
print(sem_repeticao)
# [11 12 13 14 15 16 17 18 19 20]


# funções específicas.
# cria a matriz bidimensional que chamei de k
k = np.array([[17,22,43],[27,25,14],[15,24,32]])
# Mostra a matriz k
print(k)
# Mostra um elemento específico da matriz k, aqui ele pega o elemento na posição 0, 1 
print(k[0][1])
# Mostra o tamanho das dimensões da matriz k, o método shape mostra o formato dessa matriz no  NumPy.
print(k.shape)
# [[17 22 43]
#  [27 25 14]
#  [15 24 32]]
# 22
# (3, 3)


# Funções Matemáticas aplicadas a matriz do exemplo passado.
# Mostra o maior valor da matriz k
print(k.max())
# Mostra o menor valor da matriz k
print(k.min())
# Mostra a soma dos valores da matriz k
print((k.sum()))
# Mostra o valor da média dos valores da matriz k
print(k.mean())
# Mostra o valor do desvio padrão (standard deviation) dos valores da matiz k
print(k.std())
# 43
# 14
# 219
# 24.333333333333332
# 8.615231988880057


# Funções universais, aplicadas a todos os elementos, # eu criei uma matriz que chamei de K1
# esses métodos serão aplicados universalmente a cada elemento da matriz.
# Mostra o valor da raiz quadrada de todos elementos 
k1 = np.array([1, 4, 9, 16, 25, 36])
print(np.sqrt(k1))
# Mostra o valor do exponencial de todos elementos
print(np.exp(k1))
# [1. 2. 3. 4. 5. 6.]
# [2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+06
#  7.20048993e+10 4.31123155e+15]


# Extração de elementos, primeiro eu criei uma array 
extracao = np.array([1, 2, 3, 4, 5, 6])
# Mostra o elemento da posição 2
print(extracao[1])
print("-------")
# Mostra o array criado a partir da posição 0, dois elementos, vale ressaltar 
# que em intervalos no Python ele ignora sempre o ultimo valor.
print(extracao[0:2])
print("-------")
# Mostra o array criado a partir da 2a posição
# até todo o restante do array
print(extracao[1:])
print("-------")
# Mostra o array criado a partir da antepenúltima
#posição até o final
print(extracao[-3:])
# 2
# -------
# [1 2]
# -------
# [2 3 4 5 6]
# -------
# [4 5 6]


# Extração de linhas e colunas
removendo = np.array([[4, 5], [6, 1], [7, 4]])
print(removendo)
print("-------")
#primeira linha, todas as colunas
removendo_linha_1 = removendo[0, :]
print(removendo_linha_1)
print("-------")
#segunda linha
removendo_linha_2 = removendo[1, :]
print(removendo_linha_2)
print("-------")
#terceira linha
removendo_linha_3 = removendo[2, :]
print(removendo_linha_3)
print("-------")
#todas as linhas, primeira coluna
removendo_coluna_1 = removendo[:, 0]
print(removendo_coluna_1)
print("-------")
#todas as linhas, segunda coluna
removendo_coluna_2 = removendo[:, 1]
print(removendo_coluna_2)
# [[4 5]
#  [6 1]
#  [7 4]]
# -------
# [4 5]
# -------
# [6 1]
# -------
# [7 4]
# -------
# [4 6 7]
# -------
# [5 1 4]


# Aição e multiplicação de matrizes
n = np.array([[1, 2], [3, 4]])
o = np.array([[1, 1], [1, 1]])
res1 = n+o
print(res1)
print("-------")
res2 = n*o
print(res2)
print("-------")
p = np.array([[1, 2], [3, 4], [5, 6]])
q = np.array([[2, 1]])
print(p+q)
# [[2 3]
#  [4 5]]
# -------
# [[1 2]
#  [3 4]]
# -------
# [[3 3]
#  [5 5]
#  [7 7]]


# Transposição, rearranja um conjunto de 15 elementos de 0 a 14 
# em 3 linhas e 5 colunas. Eu crio um arranjo de 15 elementos em uma matriz de 3 linhas e 5 colunas.
f = np.arange(15).reshape((3, 5))
# Mostra a matriz transposta entre linhas e colunas
print(f)
print("-------")
# Utilizo o método T para fazer a tranposição.
s = f.T
print(s)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
# -------
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]


# Outra forma de fazer, mesmo resultado.
r = np.arange(15).reshape((3, 5))
print(r)
print("-------")
# Rearranja um conjunto de 15 elementos 
# mostra a matriz transposta entre linhas e colunas
s = r.transpose((1,0))
print(s)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
# -------
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]


# Expressões lógicas
# Usando where
# criando matriz com valores aleatórios positivos e negativos
v = np.random.randn(4, 4)
print(v)
# criando matriz com valores booleanos baseado no array v , eu fiz um teste lógico 
# verificando se o v é maior que 0, ele vai retornar falso se o V for maior que 0
# senão ele retorna verdadeiro, ele vai gerar uma matriz de verdadeiros ou falsos 
# de acordo com o resultado do teste lógico.
x = (v > 0)
print(x)
# Criando matriz com valores -1 e 1 baseado nos valores do array x, também faço 
# um teste lógico, x maior que 0 vai gerar 1 se não ele vai gerar -1
z = np.where(x > 0, 1, -1)
print(z)
# [[-4.96563487e-01 -1.51837506e-01 -7.08996776e-01  9.57646480e-01]
#  [-7.96420579e-01  1.24283349e+00 -2.47639930e-01  6.10613056e-01]
#  [-1.00554832e+00 -5.54180920e-01 -1.19975797e-04  3.66623806e-01]
#  [-7.46948885e-01 -2.95980339e+00 -1.09055013e+00  3.64864672e-02]]
# [[False False False  True]
#  [False  True False  True]
#  [False False False  True]
#  [False False False  True]]
# [[-1 -1 -1  1]
#  [-1  1 -1  1]
#  [-1 -1 -1  1]
#  [-1 -1 -1  1]]