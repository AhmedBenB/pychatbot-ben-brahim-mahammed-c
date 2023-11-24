import re
import os
import math
#Création d'une fonction nous permettant d'avoir les noms des présidents sous la forme d'une liste 1D.
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
       if filename.endswith(extension):
           files_names.append(filename)
    return files_names

#La fonction def extraire_noms_presidents sert a afficher les noms des présidents.
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
def afficher_president_par_indice(indice):
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

        print(f"Nom : {nom}, prénom : {prenom}")
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


   score_idf = {mot: math.log(nb_total_documents / (nb_documents_contenant_mot[mot])) for mot in nb_documents_contenant_mot}

   return score_idf



def construire_matrice_tfidf(repertoire_corpus):
    score_idf = calculer_score_idf(repertoire_corpus)

    mots_uniques = list(score_idf.keys())

    tfidf_matrix = []

    for nom_fichier in os.listdir(repertoire_corpus):
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

                scores_tf = compter_motsTF(contenu)

                row = [scores_tf.get(mot, 0) * score_idf.get(mot, 0) for mot in mots_uniques]
                tfidf_matrix.append(row)

    return tfidf_matrix