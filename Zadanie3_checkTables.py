tabela=[]
for i in range(10):
    tabela.append(i)
print(tabela)
#tworzenie tabeli 10 elementow- liczb 0-9
print('---------------------------------------------------------------')

tabela1=[1111,2222,6,4,3,6,5,8,19,100,101] #11 elementow

for i in range(0,11):
    print (tabela1[i])
print ('indeks 0: ' + str(tabela1[0])) #indeks zerowy tabeli
print ('indeks 1: ' + str(tabela1[1])) #indeks pierwszy tabeli

#wypisuje wszystkie elementy tablicy
#WAŻNE- INDKESOWANIE TABLIC W PYTHONIE LICZY SIE OD ZERA
print('---------------------------------------------------------------')

stringi=['a','b','c','d','e']

print (stringi)
for i in range(0,len(stringi)):
    print (stringi[i])
#wypisuje wszystkie elementy tablicy stringow
print('---------------------------------------------------------------')

liczby=[1,2,3,4,5,6,7]
znaki=['x','y','z']

print (liczby[-1])  #ostatni element tablicy
print (znaki[-1])   #ostatni element tablicy
print (liczby[0])   #pierwszy element tablicy
print (znaki[0])    #pierwszy element tablicy
print (liczby[2:])  #elementy od indeksu 2 do końca (łącznie z 2)
print (znaki[:2])   #element do indeksu 2 (bez 2)
print (liczby[3:0:-1])  #elementy od końca do początku???????????????????????


#wypisuje konkretne indeksy tablicy
print('---------------------------------------------------------------')       
