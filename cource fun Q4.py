def showNumbers(limit):
    i=1
    while i<=limit:
        if i%2==0:
            print("even:",i)
        else:
            print("odd: ",i)
        i+=1
showNumbers(12)