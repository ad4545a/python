n=int(input(""))
word=input("")
new=word.split( )
for i in range(n):
   new2= tuple(new[i])

print(hash(new2))