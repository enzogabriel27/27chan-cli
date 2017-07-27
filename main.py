from cliview import StartPage
import os
import sys

os.system("clear")
s = StartPage()
print(s.build_header())
print("b [NOME DA BOARD] para acessar, ou exit para sair.\n")

while True:
	board = input(">>")
	command = board.split()
	
	#verifica se está chamando uma board
	if (len(command) > 1 and command[0] == "b"):
		#TODO: aqui deve chamar uma classe que baixa a página da board e exibe na tela
		print("TODO: chamar a board " + command[1])
	
	#quero sair
	elif (board == "exit"):
		sys.exit()
	
	#tras a insulina
	else:
		print("Comando não reconhecido, tente mais duro.")