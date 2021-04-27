"""
Objective: Make the following output using the following list:

1.Include this list:
icecream= ["flavors", "salty"] 



2.Append the integer (not string!) 99 to icecream.


3.Include an input asking for the user's name.


4.Using the appended list and the input, make this output (emphasis placed):
<99> <flavors>, and <name> chooses to be <salty>.

"""

#!/usr/bin/env python3
icecream= ["flavors", "salty"]
icecream.append(99)
print("what is you user name?")
userName = input()

print (icecream[-1],icecream[0],"and",userName,"chooses to be",icecream[1])

print (f"{icecream[-1]} {icecream[0]} and {userName} chooses to be {icecream[1]}")

        

