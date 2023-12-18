import re
import os
import math

#Création d'une fonction qui va extraire le nom des présidents du dossier cleaned


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
       if filename.endswith(extension):
           files_names.append(filename)
    return files_names
def extraire_noms_presidents_cln(repertoire):
   noms_presidents = {}
   modele_regex = r'nouveau_(\w+)(\d*)\.txt'


   for fichier in os.listdir(repertoire):
       chemin_fichier = os.path.join(repertoire, fichier)


       if os.path.isfile(chemin_fichier) and fichier.endswith(".txt"):
           match = re.search(modele_regex, fichier)

           if match:
               nom_complet = match.group(1)
               noms = nom_complet.split(
                   " ")
               nom_famille = noms[-1]


               if nom_famille not in noms_presidents:
                   noms_presidents[nom_famille] = noms[:-1]

   return noms_presidents

chemin_repertoire = "./cleaned"
resultats = extraire_noms_presidents_cln(chemin_repertoire)

noms_famille_presidents = list(resultats.keys())
print(noms_famille_presidents)



"""suite"""
#Création d'une fonction nous permettant d'avoir les noms des présidents sous la forme d'une liste 1D.
# #La fonction def extraire_noms_presidents sert a afficher les noms des présidents.
def extraire_noms_presidents(repertoire):
   noms_presidents = {}
   modele_regex = r'Nomination_(.*?)\d*\.txt'


   for fichier in os.listdir(repertoire):
       chemin_fichier = os.path.join(repertoire, fichier)


       if os.path.isfile(chemin_fichier) and fichier.endswith(".txt"):
           match = re.search(modele_regex, fichier)

           if match:
               nom_complet = match.group(1)
               noms = nom_complet.split(
                   " ")
               nom_famille = noms[-1]


               if nom_famille not in noms_presidents:
                   noms_presidents[nom_famille] = noms[:-1]

   return noms_presidents

chemin_repertoire = "./speeches"
resultats = extraire_noms_presidents(chemin_repertoire)

noms_famille_presidents = list(resultats.keys())
print(noms_famille_presidents)


#Création d'une fonction affichant le nom et le prénom d'un président en fonction de l'indice saisie par l'utilisateur
def prenom(indice):
    lst_nom = ['Chirac', 'dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']

    if 0 <= indice < len(lst_nom):
        nom = lst_nom[indice]
        prenom = ""

        if nom == "Chirac":
            prenom = 'Jacques'
        elif nom == "dEstaing":
            prenom = 'Valéry Giscard'
        elif nom == "Hollande":
            prenom = 'François'
        elif nom == "Macron":
            prenom = 'Emmanuel'
        elif nom == "Mitterrand":
            prenom = 'François'
        elif nom == "Sarkozy":
            prenom = 'Nicolas'

        print("Nom :", nom, "prénom : ", prenom)
    else:
        print("Indice invalide")


#Nous avons créer une fonction permettant de transformer le contenu des fichiers en minuscules, et à la fois de supprimer les caractères de ponctuations.
# a l'exécution cette fonction en rentrant le chiffre 3 qui lui est associé, il n'y a aucun d'affichage, il faut donc aller voir les fichiers qui ont bien subis toute les modifications.
def minus(nom_fichier):
   nouveau_nom = "nouveau_"+ nom_fichier[11:-4]
   with open("./speeches/" + nom_fichier, "r", encoding="UTF-8") as f1, open("./cleaned/" + nouveau_nom + ".txt", "w", encoding="UTF-8") as f2:
       for ligne in f1:
           minuscule = ligne.lower()
           modification =""
           for i in minuscule:
               ascii = ord(i)
               if (ascii < 33 or ascii > 47) and (ascii < 58 or ascii > 64) and (ascii < 91 or ascii > 96) :
                   modification += i
               if ascii == 45 or ascii == 39:
                   modification += " "
           f2.write(modification)

#Fonction permettant de compter la fréquence d'un mot dns le fichier
def compter_motsTF(chaine):

   mots = chaine.split()
   compte_mots = {}

   for mot in mots:
       if mot in compte_mots:
           compte_mots[mot] += 1
       else:
           compte_mots[mot] = 1
   return compte_mots

#Fonction donnant le score IDF d'un mot, plus le mot est dans le texte moins son score sera élevé.

def calculer_score_idf(repertoire_corpus):
    nb_documents_contenant_mot = {}
    nb_total_documents = 0
    
    for nom_fichier in os.listdir(repertoire_corpus):
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        if os.path.isfile(chemin_fichier):
            nb_total_documents += 1

            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                mots = fichier.read().split()

                mots_uniques = set(mots)

                for mot in mots_uniques:
                    nb_documents_contenant_mot[mot] = nb_documents_contenant_mot.get(mot, 0) + 1

    score_idf = {mot: math.log((nb_total_documents + 1) / (nb_documents_contenant_mot[mot] + 1)) for mot in nb_documents_contenant_mot}

    return score_idf


def construire_matrice_tfidf(repertoire_corpus):
    score_idf = calculer_score_idf(repertoire_corpus)

    mots_uniques = list(score_idf.keys())

    tfidf_matrice = []

    for nom_fichier in os.listdir(repertoire_corpus):
        tfidf_matrice.append(mots_uniques)
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier :
                contenu = fichier.read()

                scores_tf = compter_motsTF(contenu)

                row = [nom_fichier.split('.')[0]] + [scores_tf.get(mot, 0) * score_idf.get(mot, 0) for mot in mots_uniques]
                tfidf_matrice.append(row)

    tfidf_matrice_transposee = [[tfidf_matrice[j][i] for j in range(len(tfidf_matrice))] for i in range(len(tfidf_matrice[0]))]

    return tfidf_matrice_transposee


"""def mots_moins_importants(repertoire):
    tfidf_matrice_transposee = construire_matrice_tfidf(repertoire)

    mots_uniques = tfidf_matrice_transposee[0][1:]

    mots_non_importants = []

    for mot in mots_uniques:
        colonne = [row[mots_uniques.index(mot) + 1] for row in tfidf_matrice_transposee[1:]]

        # Vérifier si le score TF-IDF est 0 dans tous les fichiers
        if all(0.0 < score < 0.1 for score in colonne):
            mots_non_importants.append(mot)

    return mots_non_importants"""


def mots_non_importants(matrice_tfidf):
    mots_non_importants = []
    tfidf_scores=0

    for ligne in matrice_tfidf:
        for i in range(1, len(ligne)):
           tfidf_scores += float(ligne[i][1:])
        if (tfidf_scores / (len(ligne)-1) ) == 0:
            mots_non_importants.append(ligne[0])
        tfidf_scores = 0
    return mots_non_importants


def tf_idf_eleve(repertoire_fic):
    tfidf_matrice_transposee2 = construire_matrice_tfidf(repertoire_fic)

    mots_imp = tfidf_matrice_transposee2[0][1:]

    mots_importants = []

    for mot in mots_imp:
        colonnes = [float(row[mots_imp.index(mot) + 1]) for row in tfidf_matrice_transposee2[1:]]

        if all(score > 2.0 for score in colonnes):
            mots_importants.append(mot)

    return mots_importants


def mot_plus_repete_chirac(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as f1, open(fichier2, 'r', encoding='utf-8') as f2:
        contenu1 = f1.read()
        contenu2 = f2.read()

    mots_freq_fichier1 = compter_motsTF(contenu1)
    mots_freq_fichier2 = compter_motsTF(contenu2)

    # Fusionner les fréquences des deux fichiers
    mots_freq_combines = {mot: mots_freq_fichier1.get(mot, 0) + mots_freq_fichier2.get(mot, 0) for mot in set(mots_freq_fichier1) | set(mots_freq_fichier2)}

    mot_plus_cite = max(mots_freq_combines, key=mots_freq_combines.get)
    nombre_citations = mots_freq_combines[mot_plus_cite]

    return mot_plus_cite, nombre_citations

def trouver_occurrences_mot(repertoire, mot):
    occurrences_par_fichier = {}
    fichier_max_occurrences = None
    max_occurrences = 0

    fichiers_avec_occurrences = []

    for nom_fichier in os.listdir(repertoire):
        chemin_fichier = os.path.join(repertoire, nom_fichier)

        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

                occurrences_mot = compter_motsTF(contenu).get(mot, 0)

                if occurrences_mot > 0:
                    nom_sans_chiffre = extraire_noms_presidents_cln(nom_fichier)
                    fichiers_avec_occurrences.append(nom_sans_chiffre)

                occurrences_par_fichier[nom_fichier] = occurrences_mot

                if occurrences_mot > max_occurrences:
                    max_occurrences = occurrences_mot
                    fichier_max_occurrences = nom_fichier

    return fichiers_avec_occurrences, fichier_max_occurrences, max_occurrences


def token (question):
    Ponctuation=["&","#","'",",",".",";","!","?","^","_","-","`","@","*","§",["'"]]
    mot=""
    for elt in question:
        if 65 <= ord(elt) <= 90:
            mot+= chr(ord(elt)+32)
        elif elt in Ponctuation or elt in ['"']:
            mot+=" "
        else:
            mot+=elt
    Lst= list(mot.split())
    return Lst

def tf_idf_question(corpus, question):
    mots_corpus = set()
    for document in corpus:
        mots_corpus.update(document.lower().split())
    termes_question = token(question)

    termes_present = [terme for terme in termes_question if terme in mots_corpus]

    return termes_present

def norme(vecteur):
    somme = 0
    for i in range(len(vecteur)):
        somme+=vecteur[i]**2
    module_vecteur=math.sqrt(somme)
    return module_vecteur

def produit_scalaire_vecteur(vecteur1,vecteur2):
    ps=0
    for i in range(len(vecteur1)):
        ps=ps+vecteur1[i]*vecteur2[i]
    return ps
def cos_teta(a,b,ps):
    norme1 = abs(a)
    norme2 = abs(b)
    res = ps/ (norme1 * norme2)
    return res
def calcul_similarite(vecteur1,vecteur2):
    return produit_scalaire_vecteur(vecteur1,vecteur2)/(norme(vecteur1)*norme(vecteur2))

def calcul_document_plus_pertinent(matrice,vecteur,liste):
    similarite_max=0
    indice=0
    for i in range(1,len(matrice)):
        similarite=calcul_similarite(vecteur[1],matrice[i])
        if similarite>similarite_max:
            similarite_max=similarite
            indice=i
    indice=indice-1
    return liste[indice]

def generateur_reponse(vecteur):
    max_tf_idf=0
    mot=""
    for i in range(0,len(vecteur[0])):
        if max_tf_idf<vecteur[1][i]:
            max_tf_idf=vecteur[1][i]
            mot=vecteur[0][i]
    return mot

def trouver_phrase(document, mot):

    with open(f"cleaned/{document}", 'r', encoding="UTF-8") as file:
        contenu_cleaned = file.read()

    mots_contenu = contenu_cleaned.split()

    try:
        indice_mot = mots_contenu.index(mot)
    except ValueError:
        return ""

    with open(f"speeches/{document}", 'r', encoding='UTF-8') as file2:
        contenu_original = file2.read()

        indice_fin = contenu_original.find(".", indice_mot)

        indice_debut = contenu_original.rfind(".", 0, indice_mot)

        phrase_finale = contenu_original[indice_debut + 1:indice_fin + 1]

    return phrase_finale.strip()

def affiner_reponse(phrase,nom_document,liste,liste2,mot_question):

    indice=0
    for i in range(len(liste)):
        if nom_document==liste[i]:
            indice=i
            break
    if indice==1 or indice==2:
        president=liste2[0]
    elif indice==3:
        president=liste2[1]
    elif indice==4:
        president=liste2[2]
    elif indice==5:
        president=liste2[3]
    elif indice==6 or indice==7:
        president=liste2[4]
    else:
        president=liste2[5]

    mot_question_dico = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! ",
        "Quand":president+"Lors de son discour: " ,
        "Qui": president+"lors de son discour: "
    }

    if mot_question[0] in mot_question_dico:
        reponse=mot_question_dico[mot_question[0]]+phrase+"."
    else:
        reponse=phrase+"."
    return reponse
