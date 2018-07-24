#Wyzwanie1 to wypisanie zdania uzytkownika od "tylu"

print ('Wpisz zdanie\n')
sen=input()
print ('\nTwoje zdanie to: \n' + sen)

sen_list=list(sen)
tablica=[]
for i in range (0,len(sen_list)):
    tablica.append(sen_list[i])
#Poniżej dzieje się WAŻNA rzecz!
#odwracamy zawartość indeksów - co jest oczywiste :)
#ale wciąż to tablica,aby zamienić ją na string używamy .join

#zalozmy,ze uzytkownik podaje zdanie : 'Gosia ma Tifcie'
print("".join(tablica [::-1])) # tuta 'eicfiT am aisoG'


print(tablica [::-1]) #tutaj '['e', 'i', 'c', 'f', 'i', 'T', ' ', 'a', 'm', ' ', 'a', 'i', 's', 'o', 'G']'
#poniżej przetestujmy wartości co sie wstanie jak powstawiamy rozne znaki w (...).join

print(" ".join(tablica [::-1])) #tutaj 'e i c f i T   a m   a i s o G'
print("X".join(tablica [::-1])) #tutaj 'eXiXcXfXiXTX XaXmX XaXiXsXoXG'
