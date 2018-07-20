i=-10
while i<=0:
    print (i)
    i+=1
#drukuje liczby od -10 do 0
print('---------------------------------------------------------------')
    
i=-10
while i<0:
    print (i)
    i+=1
#drukuje liczby od -10 do 0
print('---------------------------------------------------------------')

#ograniczenie dla uzytkownika aby podal LICZBE wieksza od zera
print('Uzytkowniku - Podaj liczbe:')
wej=input() #tutaj pobierany jest parametr od uzytkownika

while float(wej)<=0:
    print('Podaj liczbe wieksza od zera')
    wej=input()
print('Good!:)')
print('---------------------------------------------------------------')
