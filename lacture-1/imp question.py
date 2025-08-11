# keyword={
#     2 : ["a","b","c"], 3 : ["d","e","f"], 4: ["g","h","i"], 5: ["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]
# }
# num=(input())
# out=[]
# for i in num:
#     for
# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")

# for i in range(5):
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")
# srting="aditya verma"
# C=list("".join(srting.split()))
# print(C)




# from itertools import permutations
# n=input()
# l=list("".join(n.split()))
# c,a=list(permutations(l,len(n))),0
# for i in c:
#     if(tuple(l)==i):
#         break
#     else:
#         a=a+1
# if(a==len(c)):
#     print("0")
# else:
#     print("1")

n,l=list(map(int,input().split())),[]
n.sort()
for i in range(len(n)):
    if(i!=len(n)-1):
        l.append(n[i]*n[i+1])
print(l[-1])
