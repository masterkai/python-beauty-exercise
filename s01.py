# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
print(type(+1E10))
print(+1E10)
# a = eval(input("Enter a number for the equation: "))
# print((-a) ** 2)


def safe_divide(numerator, denominator):
    if numerator is None or denominator is None:
        print("A required value is missing.")
    elif denominator == 0:
        print("The denominator is zero.")
    else:
        return numerator / denominator


print(safe_divide(10, 5))
