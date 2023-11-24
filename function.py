import re
import os
import math
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
       if filename.endswith(extension):
           files_names.append(filename)
    return files_names
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


def prenom_president(prenom):
   lst_nom = ['Chirac', 'dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']
   prenom = ""
   if lst_nom[0] == "Chirac":
       prenom = 'Jacques'
   elif lst_nom[1] == "dEstaing":
       prenom = 'Valéry Giscard'
   elif lst_nom[2] == "Hollande":
       prenom = 'François'
   elif lst_nom[3] == "Macron":
       prenom = 'Emmanuel'
   elif lst_nom[4] == "Mitterrand":
       prenom = 'François'
   elif lst_nom[5] == "Sarkozy":
       prenom = 'Nicolas'


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
def compter_motsTF(chaine):


   mots = chaine.split()
   compte_mots = {}


   for mot in mots:
       if mot in compte_mots:
           compte_mots[mot] += 1
       else:
           compte_mots[mot] = 1
   return compte_mots


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


   score_idf = {mot: math.log(nb_total_documents / (1 + nb_documents_contenant_mot[mot])) for mot in nb_documents_contenant_mot}

   return score_idf


#def fon():
  #  ...