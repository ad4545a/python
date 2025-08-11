n,coun,j=int(input("")),0,1
while(j<n):
   for i in range(1,j):
        if(n%i==0):
            coun+=1
        if(coun==1):
            print(j)
        