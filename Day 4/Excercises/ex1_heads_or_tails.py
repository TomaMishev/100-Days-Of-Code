# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised

import random

random_num = random.randint(0, 1)
if random_num == 1:
    print("Heads")
else:
    print("Tails")
