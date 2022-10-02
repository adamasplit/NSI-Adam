def milieu(p1,p2):
    xm = (p1[0]+p2[0])/2
    ym = (p1[1]+p2[1])/2
    return (xm,ym)




def moyenne(tab):
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
    return (somme/len(tab))

moyenne([1,3,7,12,16])


def cherche_age():
    age = int(input("Saisir votre age : "))
    if age < 12:
        print("Vous êtes un(e) enfant")
    elif age < 17:
        print("Vous êtes un(e) ado")
    elif age < 25:
        print("Vous êtes un(e) jeune adulte")
    elif age < 45:
        print("Vous êtes un adulte")
    else : print("Vous un fossile")