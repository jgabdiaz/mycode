#!/usr/bin/env python3

""" This code will show you the names and crafts of the astronauts currently in space. In addition, it will randomly select one of the astronauts and display his/her name. The code will also show you the top 10 NASA most recently updated NASA projects and, upon request, will also return the titles and benefits of selected project Id's """

import requests
import random

#Begining of the main function
def main():

#Get API containing the number, names and crafts of astronauts currently in space
    response = requests.get("http://api.open-notify.org/astros.json")
    print ("")

#Print the number autronauts currently in space
    print ("Number of astronauts in space:" , response.json()["number"])

    print("")

#Print the names and crafts of each astronaut currently in space
    for EveryAstronaut in response.json()["people"]:
        print("{} is currently in {}".format(str(EveryAstronaut["name"]), str(EveryAstronaut["craft"])))

#Print a random astronaut name from the previous list   
    ListNames = []      
    for EveryDict in response.json()["people"]:
        ListNames.append(EveryDict["name"])
    print("")
    print("Random astronaut today is:")
    print(random.choice(ListNames))
    print("")

#Print a list of the top 10 most recently updated NASA projects    
    print("Top 10 resently updated  projects in NASA:")

#Get API that contains list of project Ids and the dates of their most recent updates     
    response2 = requests.get("https://api.nasa.gov/techport/api/projects?api_key=ts29aU98ySByQPEB1uwEhCRDUzBWRXLdQZoPEcp6")

#Print the top 10 most recently updated projects from the list    
    i=0
    index=0
    while i<10:
        print(response2.json()["projects"][index])
        i=i+1
        index=index+1

#Show tile and benefit of a selected project id from the previous list.        
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

