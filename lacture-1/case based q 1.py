#we have hall with lenght l meter and breath b meaters we have to cover hall by carpit with breath=85
l=int(input("enter the length of the room:- "))
b=int(input("enter the breath oof the room:- "))
b_of_carpit=.85
area=l*b
print(area)
left_area=(2*(l*.5))+(2*(b*.5))
print(left_area)
area_carpit=area-left_area
print(area_carpit)
length_carpit=area_carpit/.85
print(length_carpit)
