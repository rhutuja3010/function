def number(limit):
    i=0
    sum=0
    while i<=12:
        if i%3==0 or i%5==0:
            sum+=i
            print(sum)
        i+=1
number(12) 
