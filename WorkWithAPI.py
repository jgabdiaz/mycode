#!/usr/bin/env python3
import requests
import random

def main():
    response = requests.get("http://api.open-notify.org/astros.json")
   # print(response.status_code)
   # print(dir(response))
   # print(response.json())
    print ("")
    print ("Number of astronauts in space:" , response.json()["number"])

    print("")

    for EveryAstronaut in response.json()["people"]:

        print("{} is currently in {}".format(str(EveryAstronaut["name"]), str(EveryAstronaut["craft"])))

    ListNames = []      
    for EveryDict in response.json()["people"]:
        ListNames.append(EveryDict["name"])

    print("")
    print("Random Astronaut today is:")
    print(random.choice(ListNames))    



main()

