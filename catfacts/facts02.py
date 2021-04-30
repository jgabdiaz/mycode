#!/usr/bin/env python3
import requests

def main():
    response = requests.get("http://api.open-notify.org/astros.json")
   # print(response.status_code)
   # print(dir(response))
   # print(response.json())
    print ("")
    print ("Number of astronauts in space:" , response.json()["number"])

    print("")

    for EveryAstronaut in response.json()["people"]:
       # print(f"{str(EveryAstronaut["name"])} is currently in {str(EveryAstronaut["craft"])}")

        print("{} is currently in {}".format(str(EveryAstronaut["name"]), str(EveryAstronaut["craft"])))

    print("")
main()

