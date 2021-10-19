def calculator(number_x,number_y,operation):
    if operation == "multiply":
        return (number_x * number_y)
    elif operation ==  "add":
        return (number_x + number_y)
    elif operation== "divide":
        return(number_x / number_y)
    elif operation== "substract":
        return (number_x - number_y)
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=input("enter a operation")
d=calculator(a,b,c)
print(d)




# def list_change (list1,list2):
#     i=0
#     while i<len(list1):
#         print(list1[i]*list2[i])
#         i+=1
# list_change([5,10,50,20],[2,20,3,5])
        





    