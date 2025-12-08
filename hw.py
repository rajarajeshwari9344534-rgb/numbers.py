# a=int(input("enter the num:"))
# b=int(input("enter the num:"))
# c=a+b
# if c%2==0:
#     print("even")
# else:
#     print("odd")







# n=int(input ("enter the num:"))
# o=n//10
# p=n%10
# m=o+p
# j=o*p
# if m+j==n:
#     print("Greater")
# else:
#     print("no greater")   
#  






# distance =float(input("Enter your traveled km:"))
# fare = 0
# if distance <=5:
#     fare = distance*10
# elif distance >5  and distance <=15:
#     fare = distance * 8
# else:
#     fare = distance *6
# print("your ola fare:",fare)






# X = int(input("Enter a number1:"))
# Y = int(input("Enter a number2:"))
# Z = int(input("Enter a number3:"))
# if X==Y==Z:
#     print("Equilateral ")
# elif X!=Y and Y!=Z and Z!=X:
#     print("Scalene")
# elif X==Y or Y==Z or Z==X:
#     print("Isosceles")
# else:
#     print("Not a valid triangle")





# a= input("Enter your stream (Science/Commerce/Arts): ")
# match a:
#     case "Science":
#         b = input("Enter your choice (Medical/Engineering): ")
#         match b:
#             case "Medical":
#                 print("Chosen Path: Science → Medical")
#             case "Engineering":
#                 print("Chosen Path: Science → Engineering")
#             case _:
#                 print("Invalid sub-choice for Science")
#     case "Commerce":
#         b = input("Enter your choice (CA/B Com): ")
#         match b:
#             case "CA":
#                 print("Chosen Path: Commerce → CA")
#             case "B Com":
#                 print("Chosen Path: Commerce → B Com")
#             case _:
#                 print("Invalid sub-choice for Commerce")
#     case "Arts":
#        b = input("Enter your choice (History/Literature): ")
#        match b:
#             case "History":
#                 print("Chosen Path: Arts → History")
#             case "Literature":
#                 print("Chosen Path: Arts → Literature")
#             case _:
#                 print("Invalid sub-choice for Arts")
#     case _:
#         print("Invalid stream choice")




# time = int(input("enter your time (24 hours):"))
# if 9<time and time<12:
#     print("Morning Show")
# elif 12<= time and time <16:
#     print("Matinee show")
# elif 16<= time and time<20:
#     print("Evening Show")
# else:
#     print("night Show")




# km = float(input("Enter value in kilometers: "))
# choice = input("Enter your choice (1/2/3/4): ")
# match choice:
#     case "1":
#         meters = km * 1000
#         print(f"{km} kilometers = {meters} meters")
#     case "2":
#         centimeters = km * 100000
#         print(f"{km} kilometers = {centimeters} centimeters")
#     case "3":
#         millimeters = km * 1_000_000
#         print(f"{km} kilometers = {millimeters} millimeters")
#     case "4":
#         miles = km * 0.621371
#         print(f"{km} kilometers = {miles:.4f} miles")
#     case _:
#         print("Invalid Conversion")





# payment_mode = input("Enter your payment mode (UPI/Card/NetBanking/COD): ")
# match payment_mode:
#     case "UPI":
#         print("You selected UPI payment")
#     case "Card":
#         print("You selected Debit/Credit Card payment")
#     case "NetBanking":
#         print("You selected Net Banking")
#     case "COD":
#         print("You selected Cash on Delivery")
#     case _:
#         print("Invalid Payment Mode")


# n=19
# count = 0
# output =" "
# while n>count:
#     output = output + str(n)+ " "
#     n=n-2
# print(output)



# n=20
# counter = 20 
# while counter>0:
#   print(counter)
#   counter=counter-1





# n=100
# count=0
# end_value=n
# while count<=end_value:
#     if count%5==0:
#         print(count,end= " ")
#         count = count +5





# n=int(input ("enter the value:"))
# start_num=1
# end_num=10
# while start_num<=end_num:
#     print(n,"x",start_num,"=",n*start_num)
#     start_num=start_num+1




# starting_num=1
# end_num=5
# total=0
# while starting_num<=end_num:
#     total=total+starting_num
#     starting_num=starting_num+1
# print("the sum of num is:",total)




# starting_num=1
# end_num=10
# total=0
# while starting_num<=end_num:
#     total=total+starting_num
#     starting_num=starting_num+1
# print("the sum of num is:",total) 


# start = 1
# end = 10
# total = 0

# while start <= end:
#     if start % 2 == 0:      
#         total = total + start
#     start = start + 1  

# print("Sum of even numbers from 1 to 10 is:", total)


# start=1
# end=100
# total=0
# while start<=end:
#     if start % 2 == 0:
#         total=total+start
#     start= start+1
# print("sum of the even numbers from 1 t0 is:",total)           



# a= int (input("enter the number :"))
# b= int (input("enter the number :"))
 
# if a>=b:
#     num=a
#     while num<=b:
#         print(num)
#         num+=1

# else:
#     num=a
#     while num>=b:
#         print(num)
#         num-=1         


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a <= b:
#     num = a
#     while num <= b:
#         print(num)
#         num += 1
# else:
    
#     num = a
#     while num >= b:
#         print(num)
#         num -= 1  

# a = int(input("Enter the first number: "))
# i=1
# while i<=a:
#      print(i**3)
#      i+=1


# a=int(input("enter the number:"))
# b=int(input("enter the value:"))
# i=1
# while i<=b:
#     print(a)
#     a=a+1
#     i=i+1


# a=int(input("enter the number:"))
# i=1
# while i<=a:
#    num=(i**2)+1
#    print(num,end=" ")
#    i+=1

# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print("Reversed number =", rev)




# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print("Number of digits =", count)


# N = int(input("Enter number of terms: "))
# a, b = 0, 1
# count = 0
# while count < N:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1



# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print("Number of digits =", count)


# print 1to 100 numbers

# num=100
# n=1
# while num>=n:
#     print(n,end=" ")
#     n+=1


# print 1 to n numbers
# n=1
# num=0
# while num<=n:
#     print(n)
#     n+=1


# # print even num 1 to 100
# st=2
# ed=100
# while ed>=st:
#     print(st)
#     st+=2


# #print all even n numbers
# st=2
# ed=0
# while ed>=st:
#     print(st)
#     st+=2

# a=int (input("enter the num"))
# b=int (input ("enter the num"))
# for i in range (b,a-1,-1):
#     print(i)



# a=int (input("enter the num"))
# for i in range (2,a+1,2):
#     print(i)

# a=int(input ("enter you num"))
# for i in range (a,2,-2) :
#     print(i)      







    



