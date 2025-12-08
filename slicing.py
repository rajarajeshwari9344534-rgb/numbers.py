# #slicing
sentence = "I am Iron Man!"
# sliced_str = sentence[5:9]
# print(sliced_str)
# #slicing without end
# sliced_str = sentence[5:]
# print(sliced_str)
# sliced_str = sentence[:4]
# print(sliced_str)

# #slicing and concatenation

# result_str = sentence[0] + sentence[4:]
# print(result_str[::-1])


# #Strides
# result_str=sentence[::2]
# print(result_str)

# #Multi-line string
# about_me = """Hi, I am Iron Man. 
# I invented the arc reactor while being kidnapped.
# I enjoy flying and blowing things.
# Sometimes I save people in the process.
# Billionaire, Playboy and a Philanthropist"""

# print(about_me)

# #Traversing through a string using loop.
# # for i in range(len(sentence)):
# #     print(sentence[i])

# for ch in sentence:
#     print(ch)



# # tokenize 
# words = sentence.split(",")
# for w in words:
#     print(w)

# joined_str = " ".join(words)
# print(joined_str)

# sentence= "Iam rajarajeshwari iam good girl"
# sliced_str=sentence[:19]
# print(sliced_str)


# string="Apple"
# total=0
# for n in string:
#     if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
#          total+=1
#     elif n=="A" or n=="E" or n=="I" or n=="O" or n=="U": 
#          total+=1
# print(total)

# string="Apple"
# total=0
# for i in range (len(string)): 
#    if string[i] in 'aeiouAEIOU':
#        total =total+1
# print(total)      
 

# a='apple'
# print(a[::-1])

# str=[1,2,3,4,5,6]

# for name in str[::-1]:
#     print(name)

#---------------------------------------------------------------------------------------------------------------

'''15-10-2025'''

# num=[1,2,3,4,5,6,7,8,9,]
# n= int (input(" enter the num"))
# if n in num:
#         print("found")
# else:
#         print("not found")    




# numbers = [5, 10, 15, 20,5]
# total = 0

# for n in numbers:
#     total = total + n
# print(total)    
# if total % 2 == 0:
#     print("Sum is even")
# else:
#     print("Sum is odd")


# num_list = [8, 1, 0, 19, 11, 28, 3, 5]
# a=10
# b=20
# for n in num_list:
#     if n >a and n<b:
#       print(n)

#------------------------------------------------------------------------------------------------------


# a=[1,-2,-4,3,5,6,7,-8,5]
# total=0
# for n in a:
#     if n<0:
#       total=total+1
# print(total)



# a=[1,-2,-4,3,5,-8,5]
# total=0
# for i in range (len(a)):
#     if a[i]>0:
#       total=total+a[i]
#       i=i+1
# print(total)


# a=[1,2,3,4,5,6,7,8,9]
# for n in a:
#     if n%2==0:
#         print(n)


# a=[1,2,3,4,5,6,7,8,9]
# for n in a:
#     if n%2!=0:
#         print(n)


# a=[1,3,4,6,7,9,0,12,56,78,90]
# for n in a:
#     if n%3==0:
#         print(n)


# name=["sanju","raji","saru","keerthi","kalai","nandhini"]
# marks=[90,89,75,88,78,98,]
# student_dict=dict()
# for i in range(len(name)):
#     student_dict[name[i]]=marks[i]
# print(student_dict)    



# stud_dict = {90:"Antonia",
#         "Jeeva":60,
#         "Amstrong": 51,
#         "Ragavi": 81,
#         "Preethi": 75,
#          "sujithra":95,
#           "yuva" :99}
# query = ""
# print(stud_dict[query])

#----------------------------------------------------------------------------------------------------------------------------------
# a=[1,2,3,4,5,6,7]
# b=int(input("enter the num"))
# total=0
# for n in a:
#     if n>b:
#         total+=n
# print(total)  


# a=[1,2,3,4,5,6,7,8,9,10]
# total=0
# for n in a:
#     total=total+n
# print(total) 


# a=[1,2,3,4,5,6,7,8,9,10]
# total=0
# for n in a:
#     if n>5:
#       total=total+n
# print(total)  



# a=[1,2,3,4,5,6,7,8,9,10]
# total =(a[0])+(a[-1])    
# print(total)  
    
        

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0
# for i in range(1, len(a), 2):
#     total += a[i]
# print(total)        

# a=[1,2,3,4,5]
# total=0
# for n in a:
#     total=total+n
#     div=total//5
# print(div) 


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(1, 11):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)




#---------------------------------------------------------------------------------------------------------------------------------------------

           




