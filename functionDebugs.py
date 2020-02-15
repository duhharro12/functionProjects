#1)
# This function should take in three numbers and multiply them together
# Does not do desired function:
# def multiply_three_numbers(num1, num2):
#    productOfThreeNumbers = num1 * num2
#    return productOfThreeNumbers
# Correct:
def multiply_three_numbers(num1,num2,num3):
    productOfThreeNumbers = num1 * num2 * num3
    return productOfThreeNumbers
#2)
# This function has the wrong naming conventions:
# def Multiply by Two(num1):
#    multiplied = num1 * 2
#    return multiplied
# Correct:
def multiply_by_two(num1):
    multiplication = num1*2
    return multiplication
#3)
# This function uses one more line than necessary, make it do the same function
# but in one line
# def divide_by_ten(num):
#    divided = num / 10
#    return divided
def divide_by_ten(num1):
    division_by_ten= (num1/10)
    return division_by_ten