# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

import math

# Write your code below this line 👇

output = ""


def prime_checker(number):
    prime_flag = 0
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                prime_flag = 1
                break

        if prime_flag == 0:
            output = "It's a prime number."
        else:

            output = "It's not a prime number."

    else:
        output = "It's not a prime number."

    print(output)


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

