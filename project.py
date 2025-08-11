a=1
phonebook={}
while(a!=0):
    n=int(input('''To add new contact type 1
To delect a contact type 2
To search for a contact type 3
To display all contacts type 4
type here:- '''))
    l=[]
    if(n==1):
        l.append(input("Enter name of contact:- "))
        l.append(int(input("Enter the contact number:- ")))
        phonebook.update({l[0]:l[1]})
    if(n==2):
        n1=input("Enter the name of contact which you want to remove:- ")
        del phonebook[n1]
    if(n==3):
        n2=input("Enter the contact name:- ")
        print(f"{n2} :- {phonebook.get(n2)}")
    if(n==4):
        print(phonebook)
