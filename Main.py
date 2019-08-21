from Facile import partieFacile

def main():
    print('Bienvenue au tout premier jeux de sudoku en amérique du nord')
    difficulte = input('choisissez votre niveau de difficulté(1 -facile 2- moyen -3 difficile) :')
    if difficulte == '1':
        partieFacile()

if __name__ == '__main__':
    main()
