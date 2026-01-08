# try:
#     a=int(input ("enter the num"))
#     b=int(input("enter the another the num"))
#     c=a/b
#     print(f"result of dividing {a}+{b}={c}")
# except ZeroDivisionError:
#     print("invalid second num it cannot be zero")
# except ValueError:
#     print("you have enter the word instead of a number ") 
# except:
#     print("some error has occurred while execution")  


# try:
#     a=int(input ("enter the num"))
#     b=int(input("enter the another the num"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("invalid second num it cannot be zero") 
# except ValueError:
#     print("you have enter the word instead of a number reenter the num ")
#     a=int(input ("enter the num"))           
#     c=a/b
#     print(c)



# num=[9,6,8,9,5,7,9]
# max=num[0]
# count=0
# for i in range (1,len(num)):
#     if num[i]>max:
#         max=num[i]
# for i in range (len(num)):
#     if max==num[i]:
#         count+=1
# print(count)     


# num=[1,2,3,4,5,3]
# x=5
# for i in range (len(num)):
#     if num[i]!=x:
#         print(-1)
#         break
#     else:
#         for i in range (len(num)):
#             if num [i]==x:             
#                 print(num[i])    


# a=[0,1, 2, 3, 4, 5, 6,7,9,11]
# count=0
# total=0
# for i in range (len(a)):
#     if a[i]%2==0:
#        count=count+1
#     else:
#         total=total+1  
# print("even", count, "odd", total)



# def num(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             print("starting index:",i)
#             break
#     for i in range(len(arr)-1,0,-1):
#         if arr[i]==target:
#             print("ending index:",i)
#             break
    # first=-1
    # last=
    # for i in range(len(arr)):
    #     if arr[i]==target:
    #         print(i)

 
# num ([5, 2, 3, 5, 7, 5, 8], 5) 



# str=(input("enter the sentence"))
# words = str.split()
# reversed = words [::-1]
# reversed_sentence= " ".join(reversed)
# print(reversed_sentence)
 

# word = "Python"
# rev = word[::-1]
# print("Reversed:", rev)


# word = "Python"
# rev = ""
# for i in range(len(word)):
#     rev = word[i]+rev
# print("Reversed:", rev)




# text = "Education"
# count = 0
# for ch in text:
#     if ch == "a" or ch== "e" or ch=="i" or ch=="o" or ch=="u":
#         count = count + 1
#     elif ch == "A" or ch== "E" or ch=="I" or ch=="O" or ch=="U":
#         count = count + 1  
# print("Vowels:", count)


# nums = [9, 5, 3, 8,1]
# min_num = nums[0]
# for i in range(1, len(nums)):
#     if nums[i] < min_num:
#         min_num = nums[i]
# print(min_num)

# 4. There is an error while printing alternate elements from the list. Please identify and correct it.
# lst = [10, 20, 30, 40, 50]
# for i in range (0,len(lst),2):
#      print(lst[i])


# nums = [-3, 5, -2, 7]
# for i in range(len(nums)):
#     if nums[i] < 0:
#         nums[i]= 0
# print(nums)



# text = "Education"
# count = 0
# for ch in text:
#     if ch in 'aeiouAEIOU':
#         count = count + 1 
# print("Vowels:", count)

# Write a program to reverse a given string.
# str=input()
# rev=""
# for i in range (len(str)):
#     rev=str[i]+rev
# print(rev)


# Check whether a given string is a palindrome or not.
# text="madam"
# rev1= text[::-1]
# rev=""
# for i in range (len (text)):
#     rev=text[i]+rev
#     if rev==text:
#        value="yes"       
#     else:
#         value="No"  
# print(value)          




# name=["jon","don","sam","raji"]
# sal=[1200,3000,50000,50000]
# max=sal[0]
# max_index=0
# for i in range (len(sal)):
#     if sal[i]>max:
#         max=sal[i]
#         max_index=i
# for i in range (len(name)):
#     if sal[max_index]==sal[i]:
#         num=name[i]
#         print(num)

# # 1. There is an error while counting how many times a number appears in the list. Please identify and correct it.
# nums = [1, 2, 3, 2, 2, 4]
# target = 2
# count = 0
# for i in range(len(nums)):
#     if nums[i] == target:
#         count += 1
# print(count)


# # 2. There is an error while comparing two strings character by character. Please identify and correct it.
# s1 = "cat"
# s2 = "cqt"
# same = True
# for i in range(len(s1)):
#     if s1[i] != s2[i]:
#         same = False
# if same == True:
#     print("Same")
# else:
#     print("Different")
# 
# # 3. There is an error while counting spaces in a given sentence. Please identify and correct it.
# sentence = "Python is fun "
# spaces = 0
# for ch in sentence:
#     if ch == " ":
#         spaces += 1
# print("Spaces:", spaces)


# 4. There is an error while finding the frequency of each character in a string. Please identify and correct it.
# text = "banana"
# for ch in text:
#     c = 0
#     for i in range(len(text)):
#         if text[i] == ch:
#             c = c + 1
#     print(ch, ":", c)


# 5. There is an error while counting the number of words in a given string. Please identify and correct it.
# text = "I love Python raji sanju"
# count = 1
# for ch in text:
#     if ch == " ":
#         count+= 1
# print("Words:", count)


# arr=[1,2,3,4,5,6,7,8,9,10]
# count=1
# start=arr[0]
# mul=0
# count2=0
# for i in range(1,len(arr)):
#     start+=arr[i]
#     count+=1
# mul=start//count
# for i in range (len(arr)):
#     if arr[i]>mul:
#         count2+=1
# print(count2)       



# arr=[1,2,3,4,5,6,7,8,9,10]
# soo=sum(arr)/len(arr)
# count=0
# for i in arr :
#         if i < soo:
#              count+=1
# print(count)        

# # Given a list of numbers, count how many are even and how many are odd.
# arr=[1,2,3,4,5,6,7,8,9]
# count1=0
# count2=0
# for i in range (len(arr)):
#     if arr[i]%2==0:
#         count1+=1
#     else:
#         count2+=1
# print("even",count1,"odd",count2)


        
# # Input a number and print the sum of its digits.
# num=int(input("enter the num"))
# total=0
# while num > 0:
#     digit = num % 10 
#     total+=digit  
#     num //= 10       
    
# print(total)  

# Reverse a String
# word="hello"
# print(word[::-1]) 


# word="banana"
# target=input()
# for i in range(len(word)):
#     if word[i]==target:
#         print(i)
#     else:
#         print("not found")    


# list1="python"
# list2="notebook"
# for i in range(len (list1)):
#     if list1[i]==list2[i]:
#         num=(list2[i])
# #         print(num)     



# list1 = "python"
# list2 = "notebook"

# common = ""
# for ch in list1:
#     if ch in list2 and ch not in common:
#         common += ch

# print("Common letters:", common)


# string = input("Enter brackets: ")
# count = 0
# balanced = True

# for ch in string:
#     if ch == '(':
#         count += 1
#     elif ch == ')':
#         count -= 1
#     if count < 0:   # means a closing bracket came before an opening one
#         balanced = False
#         break

# if count == 0 and balanced:
#     print(True)
# else:
#     print(False)

# last_month_score = [45, 60, 70, 55, 80]
# this_month_score = [50, 58, 75, 65, 78]
# for i in range (len(last_month_score)):


# #test case 1
# nums = [4,2,7,2,9,3,2,8]
# k = 2
# num=[]
# for i in range (len(nums)): 
#     if nums[i]==k:
#         num.append(i)
# if len(num)==0:
#     print("not found")
# else:
#     print(num)  



# nums = [1,3,7,8,9]
# rev=[]
# for i in range (len(nums)-1,-1,-1):
#     rev.append(nums[i])
# print(rev)
  



# str = "helloWorld"
# count=0
# for i in range(len(str)):
#     if str[i]>='A' and str[i]<'Z':
#         count+=1
# print(count)



# # ### LISTS
# # - Given a list, rotate it right by k positions.
# # ```python
# # #test case 1:
# # Input: nums = [4,6,9,2,3,11], k = 2
# # Output: [3,11,4,6,9,2]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# nums=[4,6,9,2,3,11] 
# k=2
# total=[]
# for i in range (len(nums)):
#     if nums[i]==2:
#        value=i
# lst=nums[value+1:] 
# total+=lst
# lst2=nums[:value+1]
# total+=lst2
# print(total)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# sentence = "apple and banana"
# words= sentence.split()
# for i in range (len(words)):
#     if words[i]== "and":
#         words[i-1],words[i+1]= words[i+1],words[i-1] 
# print(" ".join(words))        

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# - Write a program that finds the longest word in a given sentence.
#   (Bonus: If you are too studious, try without using `split(" ")` and solve)
# ```python
# # test case 1
# Input: "Johannesburg is the most populous city of South Africa"
# Output: "Johannesburg"
# # based on the word length -> it is Johannesburg




# str="Johannesburg is the most populous city of South Africa"
# lng=""
# word=""
# for i in range (len(str)):
#     if str[i]!=" ":
#         word+=str[i]
#     else:
#         if (len(word))>(len(lng)):
#             lng=word
#         word=""

# if len(word)>len(lng):
#     lng=word
# print(lng)   
 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

              
# A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False 
# [10,5,6] → False   

# lst=[10,5,6]
# max=lst[0]

# for i in range(1,len(lst)):
#     if lst[i]>max:
#        sol=True
#     else:
#        sol=False
#        break
# print(sol)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # 4. Replace characters at odd indexes with *.
# # Example: "hello" → "h*l*o"

# word = "hello"
# lst = ""

# for i in range(len(word)):
#     if i % 2 != 0:      
#         lst += "*"
#     else:
#         lst+= word[i]

# print(lst)

        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
        
# str= "Python is super powerful"
# smallest_word = ""
# word = ""
# for char in str:
#     if char != " ":
#         word += char
#     else:
#         if smallest_word == "" or len(word) < len(smallest_word):
#             smallest_word = word
#         word = ""
# if smallest_word == "" or len(word) < len(smallest_word):
#     smallest_word = word
# print(smallest_word)       
        
# list=[1,2,3,4,5]
# print(list[1:len(list)])


# nums = [2,4,3]


# nums = [2,4,3]
# target = 5
# for i in range(len(nums)):
#     for a in range(i+1,len(nums)):
#         list = nums[i]+nums[a]
#         if list==target:
#             print(i,a)


# arr=[1,33,44,55,88,33,55,88,55,88,66,88]
# max=arr[0]
# count=0
# for i in range (1,len(arr)):
#     if arr[i]>=max:
#         max=arr[i]
# for i in range(len(arr)):
#     if arr[i]==max:
#         count+=1
# print(count)    
# 

# str="This is a pen"
# tr="is"
# count=0
# for i in range (len(str)):
#     if str[i]==tr:
#         count+=1 
# print(count)                    
           


# target = 5
# for i in range(len(nums)):
#     for a in range(i+1,len(nums)):
#         list = nums[i]+nums[a]
#         if list==target:
#             print(i,a)



# def highest_marks(names, maths, physics, chemistry):
#     max_total = 0
#     topper = ""

#     for i in range(len(names)):
#         if maths[i] > 90 and physics[i] > 90 and chemistry[i] > 90:
#             total = maths[i] + physics[i] + chemistry[i]

#             if total > max_total:
#                 max_total = total
#                 topper = names[i]

#     print(topper)

# highest_marks(["jason", "priya", "madhan", "syed"],
#               [91, 92, 81, 75],
#               [91, 99, 100, 90],
#               [91, 95, 100, 90])


# arr1=[1,2,3,4,5,6,7,8,9]
# arr2=[2,4,6,8,9,4,6,8,9]
# count1=0
# count2=0
# for i in range(len(arr1)):
#     if arr1[i]%2==0:
#         count1+=1
# for i in range(len(arr2)):
#     if arr2[i]%2==0:
#         count2+=1
# if count1>count2:
#     print(arr1)
# else:
#     print(arr2)   

# str="there is good, and it is bad. iam" 
# count=1
# for i in range(len(str)):
#     if str[i]==" "and "," and ".":
#         count+=1
# print(count)  


# n=int(input("enter the num"))
# n2=int(input("enter the num")) 
# for i in range (n+1,n2,1):
#     print(i)

# arr=[54,3,2,34,4,5,6,4]
# for i in range (len(arr)):
#     if arr[i]==i:
#         print(i)



# def born_in_first_half(names,birthdates):
#     name_list = []
#     for i in range(len(birthdates)):
#         day = int(birthdates[i].split('/')[0])
#         month = int(birthdates[i].split('/')[1])
#         if month > 0 and month < 7:
#             name_list.append(names[i])
#     print(name_list)

# born_in_first_half(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"], ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"])    


# word1="apple"
# word2="alple"
# num=0
# count=0
# less=len(word1)-1
# count2=0

# if len(word1)!=len(word2):
#     print("invalid input")
# else:
#     for i in range (len(word1)):
#         if word1[i]==word2[num]:
#            count=count+1
#            num+=1
#         else:
#             count2+=1 
#             num+=1  
# if count==less:
#     print("yes")
# else:
#     ("invalid input")      


# names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"]

# birthdates = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]

# result=[]
# for i in  range(len(birthdates)):
#     if int(birthdates[i][-1]) <7 and birthdates[i][-2]=="0":
#         result.append(names[i])
# print(result)        

# word1="apple"
# word2="alple"
# count=0

# if len(word1)!=len(word2):
#     print("Invalid  Input")
# else:
#     for i in range(len(word1)):
#         if word1[i]!=word2[i]:
#             count+=1
# if count==1:
#     print("yes") 
# else:
#     print("invalid input")
# 





# books=[98, 75, 60, 50, 40, 25]
# newBook=55        
# if len(books) == 0:
#         print(-1)
# else:
#     result = 0
#     for i in range(0,len(books), +1):
#         if newBook <= books[i - 1] and newBook >= books[i]:
#             result = i 
#     print(result) 


# # 2. Print the below pattern of '*' if n = 32. Print the below pattern of '*' if n = 3
# n=3
# ops="*"
# for i in range (1,n+1):
#     if sum<
#     print(ops,end=" ")
       

# str="I am bring the apple"
# word=""  
# store=str.split()
# for ch in store:
#     if ch[0]=="a":
#       print(ch)            



# arr=[1,0,4,5,0,6,7,0,9,0]
# atr=[]
# cut=[]
# for i in range(len(arr)):
#     if arr[i]!=0:
#         atr.append(arr[i])
#     else:
#         cut.append(arr[i])
# print(atr+cut)    



# arr=[1,2,3,4,5]
# word=0
# count=0
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         word+=arr[i]*arr[i]
# print(word)        

     


# alphabet = "abcdefghijklmnopqrstuvwxyz"

# start = input("Enter start letter: ")   
# end = input("Enter end letter: ")       

# i = alphabet.index(start)
# j = alphabet.index(end)

# while i <= j:
#     print(alphabet[i], end=" ")
#     i += 1



# arr=[2,2,3,4,5]
# store=0
# for i in range (len(arr)):
#     if arr[i]%2!=0:
#         word=i
#         store+=word
#         word=0
# print(store)        
        

# str= "rajarajeshwari,kavin,ranjith,indhu,kalai"
# word=str.split()
# count=0
# for i in range (len(str)):
#     if str[i] in "aeiou":
#         count+=0        


# arr=[1,1,3,4,4,7,6,8]
# count=0
# for i in range (len(arr)):
#     if arr[i]==i:
#         count+=1    
# print(count)  

# lst=[1, 5, 8, 3, 7, 9, 3, 7, 9, 2]
# sub=[3, 7, 9]
# count=0
# for i in range(len(lst)):
#     if lst[i] in sub:
#         count+=1
# if count==len(sub)*2:
#     print("true") 
# else:
#     print("false")       



# s1 = "ABCDE"
# s2 = "CDEAB"
# if len(s1) != len(s2):
#   print (False)
# else:
#     print (s2 in (s1 + s1))


# arr=[3, 5, -9, 1, 3, -2, 3, 4, -1, 2]
# n = len(arr)
# max_sum = arr[0]

#     # Check all possible subarrays
# for i in range(n):               # starting index
#     for j in range(i, n):        # ending index
#         current_sum = 0

#             # calculate sum of subarray arr[i...j]
# for k in range(i, j + 1):
#     current_sum += arr[k]

#     if current_sum > max_sum:
#          max_sum = current_sum

# print(max_sum)



# store=""
# for i in range(len(str)):
#     if str[i]!=",":
#        store+=str[i]
# print(store)


# s="Bharath,100|velu,50|ganesh,20"
# result = []
# for item in s.split("|"):
#     name, mark = item.split(",")
#     result.append( {name,  int(mark)})
# print(result)    
  


# s="Bharath,100|velu,50|ganesh,20"
# result = []
# str = ""
# pair = []

# for ch in s:
#     if ch == ',':
#         pair.append(str)
#         str = ""
#     elif ch == '|':
#         pair.append(str)
#         result.append(pair)
#         pair = []
#         str = ""
#     else:
#         str += ch
# print(result)     
   

# data = "abi,99|priya,98|ram,100"
# records = data.split("|")
# max_name = ""
# max_mark = 0
# for rec in records:
#     name, mark = rec.split(",")
#     mark = int(mark)
#     if mark > max_mark:
#         max_mark = mark
#         max_name = name
# print("Top Scorer:", max_name, max_mark)     


# data = "abi,99|priya,98|ram,100"
# word=data.split("|")
# max_name=""
# max_mark=0
# for ch in word:
#     name,mark=ch.split(",")
#     mark=int(mark)
#     if mark> max_mark:
#         max_mark=mark
#         max_name=name
# print(max_mark, max_name)       





# season = input("Enter a season: ").lower()

# city = ["chennai", "trichy", "coimbatore", "bangalore", "salem"]
# summer  = [38.0, 40.0, 32.0, 30.0, 37.0]
# monsoon = [30.0, 32.0, 28.0, 25.0, 29.0]
# winter  = [25.0, 24.0, 20.0, 18.0, 23.0]


# data = {
#     "summer": summer,
#     "monsoon": monsoon,
#     "winter": winter
# }

# if season not in data:
#     print("Invalid season")
# else:
#     sea= data[season]
#     max_season = sea[0]
#     max_city=city[0]
#     for i in range(1, len(sea)):
#         if sea[i] > max_season:
#             max_season = sea[i]
#             max_city = city[i]

#     print( max_city, max_season)





    
# for i in range(0,len(season)):
#     if season[i]>max:
#         max=season[i]
#         name=city[i]
# print(name)         



# arr= [10,20,30,40,50]
# sum=0
# count=0
# for i in range (len(arr)):
#     if arr[i]>0:
#         sum+=arr[i]
# avg=sum//len(arr) 
# for i in range(len(arr)):
#     if arr[i]>avg:
#         count+=1
# print(count)               



# str= 'programming'
# emp=""
# for i in range(len(str)):
#     if str[i] not in emp:
#         emp+=str[i]
# print(emp)   




# str="Data science evolves every year"
# word=str.split(" ")
# big=word[0]
# for j in word:
#     if len(big)<len(j):
#         big=j   
# print(big)        


# str="Learning Python is interesting"
# word= str.split(" ")
# count=0
# max=""
# for j in str:
#     for i in range(len(j)):
#         if j[i] in "aeiou": 
#             count+=1
#             if j[i] ==" ":
#                max=j               




# str="This is a python program"
# word=str.split(" ")
# max=""
# for i in word:
#     if len(i)>4:
#        max+=i+" "
# print(max)    
   

# str="HARI@1234!7*_-the"
# output=""
# for ch in str:
#     if ch.islower():
#       output+=ch
#     elif ch.isupper():
#        c=ch.lower()
#        output+=c
#     elif ch in "1234567890_":
#        output+=ch
# print(output)    



# str="Fresh, Organic; Apples."
# sa=""
# for ch in str:
#     if ch.isupper():
#         sa+=ch
#     elif ch.islower():
#         sa+=ch
#     elif ch==(" ") :
#         sa+=ch   
#     elif ch in "1234567890" :
#         sa+=ch
# print(sa)                



# Input: ab#12!cd@EF3
# Output: AB12CDEF3
# Input: !!SAVE20!!
# Output: SAVE20


# str= "!!SAVE20!!"
# sa=""
# for ch in str:
#     if ch.islower():
#         c=ch.upper()
#         sa+=c  
#     elif ch.isupper():
#         sa+=ch
#     elif ch in "1234567890":
#         sa+=ch
# print(sa)          


# str="They also manage salaries record attendance record leave record"
# s="record"
# count=0
# word=str.split()
# for ch in word:
#     if ch == s:
#         count+=1
# print(count)        



# str="heeellooooo!1"
# emp=""
# for ch in str:
#     if ch not in emp:
#         emp+=ch
# print(emp)        
           



# str="A3@b5"
# letters=0
# digits=0
# others=0

# for ch in str:
#     if ch.islower():
#        letters+=1 
#     elif ch.isupper():
#        letters+=1
#     elif ch in "1234567890":
#         digits+=1
#     else:
#         others+=1
# print("letters:",letters,"digits:",digits,"others:",others)     
# 

# lst=[3, 5, 2, 6, 7]
# count=0
# for i in range (len(lst)):
#     for j in range (1,len(lst)):
#         if lst[i]<lst[j]:
#             count+=1
# print(count)   



# input=[3, -2, 8, -5, 0]
# sum=0
# for i in range (len(input)):
#     if input[i]<0:
#         sum+=input[i]
# print(sum)


# str="aaabbccccddeeefffff"
# count = 1
# max_count = 1
# max_char = str[0]

# for i in range(1, len(str)):
#     if str[i] == str[i-1]:
#         count += 1
#     else:
#         count = 1
#     if count > max_count:
#         max_count = count
#         max_char = str[i]
# print(max_char,"=",max_count)       
# 


# lst = [2, 3, 4]
# val = 1
# for i in lst:
#     val *= i
# print(val)




# input= ["ab12", "hello", "9nine", "cat"]
# num="1234567890"
# for ch in input:
#     for i in range(len(ch)):
#         if ch[i] in num:
#             print(ch)
#             break


# lst= ["hello", "world", "hello", "ai", "world","world","hello"]
# emp=[]
# word=[]
# for ch in lst:
#     if ch not in emp:
#         emp.append(ch)      
#     else:
#         if ch not in word:
#            word.append(ch)
# print(word)        


# arr=[2,3,5,1,4]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)  
      

# lst=["ram", "suresh", "alexander", "tom"]
# str=[]
# for ch in lst:
#     if (len(ch))>3:
#         str.append(ch) 
# print(str)  


# lst=['H','e','l','l','o']
# emp=[]
# str=""
# for i  in range (len(lst)):
#     if i!=",":
#       str+=i
#       emp.append(str)
# print(emp)    


n1 = 8
n2 = 64
gcd = 0
min_val = 0
if n1 < n2:
    min_val = n1
else:
    min_val = n2
for i in range(1, min_val + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
lcm = (n1 * n2) // gcd
print(lcm)
         














        










	
