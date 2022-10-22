from multiprocessing.util import ForkAwareThreadLock
from Joueur import*
from Jeu_carte import Jeu_carte
from math import*
import pygame
from pygame.locals import *
import time
from Carte import Carte

class Game:
    """
    Cette classe gere le deroulement de la partie
    """
    def __init__(self,scale):
        #initialisation des attibuts
        self.joueurs=list()
        for i in range(5):
            self.joueurs.append(Joueur(i+1))
        self.joueurs.append(Banquier())

        self.talon=Jeu_carte(6)

        self.tailleecran = scale



    def distribuer(self):
        for ii in range(2):
            for i in range(6-ii):
                self.joueurs[i].cartes.append(self.talon.jeu.depiler())

        for i in range(self.nbrplayer):
            self.joueurs[i].miser()

    def recalculate(self):


        if self.nbrplayer==1:
            self.poscarte = (self.tailleecran[0]*15/32,self.tailleecran[1] * 22/36)
        elif self.nbrplayer==2:
            self.poscarte = (self.tailleecran[0]*277/512,self.tailleecran[1] * 22/36)
        elif self.nbrplayer==3:
            self.poscarte = (self.tailleecran[0]*81/128,self.tailleecran[1] * 22/36)
        elif self.nbrplayer==4:
            self.poscarte = (self.tailleecran[0]*361/512,self.tailleecran[1] * 22/36)
        elif self.nbrplayer==5:
            self.poscarte = (self.tailleecran[0]*51/64,self.tailleecran[1] * 22/36)
        self.poscarteB = (self.tailleecran[0]*15/32,self.tailleecran[1] * 5/36)


        self.espace = self.tailleecran[0] * 21/128
        self.potposition = self.tailleecran[1] * 103/108
        self.cercletaille = self.tailleecran[0] * 1/96
        self.hauteurcercle = self.tailleecran[1] * 47/54



    def dessinerBase(self):
        """
        Cette methode prend en parametre le nombre de joueur de type (int)
        Et dessine la table de base dans le mode graphique en fonction du nombre de joueur
        """
        VERT = (57,186,55)
        ROUGE = (255,67,67)
        fond = pygame.image.load("../img/plateau.png").convert()
        fond = pygame.transform.scale(fond, (self.tailleecran[0],self.tailleecran[1]))
        self.window.blit(fond,(0,0))
        for i in range(self.nbrplayer):
            pygame.draw.circle(self.window, VERT, [self.poscarte[0] - self.espace *i + self.cercletaille, self.hauteurcercle], self.cercletaille)
            pygame.draw.circle(self.window, ROUGE, [self.poscarte[0] - self.espace *i +5*self.cercletaille, self.hauteurcercle], self.cercletaille)


    def dessinerCarte(self):
        """
        Cette methode prend trois parametre:
        - carte (obj type carte)
        - i (int) qui correspond au joueur a qui dessiner la carte
        - y (int) qui correspond au nombre de carte du joueur pour que se decale dans l'affichage graphique
        Cette methode dessine les cartes des joueurs dans le mode graphique du jeu
        """
        for i in range(self.nbrplayer):
            for ii in range(len(self.joueurs[i].cartes)):
                cartecharger=str(self.joueurs[i].cartes[ii].valeur)+str(self.joueurs[i].cartes[ii].couleur)
                carte= pygame.image.load(f"../img/{cartecharger}.png").convert_alpha()
                carte = pygame.transform.scale(carte, (1/16*self.tailleecran[0], 7/45*self.tailleecran[1]))
                self.window.blit(carte,(self.poscarte[0]-self.espace*i+self.cercletaille*ii,self.poscarte[1]-self.cercletaille*ii*2))

        for iii in range(len(self.joueurs[5].cartes)):
            cartecharger=str(self.joueurs[5].cartes[iii].valeur)+str(self.joueurs[5].cartes[iii].couleur)
            carte= pygame.image.load(f"../img/{cartecharger}.png").convert_alpha()
            carte = pygame.transform.scale(carte, (1/16*self.tailleecran[0], 7/45*self.tailleecran[1]))
            self.window.blit(carte,(self.poscarteB[0]-self.cercletaille*iii,self.poscarteB[1]+self.cercletaille*iii*2))



    def dessinePot(self):
        """
        Cette methode ne prend pas de parametre et dessine les pots des joueurs dans le mode graphique du jeu
        """
        BLANC=(255,255,255)
        base_font = pygame.font.SysFont(None,int(1/25*self.tailleecran[1]))
        for i in range(self.nbrplayer):
            self.window.blit(base_font.render(f"J{i+1} Pot : {self.joueurs[i].pot}", True , BLANC),(self.poscarte[0] - self.espace*i, self.potposition))



    def gagne(self):
        bljk=list()
        blcjck=list()
        text=list()
        loose=False
        for i in range(self.nbrplayer):
            self.joueurs[i].blackJack()
            if self.joueurs[i].isBlackJack:
                blcjck.append(self.joueurs[i])
                bljk.append(self.joueurs[i])
        self.joueurs[5].blackJack()
        if self.joueurs[5].isBlackJack:
            blcjck.append(self.joueurs[5])
            text.append("Le banquier a un blackjack. Les joueurs ayant un blackjack reprenne leur mise")
            loose= True

        if not loose:
            for i in range(len(bljk)):
                text.append(f"Le joueur : {bljk[i].nom} a un blackjack et gagne 30jetons")
                bljk[i].gagneJeton(30)


        if loose ==False:
            if self.joueurs[5].isPerdu:
                for i in range(self.nbrplayer):
                    if not self.joueurs[i].isPerdu and not self.joueurs[i].isBlackJack:
                        text.append(f"Le joueur : {self.joueurs[i].nom} gagne 24jetons")
                        self.joueurs[i].gagneJeton(24)

            else:
                for i in range(self.nbrplayer):
                    if not self.joueurs[i].isPerdu and not self.joueurs[i].isBlackJack:

                        if self.joueurs[i].calculPoints()>self.joueurs[5].calculPoints():
                            self.joueurs[i].gagneJeton(24)
                            text.append(f"Le joueur : {self.joueurs[i].nom} gagne 24jetons")


                    if not self.joueurs[i].isPerdu and not self.joueurs[i].isBlackJack:

                        if self.joueurs[i].calculPoints()==self.joueurs[5].calculPoints():
                            self.joueurs[i].gagneJeton(12)
                            text.append(f"Le joueur : {self.joueurs[i].nom} est égalité avec le banquier, il gagne 12jetons")



        self.dessineGagnant(text,(0,0,0))



    def dessineGagnant(self,text,coul):
        base_font = pygame.font.SysFont(None,int(5/100*self.tailleecran[1]))
        for o in range(len(text)):
            self.window.blit(base_font.render(text[o], True , coul),(self.tailleecran[0]*1/40 , self.tailleecran[1]*1/40+self.espace*o*5/40))


    def run1(self):
        open = True
        menu = True
        jouer = False
        self.joue = list()
        self.window=pygame.display.set_mode(self.tailleecran, pygame.RESIZABLE)
        pygame.display.set_caption("BlackJack")


        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    open = False

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    coo=event.pos

                    if 677<coo[0]<900 and 300<coo[1]<360:
                        self.nbrplayer=1
                        menu = False
                    elif 677<coo[0]<900 and 360<coo[1]<418:
                        self.nbrplayer=2
                        menu = False
                    elif 677<coo[0]<900 and 418<coo[1]<474:
                        self.nbrplayer=3
                        menu = False
                    elif 677<coo[0]<900 and 474<coo[1]<525:
                        self.nbrplayer=4
                        menu = False
                    elif 677<coo[0]<900 and 525<coo[1]<589:
                        self.nbrplayer=5
                        menu = False


            fond = pygame.image.load("../img/menu.png").convert()
            fond = pygame.transform.scale(fond, (self.tailleecran[0],self.tailleecran[1]))
            self.window.blit(fond,(0,0))
            pygame.display.flip()


        self.distribuer()
        self.recalculate()

        while open:
            if self.talon.jeu.pos<156:
                self.talon = Jeu_carte(6)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    open = False

                click=False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    coo=event.pos
                    for i in range(self.nbrplayer):
                        if self.poscarte[0] - self.espace *i + self.cercletaille - self.cercletaille < coo[0] < self.poscarte[0] - self.espace *i + self.cercletaille+ self.cercletaille and self.hauteurcercle - self.cercletaille <coo[1]<self.hauteurcercle + self.cercletaille:
                            click=True
                            jouer=True
                            self.joue.append(i)

                        elif self.poscarte[0] - self.espace *i +5*self.cercletaille - self.cercletaille < coo[0] < self.poscarte[0] - self.espace *i +5*self.cercletaille + self.cercletaille and self.hauteurcercle - self.cercletaille <coo[1]<self.hauteurcercle + self.cercletaille:
                            self.joueurs[i].fin = True


            for i in range(5):
                if self.joueurs[i].calculPoints()>21:
                    self.joueurs[i].isPerdu = True
                    self.joueurs[i].fin = True

            if jouer == True and click == False:
                new_list = []
                for i in self.joue:
                    if i not in new_list:
                        new_list.append(i)
                for el in new_list:
                    if not self.joueurs[el].isPerdu:
                        self.joueurs[el].carteEnPlus(self.talon.jeu.depiler())
                jouer = False
                self.joue = list()

            if self.tailleecran != pygame.display.get_surface().get_size():
                self.tailleecran = pygame.display.get_surface().get_size()
                self.recalculate()

                self.dessinerBase()

            self.dessinerBase()
            self.dessinerCarte()
            self.dessinePot()


            finish=True
            for i in range(self.nbrplayer):
                if self.joueurs[i].fin == False:
                    finish = False

            if finish:
                self.joueurs[5].coup_banquier_ia(self.talon)
                if self.joueurs[5].calculPoints()>21:
                    self.joueurs[5].isPerdu=True
                self.dessinerCarte()
                self.gagne()



                for i in range(6):
                    self.joueurs[i].miseZero()
                    self.joueurs[i].rendreCarte()
                    self.joueurs[i].isBlackJack=False
                    self.joueurs[i].isPerdu=False
                    self.joueurs[i].fin=False

            pygame.display.flip()




            if finish:
                time.sleep(5)
                self.distribuer()

        pygame.quit()






