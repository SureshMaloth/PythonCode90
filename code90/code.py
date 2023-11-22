#Write a  programme to reverse an integer in a python
#1
num=123456
con_int_str=str(num)
reverse_num=int(con_int_str[::-1])
print(reverse_num)
print(type(reverse_num))
#2


n = int(input("Please give a number: "))
print("Before reverse your number is : %d" %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print("After reverse : %d" %reverse)

print(123456//10)

#2 Write a programme in a python check whether an integer is armstrong num or not
num=153
str_num=str(num) 
length=len(str_num)
number=0
for i in str_num:
    number+=int(i)**length
if num==number:
    print("Is A ArmStrong Nmbr: ",number)
else:
    print("Is Not a Armstrong Num: ",number)

#2
num=int(input("enter the num:"))
total=0
temp=num
lenth_of_num=len(str(num))
while temp>0:
    digit=num%10
    total+=digit**lenth_of_num
    temp//=10
if total==temp:
    print("Is ArmStrong: ",num)
else:
    print("is not a ArmStrong Nbr:",num)


#3 Write a program to check given num prime or not

num=int(input("enter the num:"))
factor=0
for i in range(2,num):
    if num%i==0:
        factor+=1
    
if factor==0:
    print("It Is a Prime Num: ",num)
else:
    print("It Is Not a prime Nbr: ",num)


#4 Write a programme to print the Fibbonacci Series using iterative method

nbr=int(input("enter the nbr: "))
first,second=0,1
result=0
for i in range(0,nbr):
    if i<=1:
        result=i
    else:
        result=first+second
        first=second
        second=result
    
    print(result)
    
#5Write a programme to print the Fibbonacci Series using recursive method

def fibonacci(nbr):
    if nbr==0:
        return 0
    elif nbr==1:
        return 1
    else:
        return fibonacci(nbr-1)+fibonacci(nbr-2)
    
n=int(input("enter the nbr:"))
for i in range(0,n):
    print(fibonacci(i))
        

#6 Write a Programme in a python check wether a number is polindrome r not using iterative method

num=int(input("enter the nbr: "))
convert_int_to_str=int(str(num)[::-1])
if num==convert_int_to_str:
    print("It Is A polindrome")
else:
    print("It is Not a Polindrome")

reverse=0
while num != 0:
    reverse=reverse*10+num%10
    num=num//10
    
print(reverse)


    
#7 Write a Programme in a python check wether a number is polindrome r not using recursive method

n = int(input("please give a number : "))
def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))
def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome") 

#8Write a Programme in a python to find the gretest amoung three integers

num =int(input("enter the number: "))
print(num)
str_int=str(num)
first_num=str_int[0]
gretest_num=int(first_num)
for i in str_int:
    i=int(i)
    if i>gretest_num:
        gretest_num=i
print(gretest_num)

    
num_1=10
num_2=20
num_3=13
if num_1>=num_2 and num_1>=num_3:
    gretest=num_1
elif num_2>=num_1 and num_2>=num_3:
    gretest=num_2
else:
    gretest=num_3
print(gretest)

#9 write a program in a python to check if a number is binary or not

num=int(input("enter the num:"))
while num>0:
    n=num%10
    if n!=0 and n!=1:
        print("num is not a Binary")
        break
    num=num//10
    if num==0:
        print("Num is a binary")
#10 write a program in python to find the sum of digits of a number using recursion?
def sum(n):
    if n==0:
        return 0
    return n%10 + sum(n//10)
num=12345
res=sum(num)
print(res)


#11 write a program in a python to swap two numbers without using third variable
a=10
b=8
a=a-b
b=a+b
a=b-a
print(a)
print(b)

#12 write a program in a python to swap two numbers with using third variable
a=10
b=8
c=a
a=b
b=c
print(a)
print(b)

