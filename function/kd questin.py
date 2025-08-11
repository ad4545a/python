# #take a number from a user as a input and find its fact if the fact of the number is prime then find the sum of the digits os that fact and check the sum is even or odd
# #do this question using function
# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return(fact)

# def prime(fact):
#     count=0
#     for i in range(1,fact+1):
#         if(fact%i==0):
#             count+=1
#     if(count==2):
#         return(fact)
#     else:
#         return "not prime"
        
# def sum_of_digits(fact):
#     fact=str(fact)
#     sum=0
#     for i in fact:
#         sum+=int(i)   
#     return sum

# def even_odd(sum):
#     if(sum%2==0):
#         return "even"
#     else:
#         return "odd"
# num=int(input())
# ans=fact(num)
# ans=sum_of_digits(ans)
# ans=prime(ans)
# if(str(ans).isnumeric()==True):
#     ans=even_odd(ans)
#     print(ans)
# else:
#     print(f"fact of num is not prime")

# n=int(input())
# l=[0,1]
# for i in range(n-2):
#     sum=l[i]+l[i+1]
#     l.append(sum)
# print(l)
# sum=0
# for i in l:
#     if(i%2==0):
#         sum+=i
# print(sum)
# num=input()
# count=0
# sum1=0
# for i in range(1,int(num)):
#     if(int(num)%i==0):
#         count+=1
# if(count==1):
#     for i in num:
#         sum1+=int(i)
# print(sum1)
