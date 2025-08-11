#13
'''sum=0
for i in range(2,20):
    if(i%2!=0):
        sum+=i
        print(sum,end=" ")'''
#14
'''for i in range(1,21):
    if(i%2==0):
        if(i%4==0):
            print(-i,end=" ")
        else:
            print(i,end=" ")'''
#15
'''n=int(input(""))
sum=1
for i in range(0,n):
    if(i==1):
        print(1,end=" ")
    if(i%2!=0):
        sum+=i
        print(sum,end=" ")'''
#16
'''n=int(input(""))
for i in range(1,11):
    new=i*n
    print(new)'''
#17
'''sum=1
n=int(input(""))
for i in range(1,n+1):
    sum=sum*i
print(sum)'''
#18
n1=int(input(""))
n=0
n2=1
new=n2
c=1
print (n,end=' ')
print(n2,end=' ')
while c<=n1:
    print(new,end=' ')
    c+=1
    n,n2=n2,new
    new=n+n2
print()



    