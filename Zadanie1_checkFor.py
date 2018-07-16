for i in range (0,3):
    print (i)
#drukuje 0 1 2

for i in range (0,3):
    j=i+1
    print ('i= ' + str(i))
    print ('j= ' + str(j))
#dla i drukuje 0 1 2
#dla j drukuje 1 2 3

for i in range (0,3):
    i=i+1
    print ('i= ' + str(i))
#dla i wydrukuje 1 2 3


print('Parzyste')
for i in range (1,100):
    if i%2==0:
        print(i)


print('Nieparzyste')
for i in range (1,100):
    if i%2!=0:
        print(i)


#Ile jest liczb nieparzytych w zbiorze liczb 0-100
List=[]
for i in range (0,100):
    if i%2!=0:
        List.append(i)
print('w przedziale 0-100 jest ' + str(len(List)) + ' liczb nieparzystych')


