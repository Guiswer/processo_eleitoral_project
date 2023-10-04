"""
Aluno: Guilherme Leandro - RA: G773616	 
TURMA: CC2A13 
Profa. Eliane 
"""

import os #Library para identificar o OS (utilizar comando 'clear')


#Identificação da Seção e Zona Eleitoral
Seção = "0129"
Zona_Eleitoral = "546"

#Código de Identificação da Urna Eletrônica
Código_Identificação_UE = "jvf302"


#Definindo dicionários para contabilizar o total de votos
total_prefeito = {"C1": 0,  "C2": 0, "C3": 0, "C4": 0}

total_vereador = {"V1": 0, "V2": 0, "V3": 0, "V4": 0}


#Função para limpar o terminal
def limpar_terminal():
    if os.name == 'posix':  #Linux e macOS
        os.system('clear')
    elif os.name == 'nt':  #Windows
        os.system('cls')

#Definindo variáveis para receber os inputs
votação_prefeito = ''
votação_vereador = ''

#Valores pré-existentes

apto = 0 

#Votos brancos e nulos Prefeito
votos_brancos_prefeito = 0
votos_nulos_prefeito = 0

#Votos brancos e nulos vereador
votos_brancos_vereador = 0
votos_nulos_vereador = 0


#Processo de votação
while True: 

	#Garantindo que o input seja inteiro, se not int() = idade inválida
	try:
		idade = int(input("Digite sua idade: "))
	except ValueError:
	    print("\n * Idade inválida * \n")
	    continue #continuar a execução "não pare"  
	    
	if idade == 2023: #Condição para o encerramento do programa, apenas para administradores das máquinas
		break
	elif idade >= 16 and idade <= 115: #se existe alguém com 115 anos.
		apto = apto + 1 

		#print com aspas triplas para o conteúdo ser exibido do mesmo jeito que foi escrito no editor
		print("""
Opções de voto para PREFEITOS:

C1: Candidato 1 
C2: Candidato 2
C3: Candidato 3
C4: Candidato 4
VB: Voto BRANCO
VN: Voto NULO
""")
		votação_prefeito = input("Digite a sigla de seu candidato a prefeito ou outra opção: ")

		#O eleitor deve digitar corretamente a sigla de seu candidato
		while votação_prefeito != "C1" and votação_prefeito != "C2" and votação_prefeito != "C3" and votação_prefeito != "C4" and votação_prefeito != "VB" and votação_prefeito != "VN":
			print("\n* Escolha inválida *\n")
			votação_prefeito = input("Digite a sigla de seu candidato a PREFEITO, ou outra opção: ")
		print("\nO voto foi cadastrado!")

		#print com aspas triplas para o conteúdo ser exibido do mesmo jeito que foi escrito no editor
		print(""" \n
Opções de voto para VEREADORES: 

V1: Candidato 1 
V2: Candidato 2
V3: Candidato 3
V4: Candidato 4
VB: Voto BRANCO
VN: Voto NULO
""")
		votação_vereador = input("Digite a sigla de seu candidato a VEREADOR, ou outra opção: ")

		#O eleitor deve digitar corretamente a sigla de seu candidato
		while votação_vereador != "V1" and votação_vereador != "V2" and votação_vereador != "V3" and votação_vereador != "V4" and votação_vereador != "VB" and votação_vereador != "VN":
			print("\n* Escolha inválida *\n")
			votação_vereador = input("Digite a sigla de seu candidato a vereador ou outra opção: ")
		print("\n* Seus votos já foram cadastrados! 🙂 *\n") #primeira heurística de Nilsen
		
	elif idade < 16 and idade > 0:
		print("\nInapto a votação. Aguarde até completar 16 (dezesseis) anos.\n")
		
	else:
		print("\nIdade inválida.")

	if idade >= 16 and idade <= 115:
		print("\nVoto para prefeito:", votação_prefeito)
		print("Voto para vereador:", votação_vereador)
		#Opções para o eleitor prosseguir com o processo ou se deseja refazê-lo
		verificar = int(input("\nDigite (1) para confirmar suas escolhas, ou digite (2) se deseja anular suas escolhas e refazer o processo. "))
	elif idade < 16:
		verificar = 1
		print("\nProcesso encerrado!")

	if verificar == 2:
		if idade >= 16:
			try:
				print("Dentro do bloco try")
				#para anular as escolhas - o total_prefeito simplesmente não recebe nada
				total_prefeito[votação_prefeito] += 0
				total_vereador[votação_vereador] += 0
			except KeyError:
				print("Dentro do bloco except")
				votos_brancos_prefeito += 0
				votos_brancos_vereador += 0
				continue	
		else:
			#previnir erros para menores
			None

	elif verificar == 1:
		if idade >= 16:

			#try para o prefeito
			#o VB e VN não estão no dicionário como também não podem ser candidatos
			try:
				total_prefeito[votação_prefeito] += 1
			except KeyError:
				if votação_prefeito == 'VB':
					votos_brancos_prefeito += 1
				elif votação_prefeito == 'VN':
					votos_nulos_prefeito += 1

			#try para o vereador
			#o VB e VN não estão no dicionário como também não podem ser candidatos
			try:
				total_vereador[votação_vereador] += 1
			except KeyError:
				if votação_vereador == 'VB':
					votos_brancos_vereador += 1
				elif votação_vereador == 'VN':
					votos_nulos_vereador += 1


		else:
			#previnir erros para menores
			None
	else:
		print("Opção inválida")	

	print("\nPressione 'ENTER' encerrar sua sessão.")
	confirmar = input()
	limpar_terminal()


# * Votação (de uma Seção Eleitoral) *

#IDENTIFICAÇÃO DA URNA ELETRÔNICA
print("\nSeção:", Seção, "\nZona eleitoral:", Zona_Eleitoral,"\n")
print("Código de Identificação da Urna Eletrônica:",Código_Identificação_UE,"\n")

#Quantos eleitores podem votar
print("Total dos Eleitores que podem votar:",apto,"\n")


# * Totalização
print(total_prefeito)
print(total_vereador)


# * Divulgação dos Resultados


#Candidato a Prefeito mais votado

#Variáveis para auxiliar a contagem

#Prefeito
lista_total_prefeito = []

#Colocando os elementos da lista em ordem crescente
lista_total_prefeito = sorted(total_prefeito.items(), key = lambda x: x[1]) #lambda para extrair o segundo elemento de cada tupla

#Vereador
lista_total_vereador = []

#Colocando os elementos da lista em ordem crescente
lista_total_vereador = sorted(total_vereador.items(), key = lambda x: x[1]) #lambda para extrair o segundo elemento de cada tupla


#Verificando possível empate
if lista_total_prefeito[-1][1] == lista_total_prefeito[-2][1] and lista_total_prefeito[-1][1] != 0 and lista_total_prefeito[-2][1] != 0:
	print(f"\nHouve um empate entre os candidatos a prefeito {lista_total_prefeito[-1]} e {lista_total_prefeito[-2]} e haverá um segundo turno!")

#Caso o usuário somente digite votos BRANCOS ou NULOS - mostrar que houve um "equivoco"
elif lista_total_prefeito[-1][1] == 0:
	print('Houve um "equivoco nas eleições", haverá um novo turno.')

else:
	#resultados das votações para prefeito
	print("\nCandidato a Prefeito mais votado:", lista_total_prefeito[-1])


print("\nVotos Brancos na votação para Prefeitos:", votos_brancos_prefeito)	
print("Votos Nulos na votação para Prefeitos:", votos_nulos_prefeito)

print("x-------------------------------------------------------------------x")

if lista_total_vereador[-1][1] == lista_total_vereador[-2][1] and lista_total_vereador[-1][1] != 0 and lista_total_vereador[-2][1] != 0:
	print(f"\nHouve um empate entre os candidatos a vereador {lista_total_vereador[-1]} e {lista_total_vereador[-2]} e haverá um segundo turno!")

#Caso o usuário somente digite votos BRANCOS ou NULOS - mostrar que houve um "equivoco"
elif lista_total_vereador[-1][1] == 0:
	print('\n * Houve um "equivoco nas eleições", haverá um novo turno * ')

else: 
	#resultados das votações para vereador
	print("\nCandidato a Vereador mais votado:", lista_total_vereador[-1])


print("\nVotos Brancos na votação para Vereador:", votos_brancos_vereador)
print("Votos Nulos na votação para Vereador:", votos_nulos_vereador)
