li=[1,2,"Rabbani",True]
print(li,type(li))
print(f"The length of the string {li} is:",len(li))
li[0]="harry"  # lists are mutable we can assign new values to the lists
print(li,type(li))
# li=[]
# print(li)
print(li[1:3]) # list slicing
print(li[:3])
print(li[-1:-4:-1])
