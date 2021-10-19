# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")

#     else:
#            print(num,"is not a prime number")
# primeorNot(9)



def primenumber(number):
    i=1
    count=0
# number=int(input("enetr the number"))
    while i<=number:
        if number%i==0:
            count+=1
        i+=1
    if count==2:
        print("it is prime number")
    else:
        print("it is not prime number") 
primenumber(7)