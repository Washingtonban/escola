import jsonpath
import requests

class TestCursos:
    headers = {'Authorization': 'Token 15a14c9c2f09bb646abdc32c5ed54d9cda884faf'}
    url_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    # Get ultimo id do ultimo curso
    curso_resultado = requests.get(url=url_cursos, headers=headers)
    ultimo_curso_id = jsonpath.jsonpath(curso_resultado.json(), 'results[*].id')

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_cursos}{self.ultimo_curso_id[-1]}/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de pytest",
            "url":"https://www.google.com/search?q=facebook&oq=face&aqs=chrome.0.69i59j69i57j69i60l2j69i65l2j69i60l2.2532j0j1&sourceid=chrome&ie=UTF-8"
        }

        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso de pytest 2",
            "url": "https://www.google.com/"
        }
        resposta = requests.put(url=f'{self.url_cursos}{self.ultimo_curso_id[-1]}/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        # metodo de teste
        resposta = requests.delete(url=f'{self.url_cursos}{self.ultimo_curso_id[-1]}/', headers=self.headers)

        assert resposta.status_code == 204

