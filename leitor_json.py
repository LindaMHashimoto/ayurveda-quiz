import json

'''
Funcao para ler arquivo JSON
Funcao para adicionar dados ao arquivo JSON
'''

valores_doshas = []
lista_perguntas = []
with open('questoes.json', 'r') as f:

	lista = json.load(f)


for i in lista:

	valores_doshas = i['doshas']
	lista_perguntas.append(i)
print(lista_perguntas)