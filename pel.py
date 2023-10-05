"""

/**************************************/
/* Aluno: Guilherme Leandro - G773616 */
/* TURMA: CC2A13		      */
/* Profa. Eliane 		      */
/**************************************/

"""

import os #Library para identificar o OS (utilizar comando 'clear')
import time #Library para trabalhar com contagens


#Função para limpar o terminal
def limpar_terminal():
    if os.name == 'posix':  #Linux e macOS
        os.system('clear')
    elif os.name == 'nt':  #Windows
        os.system('cls')

print("Inicializando a Urna Eletrônica... 🇧🇷")
time.sleep(3) #adicionando 3 segundos de espera 
limpar_terminal() #chamando função que apaga o terminal

#Identificação da Seção e Zona Eleitoral
seção = "0129"
zona_eleitoral = "546"

#Código de Identificação da Urna Eletrônica
código_identificação_ue = "jvf302"

#Total de eleitores esperados
eleitores_esperados = 50

#Exibindo dados de identificação da Urna Eletrônica
print(f""" 
* Identificação da Urna Eletrônica *

Seção: {seção}
Zona eleitoral: {zona_eleitoral}
Total de eleitores(as) esperados: {eleitores_esperados}

  """)

#Status do sistema
print("\nIniciando processo de votação...")

time.sleep(2)

print("\nTudo pronto para o processo! ✅\n") #Status do sistema
input("Pressione 'ENTER' para iniciar...")

time.sleep(0.2) #adicionando 0.2s de espera

limpar_terminal() #apagando terminal

#Definindo dicionários para contabilizar o total de votos
total_prefeito = {"C1": 0,  "C2": 0, "C3": 0, "C4": 0}

total_vereador = {"V1": 0, "V2": 0, "V3": 0, "V4": 0}


#Definindo variáveis pré-existentes para receber os inputs e previnir erros de "variável não definida"
votação_prefeito = ''
votação_vereador = ''

#Valores pré-existentes

#aptos a voto (pessoas que votaram)
apto = 0 

#Votos para os partidos
pdb = 0 
psb = 0


#Votos brancos e nulos Prefeito
votos_brancos_prefeito = 0
votos_nulos_prefeito = 0

#Votos brancos e nulos vereador
votos_brancos_vereador = 0
votos_nulos_vereador = 0

#Tirar valores dos partidos caso o user desejar refazer o processo
tirar_pdb = 0
tirar_psb = 0

#Auxiliadores das variáveis "tirar"
tirar_pdb_aux = 0
tirar_psb_aux = 0

#Processo de votação
while True: 

	#Garantindo que o input seja inteiro, se not int() = idade inválida
	try:
		idade = int(input("Por favor, digite sua idade: "))
	except ValueError:
	    print("\n * Idade inválida * ")
	    print("\nIdade inválida. Por favor digite corretamente a sua idade 😊")
	    time.sleep(5) #5 segundos de espera

	    limpar_terminal()
	    continue #continuar a execução "não pare"  
	    
	time.sleep(1) #adicionando 1s de espera para apagar o terminal
	limpar_terminal() #apagando o terminal

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
VB: Voto BRANCO ⚪
VN: Voto NULO ⚫
""")
		votação_prefeito = input("Digite a sigla de seu candidato a prefeito ou outra opção: ")

		#match case para contabilizar os votos para os partidos PREFEITO
		match votação_prefeito:
			case "C1":
				pdb += 1
				tirar_pdb += 1 #Caso opção (2) devemos remover os votos para os partidos
			case "C2":
				pdb += 1 
				tirar_pdb += 1
			case "C3":
				psb += 1
				tirar_psb += 1
			case "C4":
				psb += 1
				tirar_psb += 1 

		#O eleitor deve digitar corretamente a sigla de seu candidato
		while votação_prefeito != "C1" and votação_prefeito != "C2" and votação_prefeito != "C3" and votação_prefeito != "C4" and votação_prefeito != "VB" and votação_prefeito != "VN":
			print("\n* Escolha inválida, o processo está reiniciando.. *\n")
			print("Por favor, digite corretamente a sua opção 😊 \n")

			time.sleep(5)
			limpar_terminal()

			print("""
Opções de voto para PREFEITOS:

C1: Candidato 1 
C2: Candidato 2
C3: Candidato 3
C4: Candidato 4
VB: Voto BRANCO ⚪
VN: Voto NULO ⚫
""")

			votação_prefeito = input("Digite a sigla de seu candidato a PREFEITO, ou outra opção: ")
		print("\nSeu voto foi cadastrado! ✅")

		time.sleep(2)
		limpar_terminal()

		#print com aspas triplas para o conteúdo ser exibido do mesmo jeito que foi escrito no editor
		print(""" \n
Opções de voto para VEREADORES: 

V1: Candidato 1 
V2: Candidato 2
V3: Candidato 3
V4: Candidato 4
VB: Voto BRANCO ⚪
VN: Voto NULO ⚫
""")
		votação_vereador = input("Digite a sigla de seu candidato a VEREADOR, ou outra opção: ")

		#match case para contabilizar os votos para os partidos VEREADOR
		match votação_vereador:
			case "V1":
				pdb += 1
				tirar_pdb += 1 #Caso opção (2) devemos remover os votos para os partidos
			case "V2":
				pdb += 1
				tirar_pdb += 1 
			case "V3":
				psb += 1
				tirar_psb += 1
			case "V4":
				psb += 1
				tirar_psb += 1

		#O eleitor deve digitar corretamente a sigla de seu candidato
		while votação_vereador != "V1" and votação_vereador != "V2" and votação_vereador != "V3" and votação_vereador != "V4" and votação_vereador != "VB" and votação_vereador != "VN":
			print("\n* Escolha inválida, o processo está reiniciando.. *\n")
			print("Por favor, digite corretamente a sua opção 😊 \n")

			time.sleep(5)
			limpar_terminal()

			print(""" \n
Opções de voto para VEREADORES: 

V1: Candidato 1 
V2: Candidato 2
V3: Candidato 3
V4: Candidato 4
VB: Voto BRANCO ⚪
VN: Voto NULO ⚫
""")

			votação_vereador = input("Digite a sigla de seu candidato a vereador ou outra opção: ")

		time.sleep(2)
		limpar_terminal()

		print("\n* Seus votos já foram cadastrados! * ✅\n") #primeira heurística de Nilsen
		

	elif idade < 16 and idade > 0:
		print("\nInapto a votação. Aguarde até completar 16 (dezesseis) anos 😊")
		
	else:
		print("\nIdade inválida. Por favor digite corretamente a sua idade 😊")

	if idade >= 16 and idade <= 115:
		print("\nVoto para prefeito:", votação_prefeito)
		print("Voto para vereador:", votação_vereador)


	elif idade < 16:
		verificar = 1
		print("\nProcesso encerrado!")

	print("\nAguarde alguns instantes...")
	print("\nEstamos computando seus dados... 😊")

	time.sleep(12) #12 segundos para a urna "computar"
	limpar_terminal()

	while True:
		if idade < 16 or idade > 115:
			break
		#Opções para o eleitor prosseguir com o processo ou se deseja refazê-lo
		try:
			verificar = int(input("\nDigite (1) para confirmar suas escolhas, ou digite (2) se deseja anular suas escolhas e refazer o processo: "))
		except ValueError:
			verificar = 1
			print("\n* Por favor, digite uma opção válida *")
			continue #Continuar loop até o usuário digitar a opção correta

		if verificar == 2:
			print("\nNão se preocupe, iremos reiniciar o seu processo de votação 😊\n")
			if idade >= 16:

				#Cuidando de erros de contabilidade dos votos para partidos PDB
				if votação_prefeito == "C1" or votação_prefeito == "C2" or votação_vereador == "V1" or votação_vereador == "V2" and pdb > 0:
					pdb -= tirar_pdb #Se opção 2, então - tiramos pontos dos partidos

				#Cuidando de erros de contabilidade dos votos para partidos PSB
				elif votação_prefeito == "C3" or votação_prefeito == "C4" or votação_vereador == "V3" or votação_vereador == "V4" and psb > 0:
					psb -= tirar_psb #Se opção 2, então - tiramos pontos dos partidos


				try:
					#para anular as escolhas - o total_prefeito simplesmente não recebe nada
					total_prefeito[votação_prefeito] += 0
					total_vereador[votação_vereador] += 0
				except KeyError:
					votos_brancos_prefeito += 0
					votos_brancos_vereador += 0
					continue
				break		
			else:
				#previnir erros para menores
				None

		elif verificar == 1:

			tirar_pdb = 0 
			tirar_psb = 0
			print("\nO processo foi devidamente concluído! ✅")
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
				break
			else:
				#previnir erros para menores
				None
				break

		else:
			print("Opção inválida")	


	print("\nPressione 'ENTER' encerrar sua sessão.")
	confirmar = input()
	limpar_terminal()


# * Votação (de uma Seção Eleitoral) *

#IDENTIFICAÇÃO DA URNA ELETRÔNICA
print("\nSeção:", seção, "\nZona eleitoral:", zona_eleitoral,"\n")
print("Código de Identificação da Urna Eletrônica:",código_identificação_ue,"\n")

#Quantos eleitores podem votar
print("Total dos Eleitores que podem votar:",apto,"\n")

#decoração
print("\nx-------------------------------------------------------------------x\n")

# * Totalização
print(" 🚨 Ranking das eleições! 🚨 \n")
print("Rank dos prefeitos:", total_prefeito, "\n")
print("Rank dos vereadores:", total_vereador)


# * Divulgação dos Resultados *


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

#decoração
print("\nx-------------------------------------------------------------------x")

#Mostrando votos por patido
print("\nNúmero de votos para o partido PDB:", pdb,"\n")
print("Número de votos para o partido PSB:", psb,"\n")

#decoração
print("x-------------------------------------------------------------------x")

#Verificando possível empate
#Condição de empate duplo
if lista_total_prefeito[-1][1] == lista_total_prefeito[-2][1] and lista_total_prefeito[-1][1] != 0 and lista_total_prefeito[-2][1] != 0:
	print(f"\nHouve um empate entre os candidatos a prefeito {lista_total_prefeito[-1]} e {lista_total_prefeito[-2]} e haverá um segundo turno!")

#Condição de empate triplo
elif lista_total_prefeito[-1][1] == lista_total_prefeito[-2][1] and lista_total_prefeito[-2][1] == lista_total_prefeito[-3][1] and lista_total_prefeito[-1][1] != 0 and lista_total_prefeito[-2][1] != 0 and lista_total_prefeito[-3][1] != 0:
	print(f"\nHouve um empate entre os candidatos a prefeito {lista_total_prefeito[-1]}, {lista_total_prefeito[-2]} e {lista_total_prefeito[-3]} e haverá um segundo turno!")

#Caso o usuário somente digite votos BRANCOS ou NULOS - mostrar que houve um "equivoco"
elif lista_total_prefeito[-1][1] == 0:
	print(' 🚨 Houve um "equívoco" nas eleições dos prefeitos, e haverá um novo turno 🚨 ')

else:
	#resultados das votações para prefeito
	print("\n🔰 Candidato a Prefeito mais votado:", lista_total_prefeito[-1])


print("\n⚪ Votos Brancos na votação para Prefeitos:", votos_brancos_prefeito)	
print("⚫ Votos Nulos na votação para Prefeitos:", votos_nulos_prefeito)

#decoração
print("\nx-------------------------------------------------------------------x")

#Condição de empate duplo
if lista_total_vereador[-1][1] == lista_total_vereador[-2][1] and lista_total_vereador[-1][1] != 0 and lista_total_vereador[-2][1] != 0:
	print(f"\nHouve um empate entre os candidatos a vereador {lista_total_vereador[-1]} e {lista_total_vereador[-2]} e haverá um segundo turno!")

#Condição de empate triplo
elif lista_total_vereador[-1][1] == lista_total_vereador[-2][1] and lista_total_vereador[-2][1] == lista_total_vereador[-3][1] and lista_total_vereador[-1][1] != 0 and lista_total_vereador[-2][1] != 0 and lista_total_vereador[-3][1] != 0:
	print(f"\nHouve um empate entre os candidatos a prefeito {lista_total_vereador[-1]}, {lista_total_vereador[-2]} e {lista_total_vereador[-3]} e haverá um segundo turno!")

#Caso o usuário somente digite votos BRANCOS ou NULOS - mostrar que houve um "equivoco"
elif lista_total_vereador[-1][1] == 0:
	print('\n 🚨 Houve um "equívoco" nas eleições dos vereadores, e haverá um novo turno 🚨 ')

else: 
	#resultados das votações para vereador
	print("\n🔰 Candidato a Vereador mais votado:", lista_total_vereador[-1])


print("\n⚪ Votos Brancos na votação para Vereador:", votos_brancos_vereador)
print("⚫ Votos Nulos na votação para Vereador:", votos_nulos_vereador)


#Fim do programa
#Aproximadamente 26 horas de desenvolvimento