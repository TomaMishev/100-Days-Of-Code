# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
#
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}"
# to format the 3 lists to be printed as a 3 by 3 square, each on a new line.

# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# Now it looks a bit more like the coordinates of a real map:
# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit is the vertical location and the second digit is the horizontal location.
# So an input of 23 should place an X at the position shown below:
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "x".
# Remember that your nested list map actually looks like this:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

first_index = int(position[0])
second_index = int(position[1])

treasure_map[second_index - 1][first_index - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
