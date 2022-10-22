

class Pile:
    """Cette class gère un objet pile qui peut etre modifié par plusieurs méthodes: empiler() , depiler()"""
    def __init__(self,n):
        """Le constructeur initialise les variables tel que la liste qui contient la pile"""
        self.pile = [0 for i in range(n)]
        self.pos = 0
        
    def estPleine(self):
        """cette methode ne prend pas de parametre et renvoie un booleen en fonction de si la pile est pleine"""
        return len(self.pile)==self.pos
    
    def estVide(self):
        """cette methode ne prend pas de parametre et renvoie un boolean en fonction de si la pile est vide"""
        return self.pos==0  
         
    def empiler(self,e):
        """cette methode empile à la pile l'element e passé en paramètre """
        if not self.estPleine():
            self.pile[self.pos]=e
            self.pos+=1

    def depiler(self):
        """cette methode ne prend pas de parametre et depile le dernier element de la pile et le renvoie"""
        if not self.estVide():
            tmp= self.pile[self.pos-1]
            self.pos-=1
            return tmp
            
            
            
            
            
            
            
            

                
            
            
            
            
            
            
            
            
            