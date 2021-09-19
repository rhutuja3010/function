# def perfect(a):
#     i=1
#     sum=0
#     while i<a:
#         if a%i==0 :
#             sum+=i
#             print(i)
#         i+=1
#     if a==sum:
#         print("it is perfect number")
#     else:
#         print("it is  not perfect number")
# perfect(6)


def perfect(a):
    # a=int(input("enter the number"))
    i=1
    sum=0
    while i<a:
        if a%i==0 :
            sum+=i
        i+=1
    print(i)
    if a==sum:
        print("it is perfect number")
    else:
        print("it is  not perfect number")
perfect(6)




# def perfect(a):
#     i=1
#     while i<=a:
#         if i%2==0:
#              print(i)
#         i+=1
# perfect(100)
        