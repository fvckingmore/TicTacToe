#-*- coding: utf-8 -*-

import random
import os
import time


#----------------------------
#-----FUNCION: PRINCIPAL-----
#----------------------------


def main():

	while True:

		if f_menu() == 1:

			os.system("clear")

			while True:

				os.system("clear")

				mint = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
				mext = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

				if f_tipo_juego() == 2:

					animacion()

					while True:

						if f_2players(mint, mext) == 1:
							break

				else:

					while True:

						try:
							op = input("Que desea ser X o O?: ")

							if op.upper() == "X" or op.upper() == "O":
								break

							else:
								print("Opcion Incorecta")

						except:
							print("Opcion Incorrecta")

					animacion()

					while True:

						if f_1player_easy(op, mint, mext) == 1:
							break

				if not f_volver_jugar():
					break

		else:
			break

	print("Gracias por jugar")


#----------------------------------
#-----FUNCION: MUESTRA TABLERO-----
#----------------------------------

## LISTO
def f_mostrar(mint, mext):

	k = 0
	n = ("", "", "", "", "", "", "", "", "")

	for i in range(3):

		for j in range(3):

			if mext[i][j] == 0:
				print(n[k], end="\t")

			elif mext[i][j] == 1:

				if mint[i][j] == -1:
					print("ⵝ", end="\t")

				elif mint[i][j] == 1:
					print("ⵔ", end="\t")

			k += 1

		print("\n")

	print("\n")
	# print(mint)
	# print(mext)




#-----------------------------------------
#-----FUNCION: VERIFICAR SI HA GANADO-----
#-----------------------------------------


def f_verificar(mint, mext):

	b = 0
	su = 0

	#---FILAS---

	for i in range(3):

		s = 0

		for j in range(3):

			s += mint[i][j]

			if s == -3:
				b = 1
				break

			elif s == 3:
				b = 2
				break

		# print("s = ", s)  # DEPURACION

	#---COLUMNAS---

	if b == 0:

		for i in range(3):

			s = 0

			for j in range(3):

				s += mint[j][i]

				if s == -3:
					b = 1
					break

				elif s == 3:
					b = 2
					break
		# print("s = ", s)  # DEPURACION

	#---DP---

	if b == 0:

		s = 0

		for i in range(3):

			s += mint[i][i]

			if s == -3:
				b = 1
				break

			elif s == 3:
				b = 2
				break
		# print("s = ", s)  # DEPURACION

	#---DS---

	if b == 0:

		s = 0
		j = 2

		for i in range(3):

			s += mint[i][j]
			j -= 1

			if s == -3:
				b = 1
				break

			elif s == 3:
				b = 2
				break
		# print("s = ", s)  # DEPURACION

	#---VERIFICAR CASILLAS LLENAS

	if b == 0:

		for i in range(3):

			for j in range(3):

				su += mext[i][j]
		# print("su = ", su)  # DEPURACION

		if su == 9:
			return 3

	return b


#---------------------------
#-----FUNCION JUGADOR 1-----
#---------------------------


def f_player1(mint, mext):

	print("Turno de ⵝ\n")
	fila_usr, colum_usr = f_usr(mext)
	mext[fila_usr][colum_usr] = 1
	mint[fila_usr][colum_usr] = -1


#---------------------------
#-----FUNCION JUGADOR 2-----
#---------------------------


def f_player2(mint, mext):

	print("Turno de ⵔ\n")
	fila_usr, colum_usr = f_usr(mext)
	mext[fila_usr][colum_usr] = 1
	mint[fila_usr][colum_usr] = 1


#--------------------------------
#-----FUNCION VOLVER A JUGAR-----
#--------------------------------


def f_volver_jugar():

	while True:

		print("Desea volver a jugar? s/n")
		op = input("Opcion: ")

		if op.upper() == "S":
			return True

		elif op.upper() == "N":
			return False

		else:
			print("Opcion Incorrecta!!")
			os.system("clear")


#-----------------------------
#-----FUNCION 2 JUGADORES-----
#-----------------------------


def f_2players(mint, mext):

	os.system("clear")
	f_mostrar(mint, mext)
	f_player1(mint, mext)

	if f_verificar(mint, mext) == 1:

		os.system("clear")
		f_mostrar(mint, mext)

		print("HA GANADO ⵝ\n")
		return 1

	elif f_verificar(mint, mext) == 3:

			os.system("clear")
			f_mostrar(mint, mext)
			print("EMPATE\n")
			return 1

	else:

		os.system("clear")
		f_mostrar(mint, mext)
		f_player2(mint, mext)

		if f_verificar(mint, mext) == 2:

			os.system("clear")
			f_mostrar(mint, mext)
			print("HA GANADO ⵔ\n")
			return 1

		elif f_verificar(mint, mext) == 3:

			os.system("clear")
			f_mostrar(mint, mext)
			print("EMPATE\n")
			return 1

	return 0


#--------------------------------------
#-----FUNCION ELEGIR TIPO DE JUEGO-----
#--------------------------------------


def f_tipo_juego():

	while True:

		print("Elija el tipo de juego:\n\n1. vs CPU\n\n2. 2 Jugadores\n")

		try:
			op = int(input("Opcion: "))

			if op == 1:
				return 1

			elif op == 2:
				return 2

			else:
				print("Opcion Incorrecta")
				os.system("clear")

		except:
			print("Opcion Incorrecta")
			os.system("clear")


def animacion():

	# os.system("clear")
	# print("CARGANDO PARTIDA")
	# time.sleep(1.5)
	# print(".",)
	# time.sleep(1)
	# print(".",)
	# time.sleep(0.5)
	# print(".")
	# time.sleep(0.25)
	# os.system("clear")

	b = "|"

	for i in "CARGANDO PARTIDA":

		os.system("clear")
		print("CARGANDO PARTIDA")
		print(b,)
		b += "|"
		time.sleep(0.07)


#-------------------------------
#-----FUNCION USUARIO_NUEVA-----
#-------------------------------

## LISTO

def f_usr(mext):

	while True:

		while True:

			try:

				op = int(input("Ingrese el numero de la casilla: "))

				if 1 <= op <= 3:
					fila_usr = 0
					colum_usr = op - 1
					break

				elif 4 <= op <= 6:
					fila_usr = 1
					colum_usr = (op - 1) % 3
					break

				elif 7 <= op <= 9:
					fila_usr = 2
					colum_usr = (op - 4) % 3
					break

				else:
					print("Opcion Incorrecta")

			except:
				print("Opcion incorrecta")

		if mext[fila_usr][colum_usr] == 0:
			break

		else:
			print("Esta casilla ya ha sido abierta")

	return fila_usr, colum_usr


#------------------------
#-----FUNCION ELEGIR-----
#------------------------


def f_elegir(op, mint, mext):

	if op.upper() == "X":
		f_player1(mint, mext)
		return "O"

	elif op.upper() == "O":
		f_player2(mint, mext)
		return "X"


#--------------------------------------------
#-----FUNCION DIFICULTAD CPU ULTRA FACIL-----
#--------------------------------------------


def f_cpu_easy(op, mint, mext):

	while True:

		fila_usr = random.randint(0, 2)
		colum_usr = random.randint(0, 2)

		if mext[fila_usr][colum_usr] == 0:
			break

	if op == "O":
		mext[fila_usr][colum_usr] = 1
		mint[fila_usr][colum_usr] = 1

	elif op == "X":
		mext[fila_usr][colum_usr] = 1
		mint[fila_usr][colum_usr] = -1

	print("CPU esta jugando")
	time.sleep(0.75)
	print(".",)
	time.sleep(0.5)
	print(".",)
	time.sleep(0.25)
	print(".")
	time.sleep(0.1)
	os.system("clear")


#-----------------------------------------------------
#----FUNCION 1 JUGADOR CON DIFICULTAD SUPER FACIL-----
#-----------------------------------------------------


def f_1player_easy(op, mint, mext):

	os.system("clear")
	f_mostrar(mint, mext)
	b = f_elegir(op, mint, mext)

	if f_verificar(mint, mext) == 1:

		os.system("clear")
		f_mostrar(mint, mext)
		print("HA GANADO ⵝ\n")
		return 1

	elif f_verificar(mint, mext) == 2:

			os.system("clear")
			f_mostrar(mint, mext)
			print("HA GANADO ⵔ\n")
			return 1

	elif f_verificar(mint, mext) == 3:

			os.system("clear")
			f_mostrar(mint, mext)
			print("EMPATE\n")
			return 1

	else:

		os.system("clear")
		f_mostrar(mint, mext)
		f_cpu_easy(b, mint, mext)

		if f_verificar(mint, mext) == 1:

			os.system("clear")
			f_mostrar(mint, mext)
			print("HA GANADO ⵝ\n")
			return 1

		elif f_verificar(mint, mext) == 2:

			os.system("clear")
			f_mostrar(mint, mext)
			print("HA GANADO ⵔ\n")
			return 1

		elif f_verificar(mint, mext) == 3:

			os.system("clear")
			f_mostrar(mint, mext)
			print("EMPATE\n")
			return 1

	return 0


#----------------------
#-----FUNCION MENU-----
#----------------------


def f_menu():

	while True:

		os.system("clear")

		print("   .ooodool ::   ,oooo'   'ooddoo;  'x.     :dooo.   ;ooddoo' .ldodl.   doooo, ")
		print("      'M    xk  Kd           dk    .X:X.  .Xc           0o   ;X'   .Xl  M'        ")
		print("      'M    xk :W            dk   .X' :X  oK            0o   Kl     cW  Mxlll     ")
		print("      'M    xk .W,           dk   0OlllKk ,W.           0o   d0     OO  M'        ")
		print("      .N    dd  .kxooo;      od  ck     0: ,kxooo.      kc    :kdodkl   Xxoool    ")

		print("\n1. Jugar\n2. Salir\n")

		try:
			op = int(input("Opcion: "))

			if op == 1 or op == 2:
				break

			else:
				print("Opcion Incorrecta")

		except:
			print("Opcion Incorrecta")

	return op


#----------------------------
#-----		INICIO		-----
#----------------------------


main()
