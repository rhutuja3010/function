# def check_number ():
#     a=int(input("enter the 1st number"))
#     b=int(input("enter the 2nd number"))
#     if a%2==0 and b%2==0:
#         print("dono number even hai")
#     else:
#         print("dono number even nahi hai")
# check_number()



def check_number_list(x,y):
    i=0
    while i< len(x):
        if x[i]%2==0 and y[i]%2==0:
            print(i,"even")
        else:
            print(i,"odd no")
        i+=1
check_number_list([2,6,18,10,3,75],[6,19.24,12,3,87])