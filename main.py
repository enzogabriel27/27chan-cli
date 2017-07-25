from cliview import StartPage
import os

os.system("clear")
s = StartPage()
print(s.build_header())
print("b [NOME DA BOARD] para acessar.\n")

while True:
    board = input(">>")
