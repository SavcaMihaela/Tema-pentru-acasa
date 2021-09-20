##Pb.5
x=[1, 2, 3, 4, 5]
y=x
print(sum(x[0:3]))
print(sum(y))
z=1
for i in range(0,len(x)):
    z=z*x[i]
    i+=1
print(z)
print(abs(x[2]))
print(x[0]+y[0])
