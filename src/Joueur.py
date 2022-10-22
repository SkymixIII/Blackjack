

class Joueur :
    """
	Cette class est un joueur de BlackJack
"""
    def __init__(self, nom=0, banquier = False):
        """
        Ce constructeur de la class Joueur prend un paramètre chaine de charactères "nom" et un booléen "banquier" avec une valeur de base sur False.
        Le constructeur initialise ensuite la classe joueur avec les attributs : nom(str), cartes(liste), pot(int), mise(int), isPerdu(bool), isBanquier(bool) 
        """
        self.nom=nom
        self.cartes = []
        self.pot = 100 
        self.mise = 0
        self.isPerdu = False
        self.isBanquier = banquier
        self.isBlackJack = False
        self.points= 0
        self.fin = False
        
        return
        
    def gagneJeton(self, jeton):
        """
        Cette méthode de la class Joueur prend un paramètre:
        -"jeton" (int)
        Puis ajoute celui ci à l'attribut "pot"
        """
        
        self.pot += jeton
        
        return
        
    def carteEnPlus(self, carte):
        """
        Cette méthode de la class Joueur prend un paramètre:
        - "carte" (int)
        Puis le rajoute à l'attribut "cartes"
        """
        
        self.cartes.append(carte)
        
        return
        
    def rendreCarte(self):
        """
        Cette méthode ne prend pas de paramètres et vide l'attribut "cartes"(lst)
        """
        
        self.cartes.clear()
        
        return
        
    def calculPoints(self):
        """
        Cette méthode ne prend pas de paramètres et renvoie les points du joueurs
        """
        
        points = 0
        cartesAs = []
        
        #on ajoute la valeur des cartes et ajoute dans une liste les as
        for i in range(len(self.cartes)):
            if self.cartes[i].valeur >= 10 :
                points += 10
            elif self.cartes[i].valeur == 1:
                cartesAs.append(i)
            else:
                points += self.cartes[i].valeur
                
        #on gere les points attribués pour chaque as (1 ou 11)
        if points>21:
            points+=1*len(cartesAs)
        else:
            if len(cartesAs)!=0: 
                i=0
                while points + 11*(len(cartesAs)-i)+i>21 and len(cartesAs)-i>0:
                    i+=1
                points+=11*(len(cartesAs)-i)+i
                
        self.points=points
        return points
        
    def blackJack(self):
        """
        Cette methode ne prend pas de paramètres modifie l'attribut isBlackJack sur True si le joueur à un BlackJack.
        """
        if self.points ==21 and len(self.cartes)==2:
            self.isBlackJack=True
                
    def miser(self):
        """
        Cette méthode ne prend pas de paramètres puis si le joueur à au moins 12 jeton la mise est égale à 12 et on soustrait 12 au pot dans le cas contraire la mise est égale à la valeur du pot et puis le pot est mis à 0 
        """
        
        if self.pot >= 12 :
            self.pot -= 12
            self.mise = 12
            
        else:
            self.mise = self.pot
            self.pot = 0
            
    def miseZero(self):
        """
        Cette méthode ne prend pas de paramètres puis remet la mise à 0
        """
        self.mise  = 0
        
class Banquier(Joueur):
    def __init__(self):
        super().__init__(nom =0,banquier = True)
        
    def coup_banquier_ia(self,talon) :
        """
        Cette fonction prend un paramètre:
        - un jeu_carte (obj type Jeu_carte) 
        Puis fais piocher le joueur tant qu'il a moins de points que 17
        """
        cartestmp=list()
        while self.calculPoints() < 17 :
            carte = talon.jeu.depiler()
            self.carteEnPlus(carte)
            cartestmp.append(carte)
            
        return cartestmp

            
        
        
    
        
