N = int(input("enter an integer that is greater than 1: "))

if N > 1:
    average = 0
    for i in range(1, N + 1):
        average += i / N 
    print(f"The average of the numbers in range is: {average}")
else:
    print("please enter an integer that is greater than 1")
