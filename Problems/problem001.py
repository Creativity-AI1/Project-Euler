# Multiples of 3 or 5
# if we list all natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
def sum_of_multiples(limit):
    sum = 0
    for number in range(limit):
        if number % 3 or number % 5 == 0:
            sum+= number
    return sum
result= sum_of_multiples(1000)
print("sum of all multiples of 3 and 5 below 1000 is", result)
