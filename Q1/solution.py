## Add code below with answer clearly stated
n=100
fact=1
sum=0

#code for finding the factorial;
for i in range(1,n+1):
    fact=fact*i


#converting the factorial into list of int in order to find sum
list_2 = list(map(int, str(fact)))


#adding no from list 
for j in list_2:
    sum=sum+j
    
print("Sum of digits in the number ",n," factorial is:",sum)
