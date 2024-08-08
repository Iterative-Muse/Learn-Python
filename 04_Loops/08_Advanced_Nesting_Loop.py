"""
WAP a program to print below pattern 
        *
      * *
    * * *
  * * * *
* * * * *
"""

# for i in range (1,6):
#     for j in range (i,5):
#         print(" ",end=(" "))
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()


"""
WAP a program to print below pattern 
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range (1,i+1):
#         print(k,end=(" "))
#     print()


"""
WAP a program to print below pattern 
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range (1,i+1):
#         print(i,end=(" "))
#     print()

"""
WAP a program to print below pattern 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range(1,(i*2)):
#         print("*",end =(" "))
#     print()


"""
WAP a program to print below pattern 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print("*",end=" ")
#     print()

# for i in range(4,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range (1,(i*2)):
#         print("*",end=" ")
#     print()

"""
WAP a program to print below pattern 

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""

# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print("*",end=" ")
#     print()


"""
WAP a program to print below pattern 

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

for i in range(5, 1, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range(1, (i * 2)):
        print("*", end=(" "))
    print()
