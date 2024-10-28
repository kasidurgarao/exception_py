try:   
    input1 = int(input("enter the vlaue"))
    input2 = int(input("enter the 2nd value"))
    result = input1/input2
    print(result)
# don't enter the input as zero
except ZeroDivisionError:
    print("enter the other than 0 in input2")