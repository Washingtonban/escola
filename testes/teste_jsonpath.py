import requests
import jsonpath


avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[*]')

print(resultados)