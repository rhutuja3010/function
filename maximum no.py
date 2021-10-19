def max_function():
    numbers = [3, 5, 7, 34, 2, 89, 2, 5]
    i=0
    num=numbers[0]
    while i<len(numbers):
        if numbers[i]>num:
           num=numbers[i]
        i+=1
    print(num)
max_function()