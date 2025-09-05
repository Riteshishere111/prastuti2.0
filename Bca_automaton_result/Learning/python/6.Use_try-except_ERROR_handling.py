try:
    num=int(input("Enter a number: "))
    print(10/num) #This might cause an error is num is 0
except ZeroDivisionError:
    print("Cannot Divide by Zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
