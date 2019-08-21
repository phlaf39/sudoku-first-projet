
#element81 = [0] * 81

#est-ce que grille devrait prendre la liste en argument?
def afficherGrille(element81):

    for i in range(9):

        if i < 8:
            if (i+1)%3 != 0:
                for j in range(9):
                    if (j+1)%3  == 0:
                        print (' ', element81[j + 9*i],'|| ', end='')
                    else:
                        print(' ', element81[j + 9 * i], '| ', end='')
                print("\n",'---|-----|-----||-----|-----|-----||-----|-----|-----')

            elif (i + 1) % 3 == 0:
                for j in range(9):
                    if (j+1)%3  == 0:
                        print (' ', element81[j + 9*i],'|| ', end='')
                    else:
                        print(' ', element81[j + 9 * i], '| ', end='')
                print("\n", '===|====|======||=====|=====|=====||=====|=====|=====')
        else :
            for j in range(9):
                print (' ', element81[j + 9*i],'| ', end='')
    print(' ')

