current_year=int(input("enter the number"))
birth_year=int(input("enter the number"))
if current_year-birth_year>0:
    age=current_year-birth_year
    print("your age is:",age)
elif current_year-birth_year<1:
    print("your age is less than one year")
else:
    print("wrong age")



# def number(a):

#     i=1
#     while i<=10:
#         print(a,"*",i,"=",i*a)
#         i+=1
# number(3)