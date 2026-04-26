# suppose name ="rabbani"
# r   a   b   b   a   n   i
# 0   1   2   3   4   5   6  (the length is 7)
# -7  -6  -5  -4  -3  -2  -1
name="rabbani"
print(name,type(name))
# name[0]="a"  # we cannot do this bcz the string is immutable we cannot assign the values to it 
# print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# string_slicing 
print(name[0:5])  #includes 0 and excludes 5
print(name[1:4])
print(name[-4:-3])
print(name[3:4])
print(name[:])  #means includes 0 to length of string (-1)
my_str=input("Enter your name:\n")
print(my_str,type(my_str))