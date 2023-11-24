from function import *
if __name__ == '__main__':
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
       indice_utilisateur = int(input("Entrez un indice : "))
       afficher_president_par_indice(indice_utilisateur)

   elif num == 3:
       for i in range(len(files_names)):
           minus(files_names[i])


   elif num == 3 :
       chaine_test = "le chat est sur le toit et le chien est dans la cour"
       resultat = compter_motsTF(chaine_test)
       print(resultat)


   elif num == 4 :
       repertoire_corpus = "./cleaned"
       resultat_idf = calculer_score_idf(repertoire_corpus)
       print(resultat_idf)