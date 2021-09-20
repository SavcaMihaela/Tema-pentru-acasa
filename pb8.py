t=[1, 2, 3, 4, 5, 6, 7, 8, -7,-6, -5, -4, -3, -2, -1]
print(sum(t)/24)
for i in t:
    if i==max(t):
        print('temperatura maxima la ora', t.index(i)+1)
for i in t:
    if i==min(t):
        print('temperatura medie la ora', t.index(i)+1)
z1=0
for i in t:
    if i<0:
        z1+1
        print(' nunmarul de zile in care nu a fost inregistrata temperatura sub 0=', z1)
z2=0
for i in t:
    if i>sum(t)/24:
        z2+=1
        print('numarul de zile in care au fost inregistrate temperaturi mai mari de media saptamanii =', z2)