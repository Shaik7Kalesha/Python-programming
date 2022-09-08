a=[]
b=int(input("Enter the number of elements:"))
p=0
c=0
for i in range(1,b+1):
    d=int(input("Emter the number:"))
    a.append(b)
    if(i%2!=0):
         p+=1
    else:
         c+=1
print("the count of prime numbers are:",p)
print("the count of composite numbers are:",c)