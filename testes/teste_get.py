import requests

# Variaveis
headers = {'Authorization': 'Token 15a14c9c2f09bb646abdc32c5ed54d9cda884faf'}
url_cursos = 'http://127.0.0.1:8000/api/v2/cursos'
url_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'
url_curso = 'http://127.0.0.1:8000/api/v2/cursos/2'
url_avaliacao = 'http://127.0.0.1:8000/api/v2/avaliacoes/2'

# Metodos
get_cursos = requests.get(url=url_cursos, headers=headers)
get_avaliacoes = requests.get(url=url_avaliacoes)
get_curso = requests.get(url=url_curso, headers=headers)
get_avaliacao = requests.get(url=url_avaliacao)

# Testes
# print(cursos.status_code)
print(get_curso.json())
assert get_curso.status_code == 200