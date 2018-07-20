for i in range (0,3):
    print (i)
#drukuje 0 1 2
print('---------------------------------------------------------------')

for i in range (0,3):
    j=i+1
    print ('i= ' + str(i))
    print ('j= ' + str(j))
#dla i drukuje 0 1 2
#dla j drukuje 1 2 3
print('---------------------------------------------------------------')

for i in range (0,3):
    i=i+1
    print ('i= ' + str(i))
#dla i wydrukuje 1 2 3
print('---------------------------------------------------------------')


print('Parzyste')
for i in range (1,100):
    if i%2==0:
        print(i)
# liczby parzyste z przedziału od  1 do 99 łącznie 
print('---------------------------------------------------------------')


print('Nieparzyste')
for i in range (1,100):
    if i%2!=0:
        print(i)
    # liczby nieparzyste z przedziału od  1 do 99 łącznie 
print('---------------------------------------------------------------')

List=[]
for i in range (0,101):
    if i%2!=0:
        List.append(i)
print(List)
print('w przedziale 0-100 jest: ' + str(len(List)) + ' liczb nieparzystych')
#Ile jest liczb nieparzytych w zbiorze liczb 0-99
print('---------------------------------------------------------------')

List_niep=[]
for i in range(0,101):
    if  i%2==0:
        List_niep.append(i)
print(List_niep)
print('W przedziale 0-100 jest: '+ str(len(List_niep)) + ' liczb parzystych')
#Ile jest liczb parzytych w zbiorze liczb 0-100 łącznie + wyswietlenie liczb
