questoes = ['Eu sou uma pessoa muito paciente', 0, 0, 1]
#Tá dando erro na somatória quando o valor dentro da lista é igual a 1. O q q tá contecendooo
soma_vata = 0;
soma_pitta = 0;
soma_kapha = 0;

for i in questoes:

	valor_vata = questoes[1]
	if (valor_vata != 0):
		soma_vata +=1
	else:
		soma_vata = soma_vata

	valor_pitta = questoes[2]

	if (valor_pitta != 0):

		soma_pitta +=1

	else:

		soma_pitta = soma_pitta

	valor_kapha = questoes[3]

	if(valor_kapha != 0):

		soma_kapha +=1

	else:

		soma_kapha = soma_kapha

print('Somatório de pontos Vata: ',soma_vata, ', Soma de pontos Pitta: ', soma_pitta, ', Somos de pontos Kapha: ', soma_kapha)
