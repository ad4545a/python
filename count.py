# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")
word,s,l= input(),"",[]
for y in word:
    if y== ' ':
        l.append(s)
        s= ''
    else:
        s+=y
if s:
    l.append(s)
e,o=[],[]
for i in l:
    if(int(i)%2==0):
        e.append(int(i)**2)
    else:
        o.append(int(i)**3)
print(e,o)
        
