# Couleurs: Pique = 1 | Coeur = 2 | Carreau = 3 | Trefle = 4
# Valeurs: As = 1 | 2 = 2 | 3 = 3 | .... | Dame = 12 | Roi = 13 |
# La couleur 0 n'existe pas, les valeurs 0 et 1 non plus


class Carte:
	def __init__(self, couleur, valeur):
		self.couleur = couleur
		self.valeur = valeur
		if valeur > 10:
			self.puissance = 10
		elif valeur == 1:
			self.puissance = 11
		else:
			self.puissance = valeur

