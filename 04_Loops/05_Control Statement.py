"""
Break : To stop the loop in between we use break statement. Code which is present after break it is not execute once the break statement triggers
Syntax :

for i in range (i,a)
    print(i)
    if i == b:

        break
    code()
    code()

Continue : To skip the code in some condition we use continue statement. Code which is present after continue in loop it will get skip for that perticular condition  
Syntax:

for i in range (i,a)
    print(i)
    if i == b:
        continue
    code()
    code()

Pass : Kuch nhi krta 
"""

for i in range(1, 11):
    print(i)
    if i == 5:
        break

for i in range(1, 11):
    print(i)
    if i == 5:
        continue
    print("OK")
    print("Done")

for i in range(1, 11):
    print(i)
    if i == 5:
        pass
    print("OK")
    print("Done")
