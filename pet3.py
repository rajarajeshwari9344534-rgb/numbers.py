# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* " * i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"* "*i)

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)


# n=5
# for i in range(n):
#     print(n* " * ")    

# n=5
# for i in range(n+1):
#     print("* " *i)
# for i in range(n,0,-1):
#     print("* "*i)

# n=5
# for i in range(n,0,-1):
#     print("* "*i)
# for i in range(2,n+1):
#     print("* "* i)        


# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(j ,end=" ")
#     print()    

n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print(i,end=" ")
        else:
            if j==1 or j==n:
                 print(i,end=" ")
            else:
                print(" ",end=" ")
    print()    


n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print(i,end=" ")
        else:
            if j==1 or j==n:
                print(i,end=" ")
            else:
                print(" ",end=" ")    
    print()
                



