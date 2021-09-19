def car(speed):
    if speed < 70:
        print("ok")
    elif speed > 70:
        x=speed-70
        y=x//5
        print(y,"point")
        if y>=12:
            print("License suspended")
a=int(input("enter the speed"))
car(a)
            
        
        
        
        