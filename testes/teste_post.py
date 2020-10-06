import requests

# Variaveis
headers = {'Authorization': 'Token 15a14c9c2f09bb646abdc32c5ed54d9cda884faf'}
url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'
url_curso = 'http://127.0.0.1:8000/api/v2/cursos/2'
url_avaliacao = 'http://127.0.0.1:8000/api/v2/avaliacoes/2'

# Cursos

novo_curso = {
    "titulo": "Testando teste de api",
    "url": "https://outlook.live.com/mail/0/inbox/id/AQQkADAwATYwMAItOGIwZi0zMWY2LTAwAi0wMAoAEABGT4vbee39TqwJRBORRf0w"
}
delete_curso = {
    "id": 7
}

# Metodos
post_curso = requests.post(url=url_cursos, headers=headers, data=novo_curso)

# Resultados
print(post_curso.json())
assert post_curso.status_code == 201

# delete_curso = requests.delete(url=f'{url_cursos}3/', headers=headers)
# print(delete_curso.json())
# print(delete_curso.status_code)