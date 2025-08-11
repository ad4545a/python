#ask two question from user and give output
bat=int(input("if you have bat enter 1 and not have bat press 0:- "))
ball=int(input("if you have bat enter 1 and not have bat press 0:- "))
if (bat==1 and ball==1):
    print("you can play cricket")
elif ((bat==0 and ball==0) or (bat==1 and ball==0) or (bat==0 and ball==1)):
    print("you can not play cricket")
else:
    print("enter vaild no")