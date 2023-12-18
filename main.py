from function import *
if __name__ == '__main__':
   print("Bienvenue, vous êtes sur le menu de notre programme")
   print("Si vous voulez afficher les noms des présidents sous la forme d'une Liste 1D taper 1 sur la console")
   print("Si vous voulez afficher les noms et prénoms d'un président, taper 2 sur la console, puis taper un indice entre 0 et 5 compris")
   print("Si vous voulez connaitre le nombre de fois pour lequel chaque mot est présent dans une phrase taper 4")
   print("Si vous voulez connaitre le score IDF de tous les mots les moins utilisés taper 5")
   print("Si vous voulez le score TF-IDF de tous les mots des fichiers sous forme d'une matrice, taper 6")
   print("Si vous voulez voir les mots ayant un score de 0, c'est-à-dire les plus utilisés, taper 7")
   print("Si vous voulez voir les mots ayant un score élevé, c'est-à-dire les moins utilisés, taper 8")
   print("Si vous voulez voir le mot le plus cité par Chirac, taper 9")
   print("Si vous voulez voir quel président a cité le mot nation, taper 10")
   num = int(input("Saisir numéro de la fonction : "))

   chemin_repertoire = "./speeches"
   resultats = extraire_noms_presidents(chemin_repertoire)
   """print(resultats)"""
   directory = "./speeches"
   files_names = list_of_files(directory, "txt")
   """print(files_names)"""
   if num == 1 :
       noms_famille_presidents = list(resultats.keys())
       print(noms_famille_presidents)

   elif num == 2 :
       Indice = int(input("Entrez un indice : "))
       prenom(Indice)

   elif num == 3:
       for i in range(len(files_names)):
           minus(files_names[i])
       print("Les fichiers ont été créés avec succès")


   elif num == 4 :
       chaine_test = str(input("Entrer une phrase : "))
       resultat = compter_motsTF(chaine_test)
       print(resultat)


   elif num == 5 :
       repertoire_corpus = "./cleaned"
       resultat_idf = calculer_score_idf(repertoire_corpus)
       print(resultat_idf)

   elif num == 6 :
       repertoire_documents = "./cleaned"
       matrice_tfidf = construire_matrice_tfidf(repertoire_documents)

       for row in matrice_tfidf:
           print(row)

   elif num == 7 :
       corpus_path = "./cleaned"
       tfidf_matrice = construire_matrice_tfidf(corpus_path)
       mots_non_importants = mots_non_importants(tfidf_matrice)
       print("Mots les moins importants :", mots_non_importants)

   elif num == 8 :
        chemin = "./cleaned"
        tf_idf_eleve = tf_idf_eleve(chemin)

        print("Mots importants dans les fichiers :")
        print(tf_idf_eleve)

   elif num == 9 :
       fichier1 = "./cleaned/nouveau_Chirac1.txt"
       fichier2 = "./cleaned/nouveau_Chirac2.txt"

       mot_plus_cite, nombre_citations = mot_plus_repete_chirac(fichier1, fichier2)

       print("Le mot le plus répeté par Chirac est ", mot_plus_cite, " avec ", nombre_citations, "citations.")

   elif num == 10 :
        chemin = "./cleaned"
        mot_a_rechercher = "nation"
        fichiers_avec_occurrences, fichier_max_occurrences, max_occurrences = trouver_occurrences_mot(chemin, mot_a_rechercher)
        print("Le mot ", mot_a_rechercher, " apparaît dans les fichiers suivants :" , fichiers_avec_occurrences)
        print("Le mot ", mot_a_rechercher, " apparaît le plus de fois dans le fichier ", fichier_max_occurrences, " avec",  max_occurrences, " occurrences.")
      
#Début partie II
     
   elif num == 11:
       question= input("Saisir une phrase:")
       resultat= token(question)
       print("La nouvelle phrase est", resultat)

   elif num== 12 : # a changer en fonction de l'ordre des fonctions a ajouter avant:
       a = float(input("Saisir une valeur:"))
       b = float(input("Saisir une valeur:"))
       pds = float(input("Saisir une valeur:"))
       result = cos_teta(a, b, pds)
       print("le cosinus de l'angle θ est", result)


