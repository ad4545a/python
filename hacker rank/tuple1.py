# # # # # # # fruits=("apple","cherry","banana","kiwi","avacoda")
# # # # # #  (green,yellow,*red)=fruits
# # # # # #  print(green)
# # # # # #  print(yellow)
# # # # # #  print(type(red))

# # # # # # # looping in by index tuple
# # # # # # fruits=("apple","cherry","banana","kiwi","avacoda")
# # # # # # for i in range(len(fruits)):
# # # # # #      print(fruits[i])

# # # # # # loop via tranversing
# # # # # fruits=("apple","cherry","banana","kiwi","avacoda")
# # # # # for x in fruits:
# # # # #     print(x)

# # # # fruits=("apple","cherry","banana","kiwi","avacoda")
# # # # i=0
# # # # while i<len(fruits):
# # # #     print(fruits[i])

# # # # join two tuples
# # # new=(1,2,3,4)
# # # new2=("a","b","c")
# # # new3=new+new2
# # # print(new3)

# # n=int(input())
# # fruits=("apple","banana","cherry")
# # new3= fruits*n
# # print(new3)

# # 
# thistuple=(1,2,3,4,5,6,5,6,5,4,5,5,7)
# x=thistuple.count(5)
# print(thistuple)

thistuple=(1,3,7,8,7,5,4,6,8,5)
x=thistuple.index(3)
print(x)