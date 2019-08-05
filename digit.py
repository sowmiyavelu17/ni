n=input("Enter Number to calculate sum")
 n=int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )
10.           def Counting(number):
Count = 0
while(number > 0):
number = number // 10 
Count = Count + 1
print("\n number of digit number = %d" %Count)
Counting(1234)
