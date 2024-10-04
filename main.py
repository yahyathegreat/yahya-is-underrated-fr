n = int(input("enter the number whose sum you want to finf: "))
sum=0
for i in range(1, n+1):
    sum = sum+i
    print("\nsum =", sum)
string = input("please enter your own string : ")
string2 = ('')
for i in string:
    string2 = i + string2
print("\nthe original string =", string)
print("the reversed string = ", string2)