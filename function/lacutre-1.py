# def my_name(name):
#     name2="hello"+name
#     return(name2)
# print(my_name(" aditya"))
# def temperature(temp):
#     temp_in_f=(temp*9/5)+32
#     print(temp_in_f)
# temperature(int(input()))
# def check_number(num):
#     if(num<0):
#         return "Negative"
#     elif(num>0):
#         return "Postive"
#     else:
#         return "zero"
#     print("never going to print")
# n=int(input())
# print(check_number(n))
# def square(n):
#     return(n*n)
# print(square(10))
# def maximum(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
# n,m=int(input()),int(input())
# print(maximum(m,n))
# def split_fuction(s):
#     return (s.split())
# print(split_fuction("aditay verma"))
# def is_even(n):
#     if(n%2==0):
#         return True
#     return False
# print(is_even(5))
# def get_greeting():
#     c="hello,welcome to python class"
#     return c
# message=get_greeting()
# print(message) 
# def call_area(len,wid):
#     area=len*wid
#     return area
# len,wid=int(input()),int(input())
# result=call_area(len,wid)
# print("araa =",result)
def string_slicing(name,num):
    list1=[]
    new_string=""
    for i in range(len(name)):
        if(name[i]==" "):
                new_string+=name[i:]+"."
        elif(i==0):
                new_string+=name[i]
        list1.append(new_string)
        new_string=""
    for i in range(len(name)):
        if(name[i]==" "):
            new_string+=name[:i-1]
            new_string+=name[i+1]
    list1.append(new_string)
    return(list1)
name=input()
num=int(input())
print(string_slicing(name,num))

