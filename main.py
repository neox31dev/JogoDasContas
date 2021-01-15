import random
import os
import time

def cls():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def main():
	cls()
	arte_ascii = '''   ______            __            
  / ____/___  ____  / /_____ ______
 / /   / __ \/ __ \/ __/ __ `/ ___/
/ /___/ /_/ / / / / /_/ /_/ (__  ) 
\____/\____/_/ /_/\__/\__,_/____/  
        coded by neox#0001              '''
	print(arte_ascii,'\n') 

	#Gerar Contas Random
	numeros_random1 = random.randint(0,20)
	numeros_random2 = random.randint(0,10)

	#Gerar Tipo de Conta
	contas = ['/','+','-','x']
	contas_aleatorio = random.choice(contas)

	#Resposta
	print('Conta > '+str(numeros_random1)+contas_aleatorio+str(numeros_random2))
	resposta = input('Resposta > ')

	#Checkar Conta
	if contas_aleatorio == '/':
		contas_resultado = numeros_random1/numeros_random2

	elif contas_aleatorio == '+':
		contas_resultado = numeros_random1+numeros_random2

	elif contas_aleatorio == '-':
		contas_resultado = numeros_random1-numeros_random2

	elif contas_aleatorio == 'x':
		contas_resultado = numeros_random1*numeros_random2

	else:
		print('Erro')

	#Checkar se a conta está bem
	if resposta == str(contas_resultado):
		print('\nParabens acertaste :)')
		time.sleep(1.5)
		main()
	else:
		print('\nErraste :(')
		começar_denovo = input('Queres começar denovo? s/n ')

		if começar_denovo == 's':
			main()
		else:
			quit()

if __name__ == '__main__':
	main()