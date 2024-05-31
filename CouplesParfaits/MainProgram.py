import random

Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

numero=random.randint(0,25)

print(numero)
if numero <10 : 
    nom_fichier="./fichier00"+str(numero)+".txt"
elif numero <100 : 
    nom_fichier="./fichier0"+str(numero)+".txt"
else :
    nom_fichier="./fichier"+str(numero)+".txt"
texte = open(nom_fichier, 'r') 
texte=texte.read()
print('test')
texte = str(texte)

## on fait une copie du texte original qu'on convertit en _ pour faire le texte caché

texte_cache= list(texte)
##print(texte_cache)
for i in range(len(texte_cache)) : 
    if texte[i] in Alphabet and not (texte[i-1] not in Alphabet and texte[i+1] not in Alphabet) : 
        texte_cache[i] = "_"

def changement_affichage(texte_cache) : 
    texte_affiche = ''
    for i in texte_cache : 
        texte_affiche += str(i)
    print(texte_affiche)

changement_affichage(texte_cache)
nb_essai=0
essais=[]
while "_" in texte_cache : 
    print("essayez 2 lettres")
    essai= input()
    if len(essai) ==2 and essai[1] in Alphabet and essai[0] in Alphabet and essai not in essais : 
        nb_essai +=1
        essais+=[essai]
        trouve=0
        if essai in texte : 
            N= texte.count(essai) 
            for i in range(len(texte)) : 
                if texte[i]==essai[0] and not(i==len(texte)-1) and texte[i+1]==essai[1]  : 
                    texte_cache[i] = essai[0]     
                    texte_cache[i+1] =essai[1]   
                    trouve+=1
        if essai[0]+" "+essai[1] in texte :
            if texte[i]==essai[0] and not(i==len(texte)-2) and texte[i+1]==" " and texte[i+2]==essai[1]  : 
                    texte_cache[i] = essai[0]     
                    texte_cache[i+2] =essai[1]   
                    trouve+=1
        if trouve>0 : 
            print(str(trouve)+" trouvés")
            changement_affichage(texte_cache)
        else : 
            print("dommage")
    elif essai in essais : 
        print(essai + " a déjà été essayé")   
    else : 
        print('réessayer')

print("BRAVO")
print("nombre d'essai"+str(nb_essai))

if numero<=9 : 
    print("Source : OLIVER TWIST, CHARLES DICKENS") 
elif numero<=16 : 
    print("Source : CANDIDE, VOLTAIRE")
elif numero in [17,22,24,25,26,27] : 
    print("Source : DU CÔTE DE CHEZ SWANN, MARCEL PROUST")
elif numero==18 : 
    print("Source : UNE FANTAISIE DU DOCTEUR OX, JULES VERNES")
elif numero==19 : 
    print("Source : VINGT MILLE LIEUES SOUS LES MERS, JULES VERNES")
elif numero == 20 : 
    print("Source : LE LAC, LAMARTINE")
elif numero == 21 : 
    print("Source : Lorem Ipsum")
elif numero == 23 : 
    print("Source : LE VAGABOND, VICTOR HUGO")
elif numero in [28,30] :
    print("Source : LE CID, CORNEILLE")
elif numero == 29 : 
    print("Texte original de Callixte de Reydet de Vulpillières")
elif numero == 31 : 
    print ("Source : LES TROIS MOUSQUETAIRES, ALEXANDRE DUMAS")