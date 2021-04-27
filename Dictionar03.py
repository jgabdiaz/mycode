#!/usr/bin/env python3

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }
i='yes'

while i=='yes':

    print("Which character do you want to know about?: (Wolverine, Harry Potter, Captain America)")
    charname = input()

    print("What statistic do you want to know about? (real name, powers, archenemy)")
    charstat= input()

    print(f"{charname}'s {charstat} is: {heroes[charname][charstat]}")

    print ("Do you want to do it again:(yes no)")

    i= input()


