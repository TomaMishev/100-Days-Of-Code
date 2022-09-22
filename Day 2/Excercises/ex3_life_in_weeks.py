# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age?")

current_age = int(age)

years_left = 90 - current_age

days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

output = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."

print(output)