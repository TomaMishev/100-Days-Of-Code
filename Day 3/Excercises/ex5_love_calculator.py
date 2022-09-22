# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_to_lowercase = name1.lower()
name2_to_lowercase = name2.lower()

name1_t_occurs = name1_to_lowercase.count('t')
name2_t_occurs = name2_to_lowercase.count('t')

name1_r_occurs = name1_to_lowercase.count('r')
name2_r_occurs = name2_to_lowercase.count('r')

name1_u_occurs = name1_to_lowercase.count('u')
name2_u_occurs = name2_to_lowercase.count('u')

name1_e_occurs = name1_to_lowercase.count('e')
name2_e_occurs = name2_to_lowercase.count('e')

total_true = name1_t_occurs + name2_t_occurs + name1_r_occurs + name2_r_occurs + name1_u_occurs + name2_u_occurs\
             + name1_e_occurs + name2_e_occurs

name1_l_occurs = name1_to_lowercase.count('l')
name2_l_occurs = name2_to_lowercase.count('l')

name1_o_occurs = name1_to_lowercase.count('o')
name2_o_occurs = name2_to_lowercase.count('o')

name1_v_occurs = name1_to_lowercase.count('v')
name2_v_occurs = name2_to_lowercase.count('v')

name1_e_occurs = name1_to_lowercase.count('e')
name2_e_occurs = name2_to_lowercase.count('e')

total_love = name1_l_occurs + name2_l_occurs + name1_o_occurs + name2_o_occurs + name1_v_occurs + name2_v_occurs\
             + name1_e_occurs + name2_e_occurs

total_love = total_true * 10 + total_love

if total_love < 10 or total_love > 90:
    print(f"Your score is {total_love}, you go together like coke and mentos.")
elif 40 <= total_love <= 50:
    print(f"Your score is {total_love}, you are alright together.")
else:
    print(f"Your score is {total_love}.")