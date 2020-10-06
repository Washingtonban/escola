import requests


# GET Avaliacoes

print('###############################')
print('#         Avaliações          #')
print('###############################')

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
cursos = requests.get('http://127.0.0.1:8000/api/v2/cursos/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
print(avaliacoes.json())

# acessando a quantidade de registros
print(avaliacoes.json()['count'])

# Acessando o primeiro elemento de uma lista
print(avaliacoes.json()['results'][-1])

# GET Cursos
headers = {'Authorization': 'Token 15a14c9c2f09bb646abdc32c5ed54d9cda884faf'}
curso = requests.get(url='http://127.0.0.1:8000/api/v2/cursos', headers=headers)


print('###############################')
print('#           Cursos            #')
print('###############################')

print(curso.json())

# GET Avaliacao

print('###############################')
print('#         Avaliação           #')
print('###############################')

avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/7')


print(avaliacao.json())

# GET Curso
headers = {'Authorization': 'Token 15a14c9c2f09bb646abdc32c5ed54d9cda884faf'}
curso = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/3', headers=headers)


print('###############################')
print('#           Curso             #')
print('###############################')

print(curso.json())
