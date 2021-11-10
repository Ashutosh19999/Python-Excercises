"""
Pattern Printing
Input=Integer n
Boolean=True or False

True
*
**
***
****

False
****
***
**
*
"""
print("Printing Pattern")
print("Enter the length of the right angled triangle")
n=int(input())
print("Do you want to print the  pattern in a normal way or upside down?:True or False")
b=eval(input())#type cast a input string to boolean
y=1

if b==True:
   while(y<=n):
    print(y*"*")
    y=y+1
    continue

if b==False:
   while (n > 0):
     print(n * "*")
     n = n - 1
     continue





