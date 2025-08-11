# word,s,l= input(),"",[]
word=input()
s=""
l=[]
for y in word:
    if y== ' ':
        l.append(s)
        s= ''
    else:
        s+=y
if s:
    l=[s]
print(l)
# new_str=""
# for n in l:
#     c,new=0,""
#     for x in range(len(n)):
#         if(n[x]=="a" or n[x]=="e"or n[x]=="i" or n[x]=="o"or n[x]=="u" or n[x]=="A" or n[x]=="E"or n[x]=="I" or n[x]=="O"or n[x]=="U"):
#             l=n[x:len(n)]
#             c+=1
#             break
#         else:
#             new+=n[x]
#     if(c==1):
#         new_str+=l+new+"ay"+" "
#     else:
#         new_str+=n+" "
# print(new_str)

