# age= int(input("enter the age:"))
# if age <18:
#     print ("A cinema charge:150")
# if age >18 and age<=60:
#     print ("A cinema charge:250")  
# if age>60:
#     print ("A cinema charge:100")   



# age= int(input("enter the age:"))
# if age <12:
#     print ("A ticket is :50")
# if age>=12 and age<=59:
#     print ("A ticket is :120")  
# if age>=60:
#     print ("A ticket is:80") 



# num= int (input("enter the num:"))
# if num>0:
#     remainder=num//5
#     basket=num%5
#     print("Full basket",remainder)
#     print("Left over mangoes:",basket)


# n = int(input("Enter number of candies: "))
# for day in range(1, n + 1):
#     left = n - day
#     print(f"Day {day} = {left} left")
  
    
# salary = float(input("Enter your salary: "))
# sales = int(input("Enter your sales: "))

# if sales >= 100:
#     bonus = 0.10 * salary
# elif sales >= 50:
#     bonus = 0.05 * salary
# else:
#     bonus = 0

# total_salary = salary + bonus

# print(f"Bonus = {int(bonus)}")
# print(f"Total Salary = {int(total_salary)}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# a=int(input ("enter the num "))
# b=int(input ("enter the num "))

# for i in range (a,b+1,1):
#     print(i)


# Write a function to print all numbers from b to a in reverse order using a loop.
# a=int(input ("enter the num "))
# b=int(input ("enter the num "))
# while a>b:
#     print(a)
     #a-=1 


#  Write a function to print all even numbers between a and b using a loop.
# a=int(input ("enter the num "))
# b=int(input ("enter the num "))
# while a>=b:
#     if b%2==0:
#      print(b)
#     b+=2
    


# Write a function to print all numbers between a and b that are divisible by a given number n.
# a=int(input ("enter the num a: "))
# b=int(input ("enter the num b: "))
# n=int (input("enter the divisible num:"))

# while a<=b:
#     if a%n==0:
#         print(a)
#     a+=1



# # Write a function to print all odd numbers between a and b in reverse order using a loop.
# def print_odd_reverse(a, b):
#     # write your code here

#     while b>=a:
#       if b%2!=0:
#          print(b)
#       b=b-1   
# print_odd_reverse(1, 10)
# print_odd_reverse(5, 15)
# print_odd_reverse(10, 20)    


# # Write a function to count how many odd numbers are between a and b.
# def count_odd(a, b):
#     # write your code here
#     sum=0
#     while a<=b:
#         if a%2!=0:
#            sum=sum+1
#         a=a+1
#     print(sum)                  
            
# count_odd(1, 10)
# # count_odd(5, 20)
# # count_odd(10, 15)


# # Write a function to count how many numbers are divisible by a given number between a and b.
# def count_divisible(a, b, n):
#     # write your code here
#     sum=0
#     while a<=b:
#         if a%n==0:
#            sum=sum+1
#         a=a+1
#     print(sum)       


# count_divisible(1, 10, 2)
# count_divisible(5, 25, 3)
# count_divisible(10, 50, 5)




# Write a function to find the sum of all numbers from a to b using a loop.
# def sum_range(a, b):
#     # write your code here
#     sum=0
#     while a<=b:
#         sum=sum+1
#         a=a+1
#     print(sum)       
# sum_range(1, 5)
# sum_range(3, 7)
# sum_range(10, 12)



# Write a function to find the sum of numbers from 1 to n.
# def sum_to_n(n):
#     # write your code here
#     sum=0
#     num=1
#     while n>=num:
#         sum=sum+1
#         num=num+1   
#     print(sum)    
# sum_to_n(5)
# sum_to_n(10)
# sum_to_n(3)



# Write a function to find the factorial of a given number using a loop.
# def factorial(n):
    
#     # write your code here
#     fac=1
#     while n>0:
#         fac= fac * n
#         n=n-1
#     print(fac)    


# factorial(5)
# factorial(3)
# factorial(7)



# Write a function to calculate taxi fare based on the following rates:
# First 10 km → ₹15/km
# Next 20 km → ₹12/km
# Beyond 30 km → ₹10/km
# def taxi_fare(distance):
#     # write your code here
#     if distance<=10:
#         total=distance*15
#     elif distance<=30:
#         total=(10*15)+(distance-10)*12
#     else:
#         total=(10*15)+(20*12)+(distance-30)*10
#     print(total)    

              

# taxi_fare(10)
# taxi_fare(15)
# taxi_fare(35)


# Write a function to calculate total reward for a given number of steps.
#  For every 1000 steps → ₹5
#  Every 5000th step → bonus ₹20
# def total_reward(steps):
#     # write your code here
#     reward=(steps//1000)*5
#     if steps>=5000:
#        reward += 20
#     print(reward)     
# total_reward(4000)
# total_reward(6000)
# total_reward(10000)



# # Write a function to find how many un-popped balloons remain after n balloons are inflated.
# #  Every 4th balloon pops automatically.
# def balloons_left(n):
#     # write your code here
#     pop=n//4
#     rem=n-pop
#     print(pop)
# balloons_left(39)
# # balloons_left(10)
# # balloons_left(20)



# Write a function to calculate total savings after n months.
#  The person saves ₹100 in the first month and increases savings by ₹50 every month.
# def total_savings(months):
#  write your code here
# saving=0
# monthly_saving=100
# for month in range (1,months+1):
#     saving+=monthly_saving
#     monthly_saving+=50
#     print(saving)

# total_savings(1)
# total_savings(3)
# total_savings(6)




# def water_level(minutes):
#     water = 0  # current water level starts at 0 liters

#     for i in range(1, minutes + 1):
#         water += 7      # tank fills 7 liters per minute
#         water -= 3      # tank leaks 3 liters per minute

#         # make sure water doesn’t go above 100 liters
#         if water > 100:
#             water = 100

#     print("Water level after", minutes, "minutes =", water, "liters")
#     def water_level(minutes):
#      water_level(1)
#     water_level(10)
#     water_level(30)




# def total_reward(steps):
#     # write your code here
#     if steps<5000:
#         total=(steps//1000)*5
#     else:
#         total =(steps//1000)*5+(steps//5000)*20
#     print(total)
# total_reward(4000)
# total_reward(6000)
# total_reward(10000)



