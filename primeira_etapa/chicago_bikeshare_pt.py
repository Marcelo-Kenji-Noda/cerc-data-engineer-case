# coding: utf-8 

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
    print(f"{i}: {data_list[i+1]}")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(20):
    print(f"{i}: {data_list[i][-2]}")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int) -> list:
    """
    Essa função retorna os dados da coluna na posição index
    
    Observação: A lista data deve conter outras listas, de forma que cada posição da lista seja correspondente a uma coluna
    
    Parameters:
    ----------
        data: list
            Dados em formato de lista, tal que cada elemento da lista corresponde a uma linha de uma tabela
        index: int
            Posição da coluna da tabela que será extraída como lista

    Returns:
    -------
        list
            Retorna uma lista contendo as informações acerca da posição index de cada elemento de data
        
    Examples
    --------
    >>> data = [[1,'A','X'],[2,'B','Y'],[5,'C','Z']]
    >>> column_to_list(data, 0)
    [1,2,5]
    >>> column_to_list(data, 1)
    ['A','B','C']
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for row in data:
        column_list.append(row[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1048575, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for gender in column_to_list(data_list, -2):
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1
    else:
        pass

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 665437 and female == 198247, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list: list) -> list[int, int]:
    """
    Função conta a quantidade de gêneros na lista

    Parameters:
    ----------
        data_list: list[Literal["Male","Female",""]]
            Lista contendo os gêneros a serem contados

    Returns:
    -------
        list[int, int]:
            Lista de tamanho 2 sendo o primeiro item a quantidade de occorências do gênero masculino e o secundo item a quantidade de occorências do gênero feminino
        
    Examples
    --------
    >>> count_gender(["Male", "Male", "Male", "", "Female","Male", "Female","Female"])
    [4, 3]
    >>> count_gender([])
    [0, 0]
    """
    male = 0
    female = 0
    for gender in column_to_list(data_list, -2):
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1
        else:
            pass
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 665437 and count_gender(data_list)[1] == 198247, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list: list) -> str:
    """
    Função encontra qual o gênero com maior ocorrência na lista
    Parameters:
    ----------
        data_list: list[Literal['Male','Female','']]
            Lista contendo os gêneros

    Returns:
    -------
        Literal['Male','Female','Equal']
            Retorna uma string contendo o gênero com maior ocorrência (Ou "Equal" caso a quantidade seja igual)
        
    Examples:
    --------
    >>> most_popular_gender(["Male","Female","","Female","Female","Male"])
    Female
    >>> most_popular_gender([])
    Equal
    """
    answer = ""
    male_count, female_count = count_gender(data_list=data_list)
    if male_count > female_count:
        answer = "Male"
    elif female_count > male_count:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

user_types = column_to_list(data_list, -3)
user_type_counter = {} # Utilizando um dicionário para facilitar o processo de contagem
for user in user_types:
    if user not in user_type_counter:
        user_type_counter[user] = 1 # Faz a contagem da primeira ocorrência de um novo user_type
    else:
        user_type_counter[user] += 1 # Adiciona 1 ao número de ocorrências de um user_type

types = user_type_counter.keys()
quantity = user_type_counter.values()
y_pos = list(range(len(types)))

plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A condição é falsa pois o o data_list contém valores em branco para o campo de gênero. Ou seja, o total de linhas corresponde ao total de nulos, 'Male' e 'Female' e não somente ao total de 'Male' e 'Female'"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# Passo a Passo
# 1. Utilizar a função column_to_list para receber uma lista com todos os valores de trip_duration
# 2. Corrigir o tipo de dado de string para float O(N) (N = número de linhas)
# 3. Ordenar os dados para o cálculo da mediana O(N*Log(N)), Ordem de todas as operações => O(N*Log(N)) + O(N) => O(N*Log(N))
# 4. Encontrar os valores de mediana, média, min e max

trip_duration_list = [float(i) for i in trip_duration_list]
sorted_trip_duration_list = sorted(trip_duration_list)
N = len(sorted_trip_duration_list)

min_trip = sorted_trip_duration_list[0]
max_trip = sorted_trip_duration_list[-1]
mean_trip = sum(sorted_trip_duration_list)/N
if N % 2 == 0:
    median_trip = (sorted_trip_duration_list[N//2] + sorted_trip_duration_list[N//2 - 1])/2
else:
    median_trip = sorted_trip_duration_list[N//2]
    
print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 885, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 624, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set()
start_stations_names = column_to_list(data_list, 3)
for station in start_stations_names:
    if station not in start_stations:
        start_stations.add(station)
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 578, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list: list) -> tuple[list, list]:
    """
    Função conta a ocorrência de cada elemento de uma lista
    Parameters:
    ----------
        column_list: list[Any]
            Lista contendo os elementos a serem contados

    Returns:
    -------
        tuple(list, list)
            Tupla contendo as listas das chaves e a lista com as quantidades, respectivamente
        
    Examples:
    >>> count_items(["A","A","B","C","D","G"])
    (["A","B","C","D","G"],[2,1,1,1,1])
    >>> count_items(["C","A","D","D","D"])
    (["C","A","D"],[1,1,3])
    --------
    """
    column_list_mapping = {}
    for item in column_list:
        if item not in column_list_mapping:
            column_list_mapping[item] = 1
        else:
            column_list_mapping[item] += 1
    
    return list(column_list_mapping.keys()), list(column_list_mapping.values())


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1048575, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
