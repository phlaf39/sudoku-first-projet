from Grille import afficherGrille
from Carre import sudokuGrilleFacile
from Carre import sudokuGrillefini

def partieFacile():
    inputLigne = 0
    inputColone = 0
    inputNumero = 0
    print('Voici la grille de la partie facile ! commencons...')
    etatDePartie = True
    while etatDePartie is True:

        grilleDeJeux = sudokuGrilleFacile
        #------ Game de pratique-------
        #grilleDeJeux = sudokuGrillefini
        afficherGrille(grilleDeJeux)
        # Input nécessaire pour le placement d'un numero
        inputValid = False
        while inputValid is False:
            while True:
                try:
                    inputLigne = int(input('entrez le numero de la ligne'))
                except ValueError:
                    print('Votre réponse doit être un chiffre :)')
                else:
                    break
            if inputLigne >= 0 and inputLigne <=9:
                inputValid = True

        inputValid = False
        while inputValid is False:
            while True:
                 try:
                    inputColone = int(input('entrez le numero de la colone'))
                 except ValueError:
                     print('Votre réponse doit être un chiffre :)')
                 else:
                     break
            if inputColone >= 0 and inputColone <= 9:
                inputValid = True

        inputValid = False
        while inputValid is False:
            while True:
                 try:
                     inputNumero = int(input('entrez le numero'))
                 except ValueError:
                     print('Votre réponse doit être un chiffre :)')
                 else:
                     break
            if inputNumero >= 0 and inputNumero <= 9:
                inputValid = True

        empNewNumber = (int(inputLigne)-1)*9+ int(inputColone)-1

        grilleDeJeux[empNewNumber] = int(inputNumero)
        nombreDe0 = 0
        for i in grilleDeJeux:
            if grilleDeJeux[i] ==0:
                nombreDe0 = nombreDe0 +1
            if i == grilleDeJeux[-1] and nombreDe0 == 0:
                etatDePartie = False
        if etatDePartie == False:
            afficherGrille(grilleDeJeux)
            print('Wow ! bravo vous avez réussi!!')



