# n=input()
# n,c=n+n,""
# for i in n:
#     if(i.islower()==True):
#         c=c+i
# d=""
# for i in c:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         d=d+"#"
#     else:
#         d=d+i
# print(d)
 
# n,c,v=int(input()),[],[]
# for i in range(n):
#     n1,c1,v1=input(),0,0
#     for j in n1:
#         if(j=="a" or j=="e"or j=="i" or j=="o"or j=="u" or j=="A" or j=="E"or j=="I" or j=="O"or j=="U"):
#             v1+=1
#         else:
#             c1+=1
#     v.append(v1),c.append(c1)
# for i in range(len(v)):
#     print(v[i],c[i])
from itertools import permutations
x,y,z,n=int(input()),int(input()),int(input()),int(input())
l1=[]
l1.extend(list(i for i in range(x)))
l1.extend(list(i for i in range(y)))
l1.extend(list(i for i in range(z)))
all_com=list(permutations(l1,3))
print(all_com)

        
