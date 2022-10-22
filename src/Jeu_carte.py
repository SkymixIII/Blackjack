from Carte import Carte
from random import shuffle
from Pile import Pile

class Jeu_carte:
	"""
	Cette classe creer un talon contenant plusieurs jeu de carte
	"""
	def __init__(self,nbr):
		"""Le constructeur ne prend pas de parametres et cree une pile contenant 4 jeux de cartes"""
		self.nbrc=nbr*52
		self.jeu = list()
		self.creerTalon(nbr)
		self.melangerLeTalon()
		self.ajouterDansUnePile()


	def creerJeuCarte(self):
		"""
		Cette methode ne prend pas de parametre et creer un jeu de carte 52 cartes
		"""
		# Pour 4 couleurs differentes
		for coul in range(1,5):
			# Pour 13 valeurs
			for val in range(1,14):
				self.jeu.append(Carte(coul, val))

	def creerTalon(self,n):
		"""
		Cette methode prend 1 parametre:
		- n (int)
		Et creer un talon de n jeu de carte
		"""
		# Pour n paquets de cartes
		for i in range(n):
			self.creerJeuCarte()


	def melangerLeTalon(self):
		"""
		Cette methode ne prend pas de parametre et melange le talon
		"""
		# Melanger le tas de cartes
		shuffle(self.jeu)

		# Importation du jeu dans une pile

	def ajouterDansUnePile(self):
		"""
		Cette methode ne prend pas de parametre et ajoute le talon dans la pile
		"""
		pile = Pile(self.nbrc)
		for i in range(self.nbrc):
			pile.empiler(self.jeu[i])
		self.jeu = pile






