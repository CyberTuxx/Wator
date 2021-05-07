import random
from display import *

dict_type = "type"
dict_gest = "gestation"
dict_energ = "energie"

def create_thon(gestation):
    """
    :param gestation: (int) le temps de gestation
    :return: (dictionnaire) dictionnaire correpondant à un thon
    :Exemples:
    >>> create_thon(5)
    {'type': 0, 'gestation': 5}
    """
    return {dict_type : 0, dict_gest : gestation}

def create_requin(gestation, energie):
    """
    :param gestation: (int) le temps de gestation
    :param energie: (int) l'energie d'un requin
    :return: (dictionnaire) dictionnaire correpondant à un requin
    :Exemples:
    >>> create_requin(5, 10)
    {'type': 1, 'gestation': 5, 'energie': 10}
    """
    return {dict_type : 1, dict_gest : gestation, dict_energ : energie}

def thon_action(thon, thon_gestation):
    """
    :param thon: (dictionnaire) dictionnaire rempresentent toujours un thon
    :pram thon_gestation: (int) representant le temps de gestation thon
    :return: (tuple) tuple soit de 2 thons soit de 1 thon et un 0
    :Exemples:
    >>> thon_action(create_thon(5), 5)
    ({'type': 0, 'gestation': 4}, 0)
    """
    if(thon[dict_gest] == 0):
        thon[dict_gest] = thon_gestation
        return (thon, create_thon(thon_gestation))
    else:
        thon[dict_gest] -= 1
        return (thon, 0)

def requin_action(requin, requin_gestation, requin_energie):
    """
    :param requin: (dictionnaire) dictionnaire rempresentent toujours un requin
    :param requin_gestation: (int) representant le temps de gestation requin
    :param requin_energie: (int) represente l'energie d'un requin
    :return: (tuple) tuple soit de 2 requin soit de 1 requin et un 0
    :Exemples:
    >>> requin_action(create_requin(5, 10), 5, 10)
    ({'type': 1, 'gestation': 4, 'energie': 10}, 0)
    """
    if(requin[dict_energ] == 0):
            return (0, 0)
    elif(requin[dict_gest] == 0):
        requin[dict_gest] = requin_gestation
        return (requin, create_requin(requin_gestation, requin_energie))
    else:
        requin[dict_gest] -= 1
        requin[dict_energ] -= 1
        return (requin, 0)

def action(poisson, thon_gestation, requin_gestation, requin_energie):
    """
    :param poisson: (dictionnaire) dictionnaire representant un poisson (requin ou thon)
    :param thon_gestation: (int) representant le temps de gestation thon
    :param requin_gestation: (int) representant le temps de gestation requin
    :param requin_energie: (int) represente l'energie d'un requin
    :return: (tuple) tuple soit de 2 requins soit de 1 requin et un 0 ou de 2 thons soit de 1 thons et un 0
    :Exemples:
    >>> action(create_requin(5, 10), 5, 5, 10)
    ({'type': 1, 'gestation': 4, 'energie': 10}, 0)
    >>> action(create_requin(5, 10), 5, 5, 10)
    ({'type': 1, 'gestation': 4, 'energie': 10}, 0)
    """
    if(poisson[dict_type] == 0):
        return thon_action(poisson, thon_gestation)
    else:
        return requin_action(poisson, requin_gestation, requin_energie)

def remplir_grille(grille, rand_thon, rand_requin, thon_gestation, requin_gestation, requin_energie):
    """
    :param grille: (liste de liste) liste 2d representant la grille de jeu
    :param rand_thon: (int) representant le nombre de thon pour 100 casses
    :pram rand_requin: (int) representant le nombre de requins pour 100 casses
    :param thon_gestation: (int) representant le temps de gestation d'un thon
    :param requin_gestation: (int) represntant le temps de gestation d'un requin
    :param requin_energie: (int) representant l'energie d'un requin
    :return: (liste de liste) liste remplie avec rand_thon/100 thon et rand_requin/100 de requins le reste est 0
    """
    for i in range(0, len(grille)):
        for j in range(0, len(grille[i])):
            r = random.randrange(0, 100)
            if(r <= rand_thon):
                grille[i][j] = create_thon(thon_gestation)
            elif(r <= rand_thon + rand_requin):
                grille[i][j] = create_requin(requin_gestation, requin_energie)
    return grille

def is_empty(grille, x, y):
    """
    :param grille: (liste de liste) liste 2d representant la grille de jeu
    :param x: (int) coordonnee en abscise de la case à tester
    :param y: (int) coordonnee en ordonne de la case à tester
    :return: (boolean) return True si la case est vide sinon False
    """
    if(grille[x][y] == 0):
        return True
    else:
        return False
        
def is_requin(grille, x, y):
    return grille[x][y][dict_type] == 1

def can_move(grille, x, y, old_x, old_y):
    """
    :param grille: (liste de liste) liste 2d representant la grille de jeu
    :param x: (int) coordonne en abscise de la nouvelle case
    :param y: (int) coordonne en ordonne de la nouvelle case
    :param old_x: (int) coordonne en abscise de l'ancienne case
    :param old_y: (int) coordonne en ordonne de l'ancienne case
    :return: (boolean) return True l'objet present au coordonne (old_x, old_y) peut bouger vers (x, y)
    """
    if(is_empty(grille, x, y)):
        return True
    elif(grille[x][y][dict_type] != grille[old_x][old_y][dict_type]):
        return True
    else:
        return False

def random_except(start, end, ex):
    """
    FUNCTION TEST
    """
    if len(ex) >= (end - start):
        return -1
    else:
        r = random.randrange(start, end)
        while(r in ex):
            r = random.randrange(start, end)
        return r

def real_move(x, y, old_x, old_y, grille, thon_gesta, requin_gesta, requin_ener):
        if(is_requin(grille, old_x, old_y) and not is_empty(grille, x, y)):
                grille[old_x][old_y][dict_energ] = requin_ener + 1
        grille[x][y], new = action(grille[old_x][old_y], thon_gesta, requin_gesta, requin_ener)
        if(new != 0):
                grille[old_x][old_y] = new
        else:
                grille[old_x][old_y] = 0


def move(i, j, grille, r, thon_gesta, requin_gesta, requin_ener, ex=[]):
    new_x = i
    new_y = j
    if(r == 0):
        #move_right
        if((new_y + 1) >= size_x):
            new_y = (new_y + 1) - size_x
        else:
            new_y = new_y + 1
        if(can_move(grille, new_x, new_y, i, j)):
            real_move(new_x, new_y, i, j, grille, thon_gesta, requin_gesta, requin_ener)
        else:
                ex.append(0)
                move(i, j, grille, random_except(0, 4, ex), thon_gesta, requin_gesta, requin_ener, ex) 
    elif(r == 1):
        if((new_y - 1) < 0):
            new_y = (new_y - 1) + size_x
        else:
            new_y = new_y - 1
        if(can_move(grille, new_x, new_y, i, j)):
            real_move(new_x, new_y, i, j, grille, thon_gesta, requin_gesta, requin_ener)
        else:
            ex.append(1)
            move(i, j, grille, random_except(0, 4, ex), thon_gesta, requin_gesta, requin_ener, ex) 
    elif(r == 2):
        if((new_x + 1) >= size_x):
            new_x = (new_x + 1 ) - size_x
        else:
            new_x = new_x + 1
        if(can_move(grille, new_x, new_y, i, j)):
            real_move(new_x, new_y, i, j, grille, thon_gesta, requin_gesta, requin_ener)
        else:
            ex.append(2)
            move(i, j, grille, random_except(0, 4, ex), thon_gesta, requin_gesta, requin_ener, ex) 
    elif(r == 3):
        if((new_x - 1) < 0):
            new_x = (new_x - 1) + size_x
        else:
            new_x = new_x - 1
        if(can_move(grille, new_x, new_y, i, j)):
            real_move(new_x, new_y, i, j, grille, thon_gesta, requin_gesta, requin_ener)
        else:
            ex.append(3)
            move(i, j, grille, random_except(0, 4, ex), thon_gesta, requin_gesta, requin_ener, ex) 
    else:
        action(grille[new_x][new_y], thon_gesta, requin_gesta, requin_ener)
        
def search_thon(grille, x, y):
    new_x = x
    new_y = y
    liste = []
    if((new_y + 1) >= size_x):
        new_y = (new_y + 1) - size_x
    else:
        new_y = new_y + 1
    if(is_empty(grille, new_x, new_y)):
        liste.append(0)
    elif(is_requin(grille, new_x, new_y)):
        liste.append(0)
    if((new_y - 1) < 0):
        new_y = (new_y - 1) + size_x
    else:
        new_y = new_y - 1
    if(is_empty(grille, new_x, new_y)):
        liste.append(1)
    elif(is_requin(grille, new_x, new_y)):
        liste.append(1)
    if((new_x + 1) >= size_x):
        new_x = (new_x + 1 ) - size_x
    else:
        new_x = new_x + 1
    if(is_empty(grille, new_x, new_y)):
        liste.append(2)
    elif(is_requin(grille, new_x, new_y)):
        liste.append(2)
    if((new_x - 1) < 0):
        new_x = (new_x - 1) + size_x
    else:
        new_x = new_x - 1
    if(is_empty(grille, new_x, new_y)):
        liste.append(3)
    elif(is_requin(grille, new_x, new_y)):
        liste.append(3)
    if(len(liste) >= 4):
        return []
    else:
        return liste

def tour(grille, thon_gesta, requin_gesta, requin_ener):
    for i in range(0, len(grille)):
        for j in range(0, len(grille[i])):
            if not (is_empty(grille, i, j)):
                if is_requin(grille, i, j):
                    move(i, j, grille, random_except(0, 4, search_thon(grille, i, j)), thon_gesta, requin_gesta, requin_ener)
                else:
                    move(i, j, grille, random.randrange(0, 4), thon_gesta, requin_gesta, requin_ener)

def affichage(grille, thon_gestation, requin_gestation, requin_energie, fen):
        speed = 100
        tour(grille, thon_gestation, requin_gestation, requin_energie)
        fen.display_grille(grille, is_empty, is_requin)
        fen.next(speed, affichage, grille, thon_gestation, requin_gestation, requin_energie, fen)
        

size_x = 40
thon_gestation = 2
requin_gestation = 5
requin_energie = 5
rand_thon = 30
rand_requin = 10
grille = [[0 for _ in range (size_x)] for _ in range(size_x)]
remplir_grille(grille, rand_thon, rand_requin, thon_gestation, requin_gestation, requin_energie)
fen = Fenetre(size_x, size_x)
affichage(grille, thon_gestation, requin_gestation, requin_energie, fen)
        
"""if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
"""
