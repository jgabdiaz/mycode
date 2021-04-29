#!usr/bin/env python3                                                                                                                                                                                                          
def main():
    MyJson = {"name":{"birth":"Cassius Clay","current":"Muhammad Ali"},"contact":{"phone":"333-444-5555","email":"thebest@boxing.com"},"favorites":{"number":56,"food":{"baked chicken":3.5,"mac and cheese":4.5,"spinach":2,"green peas":2},"drink":{"adult":["none"],"nonadult":["Mr. Champ soda"]}}}                                         
    print ("Muhammad Ali's favorite food list: ")
    for Each_Dic in MyJson ["favorites"]["food"]:                                                             
        print (Each_Dic)

    
    print ("Muhammad Ali's phone number is:" + MyJson["contact"]["phone"] + " and his email address is: " + MyJson["contact"]["email"] )

    print("The total cost of Muhammad Ali's food is")
   
   
    Each_Dic2 =  MyJson ["favorites"]["food"]
      
    Cost = float( Each_Dic2["baked chicken"]) + float(Each_Dic2["mac and cheese"]) + float( Each_Dic2["spinach"]) + float(Each_Dic2["green peas"]) 
    print(Cost)

    Wins =int(MyJson["favorites"]["number"])
     
    for n in range(Wins):
        print (MyJson["favorites"]["drink"]["nonadult"])
    

                
main()        




