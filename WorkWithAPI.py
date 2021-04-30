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
    print("")

    print("Top 10 resently updated  projects in NASA:")


    response2 = requests.get("https://api.nasa.gov/techport/api/projects?api_key=ts29aU98ySByQPEB1uwEhCRDUzBWRXLdQZoPEcp6")

    i=0
    index=0
    while i<10:
        print(response2.json()["projects"][index])
        i=i+1
        index=index+1
    
    print("")

    print("Do you want to  get information about any of these projects? (Y/N) ")
    
    proceed = input()

    while proceed.upper()=="Y":

        print("Enter the projectId you want information about: ")
        prjId = input()
       
        JsonStr = "https://api.nasa.gov/techport/api/projects/" + prjId + "?api_key=ts29aU98ySByQPEB1uwEhCRDUzBWRXLdQZoPEcp6"

        response3 = requests.get(JsonStr)       

        print("Project Title: ")

        print (response3.json()["project"]["title"])
        

        print("")
        print("Project Benefits: ")
        print (response3.json()["project"]["benefits"])
        print("")
        print("Do you want to see information about any other project?")
        proceed = input(">>>")


main()

