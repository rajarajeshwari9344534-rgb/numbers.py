# Input= [4,3,2,2,3,1,7,8,8] 
# arr=[]
# out=[]
# for ch in Input:
#     if ch not in arr:
#         arr.append(ch)
#     else:
#         out.append(ch)   
# print(out)       



# matrix = [[1, 2,9],
#          [3, 4,9],
#          [5, 6,0]]
# def transpose(matrix):
#     result = []

#     for i in range(len(matrix[0])):  # column
#         row = []
#         for j in range(len(matrix)):  # row
#             row.append(matrix[j][i])
#         result.append(row)

#     return result
# print(transpose(matrix))




# n=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[j][i]==n:
#             print(j,i)


# matrix=[
#  [1, 2, 3],
#  [4, 5, 6]
# ]
# total=0
# for row in matrix:
#     for num in row:
#         total=total+num
# print(total)  
# 


"method 2"

# total=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         total+=matrix[i][j]
# print(total)    
# 


sam='aaabbbbcccaaa'
# result=""
# count=1
# for i in range(1,len(sam)):
#     if sam[i]==sam[i-1]:
#         count+=1
#     else:
#         result+=sam[i-1]+str(count)
#         count=1
# result+=sam[-1]+str(count)
# if len(result)>=len(sam):
#     print(sam)
# else:
#     print(result) 


# sam='aaabbbbcccaaa'
# result=""
# count=1
# for i in range(1,len(sam)):
#     if sam[i]==sam[i-1]:
#         count+=1
#     else:
#         result+=sam[i-1]+str(count)
#         count=1 
# result+=sam[-1]+str(count)
# print(result)



# n1 = int(input())
# n2 = int(input())

# gcd = 0
# min_val = 0

# if n1 < n2:
#    min_val = n1
# else:
#     min_val = n2

# for i in range(1, min_val + 1):
#     if n1 % i == 0 and n2 % i == 0:
#        gcd = i    

# lcm = (n1 * n2) // gcd
# print(lcm)



# word = "babad"
# st=""
# su=""
# for ch in word:
#     if ch not in st:
#         st+=ch
#     else :
#         su+=ch
# nwe=""        
# for ch in word:
#     if ch in su:
#         nwe+=ch
# print(nwe)        


# nums = [2, 0, 2, 1, 1, 0]
# min=nums[0]
# ls=[]
# for ch in nums:
#     if ch<=min:
#         min=ch
# for i in range(1,len(nums)):
#     if nums[i]<=min and nums[i]-1<=nums[i]:
#         ls.append(nums[i])
# print(ls)        


# num=5
# for i in range(1,num+1):
#     print(i)


# num=20
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)

# num=5
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)


    

















    
    