# 1. Write a program to print multiplication table of a given number using for loop. while loop
num=int(input("Enter the number that you want multiplication"))
i=1
while(i<=10):
    print(f"{num} X  {i} = {num*i}")
    i+=1