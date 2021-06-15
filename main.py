Matrice_base = []  # Base de donnée contenat les noms des matrices actives


# Fonctions assurant le bon fonctionnement des méthodes de la classe Matrice
def create_matrice():
    name = str(input("Nommer votre matrice : "))
    nl = input("Combien de lignes : ")
    nc = input("Combien de colonnes : ")
    M = []
    i = 0
    if nl.isdigit() and nc.isdigit():
        nl = int(nl)
        nc = int(nc)
    else:
        pass
    while i < nl:
        L = input(f"Entrer la {i + 1} ligne : ")
        LL = L.split(" ")
        LLdigit = []
        for number in LL:
            if number.isdigit():
                LLdigit.append(int(number))
        if len(LLdigit) != nc:
            print("Erreur : Nombre de colonne non respecté.")
            continue
        M.append(LL)
        i += 1
    for i in range(0, nl):
        for j in range(0, nc):
            M[i][j] = int(M[i][j])
    globals()[name] = Matrice(M, name)
    Matrice_base.append(name)


def create_temp_object(Mn, Mp, opération, M_teeeemp):
    name = Mn + opération + Mp
    globals()[name] = Matrice(M_teeeemp, name)
    Matrice_base.append(name)
    return name


def unité_ou_zéro(n, fonction):
    M = []
    i = 0
    while i < n:
        L = n * " 0 "
        LL = L.split(" ")
        LLdigit = []
        for number in LL:
            if number.isdigit():
                LLdigit.append(int(number))
        LL = LLdigit
        M.append(LL)
        i += 1
    if fonction == True:
        for j in range(0, n):
            M[j][j] = 1
    for i in range(0, n):
        for j in range(0, n):
            M[i][j] = int(M[i][j])
    return M


def matrice_sans_i_j(M, ligne, colonne):
    M3 = M.copy()
    M3.pop(ligne - 1)
    for i in range(0, len(M3)):
        M3[i].pop(colonne - 1)
    return M3


def comatrice(M):
    m0 = M.copy()
    for i in range(0, len(M)):
        for j in range(0, len(M)):
            m0[i][j] = delta_1(matrice_sans_i_j(M, i, j))
    return m0


def matrice_sans_i_j_1(M, ligne, colonne):
    M3 = M.copy()
    M3.pop(ligne - 1)
    for i in range(0, len(M3)):
        M3[i].pop(colonne - 1)
    return M3


def delta_1(M):
    if len(M[0]) == 2:
        delt = float(M[0][0]) * float(M[1][1]) - float(M[0][1]) * float(M[1][0])
        return delt
    else:
        delt = 0
        for k in range(1, len(M)):
            s = (-1) ** (1 + k)
            u = s * M[0][k - 1]
            N = matrice_sans_i_j_1(M, 1, k)
            w = u * delta_1(N)
            delt += w
        return float(delt)


def diviser_liste(lst, n):
    final = []
    for x in range(0, len(lst), n):
        partie = lst[x: n + x]
        final.append(partie)
    return final


# Les parametres, les méthodes et l'affiche des entités "Matrices"
class Matrice:
    def __init__(self, M, name):
        self.M = M
        self.name = name

    def modif(self):
        name = self.name
        nl = len(self.get_matrice())
        nc = len(self.get_matrice()[0])
        M = []
        i = 0
        while i < nl:
            L = input(f"Entrer la {i + 1} ligne : ")
            LL = L.split(" ")
            LLdigit = []
            for number in LL:
                if number.isdigit():
                    LLdigit.append(number)
            LL = LLdigit
            if len(LL) != nc:
                print("Erreur : Nombre de colonne non respecté.")
                continue
            M.append(LL)
            i += 1
        globals()[name] = Matrice(M, name)

    def get_matrice(self):
        return self.M

    def somme_matrice(self, M1):
        nl, nc, nl1, nc1 = len(self.M), len(self.M[0]), len(M1), len(M1[0])
        M3 = []
        if nl == nl1 and nc == nc1:
            for i in range(0, len(M1)):
                L1 = []
                for j in range(0, nc):
                    somme = int(self.M[i][j]) + int(M1[i][j])
                    L1.append(somme)
                M3.append(L1)
            return M3
        else:
            print("Erreur : Les deux matrices doivent avoir le meme nombre de lignes et de colonnes.")

    def produit_matrice(self, M1):
        nl, nc, nl1, nc1 = len(self.M), len(self.M[0]), len(M1), len(M1[0])
        M3 = []
        if nc == nl1:
            for k in range(0, nl):
                l = []
                for j in range(0, nc1):
                    s = 0
                    for i in range(0, nc):
                        a = self.M[k][i] * M1[i][j]
                        s += int(a)
                    l.append(s)
                M3.append(l)
            return M3
        else:
            print("Erreur : Les deux matrices doivent avoir le même nombre de lignes et de colonnes.")

    def puissance_matrice(self, n):
        i = 0
        M = unité_ou_zéro(len(self.get_matrice()), True)
        while i < n:
            M = self.produit_matrice(M)
            i += 1
        return M

    def scalaire(self, a):
        name = self.name
        M = self.get_matrice()
        nl = len(self.get_matrice())
        nc = len(self.get_matrice()[0])
        for i in M:
            for j in range(0, len(i)):
                i[j] = a * int(i[j])
        return M

    def trace_matrice(self):
        nl, nc = len(self.M), len(self.M[0])
        M3 = []
        if nl != nc:
            return print("La trace d'une matrice rectangulaire n'existe pas.")
        else:
            tr = 0
            for i in range(nl):
                tr += self.M[i][i]
            return tr

    def matrice_sans_i_j(self, ligne, colonne):
        M3 = self.M.copy()
        M3.pop(ligne - 1)
        for i in range(0, len(M3)):
            M3[i].pop(colonne - 1)
        return M3

    def delta(self):
        M = self.M
        if len(M[0]) == 2:
            delt = float(M[0][0]) * float(M[1][1]) - float(M[0][1]) * float(M[1][0])
            return delt
        else:
            delt = 0
            for k in range(1, len(M)):
                s = (-1) ** (1 + k)
                u = s * M[0][k - 1]
                N = matrice_sans_i_j_1(M, 1, k)
                w = u * float(delta_1(N))
                delt += w
            return delt

    def display(self):
        print(self.name, ":")
        maxim = []
        coef_len = []
        for k in range(0, len(self.get_matrice()[0])):
            d = len(str(self.get_matrice()[0][k]))
            for i in self.get_matrice():
                o = len(str(i[k]))
                if o > d:
                    d = len(str(i[k]))
            maxim.append(d)
        maxim = maxim * len(self.get_matrice())
        maxim = maxim * len(self.get_matrice())
        all_coef = []
        for i in self.get_matrice():
            for j in i:
                all_coef.append(j)
        str_coef = all_coef.copy()
        for i in range(0, len(str_coef)):
            d = str(str_coef[i])
            str_coef[i] = d.center(maxim[i])
        str_coef = diviser_liste(str_coef, len(self.get_matrice()))
        for i in str_coef:
            print('  '.join(i))

    def transposition_matrice(self):
        M3 = []
        nl = len(self.get_matrice())
        nc = len(self.get_matrice()[0])
        if nl != nc:
            return print("La transposition ne se fait que sur les matrices carrées.")
        else:
            for j in range(nc):
                L = []
                for i in range(nl):
                    L.append(self.get_matrice()[i][j])
                M3.append(L)
            return M3

    def comatrice(self):
        M0 = self.get_matrice().copy()
        for i in range(0, len(self.get_matrice())):
            for j in range(0, len(self.get_matrice())):
                M0[i][j] = delta_1(self.matrice_sans_i_j(i, j))
        return M0

    def inverse(self):
        delt = self.delta()
        if delt == 0:
            print("Le détermiant est nulle,la matrice n'est pas invrsible.")
        if delt != 0:
            M0 = self.transposition_matrice()
            M1 = comatrice(M0)
            for i in range(0, len(self.get_matrice())):
                for j in range(0, len(self.get_matrice())):
                    M1[i][j] = M1[i][j] * (1 / delt)
            return M1

    def puissance(self, n):
        i = 1
        while i < n + 1:
            self.produit_matrice(self.get_matrice())


# Interface de l'utilisateur
print(r"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   _____          __          __        __             ©
  /     \ _____ _/  |________|__| ____ |__|__ __  _____  
 /  \ /  \\__  \\   __\_  __ \  |/ ___\|  |  |  \/     \ 
/    Y    \/ __ \|  |  |  | \/  \  \___|  |  |  /  Y Y  \
\____|__  (____  /__|  |__|  |__|\___  >__|____/|__|_|  /
        \/     \/                    \/               \/ """)
print(f"""\r      P E R F O R M A N C E  E T  E L E G A N C E          
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
o o o Choisir une commande en donnant sa référence o o o  
              Gestionnaire de matrices :                 
|    Créer    |  Supprimer  |   Afficher  |   Modifier  |
| une matrice | une matrice | une matrice | une matrice |
|    [0]      |     [1]     |     [2]     |     [3]     |
|    Créer    |  Supprimer  |   Afficher  |    Créer    |
|   l'unité   |    tous     |    tous     |   le zéro   |
|     [4]     |     [5]     |     [6]     |     [7]     |
               Opération sur 2 matrices :                
|    Sommer   | Soustraire | Multiplier |    Test de    |
|  2 matrice  | 2 matrice  | 2 matrice  | commutativité |
|     [8]     |     [9]    |    [10]    |     [11]      |
              Opération sur une matrices :               
|    Trace    | Transposée |   Inverse  |  Determinant  |
|    [12]     |    [13]    |    [14]    |     [15]      |
|  Comatrice  | Puissance  |  l'opposé  | x un scalaire |
|    [16]     |    [17]    |    [18]    |     [19]      |
        [20] A propos         [entrer] Quitter           """)


def refresh(p):
    print(f"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Matrices : {Matrice_base}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""", "\n", p)


refresh("")
# L'interaction avec l'utilisateur
while True:
    try:
        g = input("VOTRE COMMANDE : ")
        if g == "":
            break
        elif g == "0":
            create_matrice()
            refresh("Votre matrice a été bien créer.")
            continue
        elif g == "1":
            print("Suppression d'une matrice : ")
            del_mat = input("La matrice à supprimer : ")
            Matrice_base.remove(del_mat)
            del globals()[del_mat]
            refresh("La Matrice est supprimée.")
        elif g == "2":
            print("Affichage d'une matrice : ")
            disp_mat = input("La matrice à afficher : ")
            globals()[disp_mat].display()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif g == "3":
            print("Modification d'une matrice : ")
            modif_mat = input("La matrice à modifier : ")
            globals()[modif_mat].display()
            globals()[modif_mat].modif()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nLa matrice a été bien modifiée.")
        elif g == "8":
            print("Sommation de deux matrices : ")
            Mn = input("Entrer le nom de la première matrice : ")
            Mp = input("Entrer le nom de la deuxième matrice : ")
            M_teeeemp = globals()[Mn].somme_matrice(globals()[Mp].get_matrice())
            create_temp_object(Mn, Mp, '_plus_', M_teeeemp)
            s = Mn + "_plus_" + Mp
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "9":
            print("Soustraction de deux matrices : ")
            Mq = input("Entrer le nom de la première matrice : ")
            Mr = input("Entrer le nom de la deuxième à soustraire : ")
            M_teeeemp = globals()[Mq].somme_matrice(globals()[Mr].scalaire(-1))
            print(M_teeeemp)
            create_temp_object(Mq, Mr, '_moins_', M_teeeemp)
            s = Mq + "_moins_" + Mr
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "10":
            print("Multiplication de deux matrices : ")
            Mn = input("Entrer le nom de la première matrice : ")
            Mp = input("Entrer le nom de la deuxième à soustraire : ")
            M_teeeemp = globals()[Mn].produit_matrice(globals()[Mp].get_matrice())
            create_temp_object(Mn, Mp, '_fois_', M_teeeemp)
            s = Mn + "_fois_" + Mp
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "11":
            print("Test de commutativité : ")
            Mq = input("Entrer le nom de la première matrice : ")
            Mr = input("Entrer le nom de la deuxième à soustraire : ")
            M_teeeemp = globals()[Mq].produit_matrice(globals()[Mr].get_matrice())
            M_teeeemp_1 = globals()[Mr].produit_matrice(globals()[Mq].get_matrice())
            if M_teeeemp_1 == M_teeeemp:
                print("Les deux matrices commutent.")
            else:
                print("Les deux matrices ne commutent pas.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "8":
            print("Trace de la matrice : ")
            s = input("Entrer une matrice")
            print(f"La trace de {s} est : ", globals()[s].trace_matrice())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "13":
            print("Transposée de la matrice : ")
            s = input("Entrer une matrice : ")
            M_teeeemp = globals()[s].transposition_matrice()
            create_temp_object(s, "", '_Transposée', M_teeeemp)
            s = s + '_Transposée'
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "14":
            print("Inverse de la matrice : ")
            s = input("Entrer une matrice : ")
            M_teeeemp = globals()[s].inverse()
            create_temp_object(s, "", '_Inverse', M_teeeemp)
            s = s + '_Inverse'
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "15":
            print("Détermiant de la matrice : ")
            s = input("Entrer une matrice")
            print(f"Le détermiannt de {s} est : ", globals()[s].delta())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "20":
            print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Programme créer par Said najim et Yahia El Janati
     comme un projet d'ingénierie numérique proposé 
          par notre Professeur Nadia Dreif;
   Centre des Classes Préparatoires Salmane Al Farissi,
               MPSI-2 promotion 2022 ;)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        elif g == "16":
            print("Comatrice de la matrice : ")
            s = input("Entrer une matrice : ")
            M_teeeemp = globals()[s].comatrice()
            create_temp_object(s, "", '_Comatrice', M_teeeemp)
            s = s + '_Comatrice'
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "17":
            print("Puissance de la matrice : ")
            s = input("Entrer une matrice : ")
            n = int(input("Entrer la puissance : "))


            def display_power(s, n):
                M_teeeemp = globals()[s].puissance_matrice(n)
                create_temp_object(s, "", f'_Puisance_{n}', M_teeeemp)
                s = s + f'_Puisance_{n}'
                globals()[s].display()


            choix = input("Voulez-vous afficher toute les puissances présédentes [Y,N] : ")
            if choix in ["Y", "y"]:
                for i in range(1, n + 1):
                    display_power(s, i)
                    del globals()[s + f'_Puisance_{i}']
                    Matrice_base.remove(s + f'_Puisance_{i}')
            else:
                display_power(s, n)
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                for i in Matrice_base:
                    if Matrice_base.count(i) != 1:
                        Matrice_base.remove(i)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "19":
            print("Multiplication d'une matrice par un scalaire : ")
            s = input("Entrer une matrice : ")
            n = int(input("Entrer le scalaire : "))
            M_teeeemp = globals()[s].scalaire(n)
            create_temp_object(s, "", f'_scalaire_{n}', M_teeeemp)
            s = s + '_L_opposé'
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif g == "18":
            print("L'opposé de la matrice : ")
            s = input("Entrer une matrice : ")
            M_teeeemp = globals()[s].scalaire(-1)
            create_temp_object(s, "", '_L_opposé', M_teeeemp)
            s = s + '_L_opposé'
            globals()[s].display()
            resp = input("Voulez-vous sauvegarder cette matrice[Y,N]: ")
            del globals()[s]
            Matrice_base.remove(s)
            if resp in ['Y', 'y']:
                name = input("Nommer cette matrice : ")
                create_temp_object(name, "", '', M_teeeemp)
                refresh("La matrice a été bien ajoutée.")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        if g == '6':
            for i in Matrice_base:
                globals()[i].display()
        if g == '4':
            print("Création d'une matrice unité :")
            n = int(input("Entrer la taille de la matrice : "))
            name = f"I_{n}"
            M_teeeemp = unité_ou_zéro(n, True)
            create_temp_object(name, "", '', M_teeeemp)
            refresh("La matrice a été bien ajoutée.")
            Matrice_base.append(name)
        if g == '7':
            print("Création de la matrice nulle :")
            n = int(input("Entrer la taille de la matrice : "))
            name = f"zéro_{n}"
            M_teeeemp = unité_ou_zéro(n, False)
            create_temp_object(name, "", '', M_teeeemp)
            refresh("La matrice a été bien ajoutée.")
            Matrice_base.append(name)
        if g == '5':
            for i in Matrice_base:
                del globals()[i]
            Matrice_base.clear()
    except TypeError or ValueError or EOFError:
        print("Valeur non conforme,réessayez.")
    except KeyError:
        print("Cette matrice n'existe pas.")
        continue
