#-*- coding: utf-8 -*-

import random
import os
import time

X = -1
O = OPEN = 1
CLOSE = 0

class Table:

	def __init__(self):
		self.internalTable = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.externalTable = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

	def show(self):
		k = 0
		n = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
		for i in range(3):
			for j in range(3):
				if(self.externalTable[i][j]) == CLOSE:
					print(n[k], end="\t")

				elif(self.externalTable[i][j]) == OPEN:
					if(self.internalTable[i][j]) == X:
						print("ⵝ", end="\t")

					elif(self.internalTable[i][j]) == O:
						print("ⵔ", end="\t")
				k += 1
			print("\n")
		print("\n")

	def checkLine(self):
		total = 0
		for i in range(3): # FILAS
			row = 0
			colum = 0
			firstDiagonal = 0
			secondDiagonal = 0
			for j in range(3):
				row += self.internalTable[i][j]
				colum += self.internalTable[j][i]
				firstDiagonal += self.internalTable[j][j]
				secondDiagonal += self.internalTable[j][2-j]
				total += self.externalTable[i][j]
				if(row == -3 or colum == -3 or firstDiagonal == -3 or secondDiagonal == -3):
					return 1

				elif(row == 3 or colum == 3 or firstDiagonal == 3 or secondDiagonal == 3):
					return 2

		if(total == 9): return 3
		return 0

	def setMove(self,player,turn):
		if(self.externalTable[turn[0]][turn[1]] == CLOSE):
			self.externalTable[turn[0]][turn[1]] = OPEN
			self.internalTable[turn[0]][turn[1]] = player
			return True
		else: 
			print("Esta casilla ya ha sido abierta")
			return False

	def checkGame(self):
		if(self.checkLine()) == 1:
			os.system("clear")
			self.show()
			print("HA GANADO ⵝ\n")
			return True

		elif(self.checkLine()) == 2:
			os.system("clear")
			self.show()
			print("HA GANADO ⵔ\n")
			return True

		elif(self.checkLine()) == 3:
			os.system("clear")
			self.show()
			print("EMPATE\n")
			return True

		return False


class Player:

	def __init__(self,player=X):
		self.player = player
		self.turn = [0,0]

	def play(self):
		while True:
			try:
				op = int(input("Ingrese el numero de la casilla: "))
				if(1 <= op <= 3):
					self.turn[0] = 0
					self.turn[1] = op - 1
					break

				elif(4 <= op <= 6):
					self.turn[0] = 1
					self.turn[1] = (op - 1) % 3
					break

				elif(7 <= op <= 9):
					self.turn[0] = 2
					self.turn[1] = (op - 4) % 3
					break

				else:
					print("Opcion Incorrecta")
			except:
				print("Opcion incorrecta")
		return self.turn

	def setPlayer(self):
		while True:
			os.system("clear")
			try:
				op = input("Que desea ser X o O?: ")
				if op.upper() == "X": 
					self.player = X
					break

				elif op.upper() == "O":
					self.player = O
					break

				else:
					print("Opcion Incorrecta")
			except:
				print("Opcion Incorrecta")

class Bot(Player):

	def __init__(self,player,table):
		Player.__init__(self,player)
		self.player *= -1
		self.table = table

	def play(self):
		while True:
			self.turn[0] = random.randint(0, 2)
			self.turn[1] = random.randint(0, 2)
			if(self.table.externalTable[self.turn[0]][self.turn[1]] == CLOSE): break

		print("CPU esta jugando")
		time.sleep(0.75)
		print(".",)
		time.sleep(0.5)
		print(".",)
		time.sleep(0.25)
		print(".")
		time.sleep(0.1)
		return self.turn

class Game:

	def __init__(self):
		self.p1 = Player(X)
		self.p2 = Player(O)
		self.table = Table()
		self.isSinglePlayer = False
		self.isPlayAgain = True

	def start1(self):
		while True:
			os.system("clear")
			self.table.show()
			self.printTurn(self.p1.player)
			while True:
				if(self.table.setMove(self.p1.player,self.p1.play())): break
			if(self.table.checkGame()): break

			else:
				os.system("clear")
				self.table.show()
				self.printTurn(self.p2.player)
				while True:
					if(self.table.setMove(self.p2.player,self.p2.play())): break
				if(self.table.checkGame()): break

	def play(self):
		while True:
			for player in [self.p1,self.p2]:
				os.system("clear")
				self.table.show()
				self.printTurn(player.player)
				while True:
					if(self.table.setMove(player.player,player.play())): break
				if(self.table.checkGame()): return True


	def selectGame(self):
		while True:
			os.system("clear")
			print("Elija el tipo de juego:\n\n1. vs CPU\n\n2. 2 Jugadores\n")
			try:
				op = int(input("Opcion: "))
				if(op == 1):
					self.isSinglePlayer = True
					break
				elif(op == 2): break

				else:
					print("Opcion Incorrecta")
					os.system("clear")
			except:
				print("Opcion Incorrecta")
				os.system("clear")

	def singlePlayer(self):
		self.p1.setPlayer()
		self.p2 = Bot(self.p1.player,self.table)

	def printTurn(self,player):
		if(player == X):
			print("Turno de ⵝ")
		elif(player == O):
			print("Turno de ⵔ")

	def playAgain(self):
		while True:
			print("Desea volver a jugar? s/n")
			op = input("Opcion: ")
			if op.upper() == "S":
				self.table.__init__()
				self.__init__()
				break
			elif op.upper() == "N":
				self.isPlayAgain = False
				break
			else:
				print("Opcion Incorrecta!!")
				os.system("clear")

	def menu(self):
		os.system("clear")
		print("   .ooodool ::   ,oooo'   'ooddoo;  'x.     :dooo.   ;ooddoo' .ldodl.   doooo, ")
		print("      'M    xk  Kd           dk    .X:X.  .Xc           0o   ;X'   .Xl  M'        ")
		print("      'M    xk :W            dk   .X' :X  oK            0o   Kl     cW  Mxlll     ")
		print("      'M    xk .W,           dk   0OlllKk ,W.           0o   d0     OO  M'        ")
		print("      .N    dd  .kxooo;      od  ck     0: ,kxooo.      kc    :kdodkl   Xxoool    ")
		print("\n1. Jugar\n2. Salir\n")
		while True:
			try:
				op = int(input("Opcion: "))
				if(op == 1): return True
				elif(op == 2):
					print("Gracias por jugar")
					return False
				else: print("Opcion Incorrecta")
			except:
				print("Opcion Incorrecta")




def main():
	game = Game()
	while(game.menu()):
		while(game.isPlayAgain):
			game.selectGame()
			if(game.isSinglePlayer):
				game.singlePlayer()
			game.play()
			game.playAgain()
main()



