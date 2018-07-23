#Wyzwanie1 to wypisanie zdania uzytkownika od "tylu"

print ('Wpisz zdanie\n')
sen=input()
print ('\nTwoje zdanie to: \n' + sen)

sen_list=list(sen)
tablica=[]
for i in range (0,len(sen_list)):
    tablica.append(sen_list[i])
print(tablica [::-1])
