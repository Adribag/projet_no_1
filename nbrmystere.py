def nbrMyst():
    import random
    import variables as var
    
    response = -1

    def checkLose(countResponse,tryResponse):
        if(tryResponse == 5):
            print("Tu as perdu ! ")
            nbrMyst1 == response
            print(nbrMyst1)
            countResponse = 4    
            print(countResponse)  
        else:       
            print(f"Il te reste {5 - tryResponse} essais")
            takeResponse

    startNbrMyst = input("Veux tu jouer au nombre mystere O -> oui N -> non : ").upper()
    countResponse = 0
    while startNbrMyst == "O":

        while countResponse < 3:

            tryResponse = 0

            nbrMyst1 = random.randint(0,100)
            nbrMyst2 = random.randint(0,100)
            nbrMyst3 = random.randint(0,100)
            print(nbrMyst1)
            print(nbrMyst2)
            print(nbrMyst3)

            while nbrMyst1 != response:
            
                takeResponse = int(input("Trouve le premier nombre : "))

                if(nbrMyst1 == takeResponse):
                    print("Bravo tu as trouvé le premier nombre")
                    countResponse += 1
                    nbrMyst1 = response
                    break
                elif(nbrMyst1 > takeResponse):
                    print("Le nombre est plus grand")   
                    tryResponse += 1        
                    if(tryResponse == 5):
                        print("Tu as perdu ! ")
                        nbrMyst1 == response
                        print(nbrMyst1)
                        countResponse = 4    
                        print(countResponse)
                        break 
                    else:       
                        print(f"Il te reste {5 - tryResponse} essais")
                        takeResponse
                    
                elif(nbrMyst1 < takeResponse):
                    print("Le nombre est plus petit")
                    tryResponse += 1
                    if(tryResponse == 5):
                        print("Tu as perdu ! ")
                        nbrMyst1 == response
                        print(nbrMyst1)
                        countResponse = 4    
                        print(countResponse) 
                        break 
                    else:       
                        print(f"Il te reste {5 - tryResponse} essais")
                        takeResponse
            if(nbrMyst1 != response):
                print("Tu as perdu le jeu du nombre mystere")
                break  


            while nbrMyst2 != response:
            
                takeResponse = int(input("Trouve le deuxieme nombre : "))

                if(nbrMyst2 == takeResponse):
                    print("Bravo tu as trouvé le deuxieme nombre")
                    countResponse += 1
                    nbrMyst2 = response
                    break
                elif(nbrMyst2 > takeResponse):
                    print("Le nombre est plus grand")   
                    tryResponse += 1        
                    if(tryResponse == 5):
                        print("Tu as perdu ! ")
                        nbrMyst2 == response
                        print(nbrMyst2)
                        countResponse = 4    
                        print(countResponse)
                        break 
                    else:       
                        print(f"Il te reste {5 - tryResponse} essais")
                        takeResponse
                    
                elif(nbrMyst2 < takeResponse):
                    print("Le nombre est plus petit")
                    tryResponse += 1
                    if(tryResponse == 5):
                        print("Tu as perdu ! ")
                        nbrMyst2 == response
                        print(nbrMyst2)
                        countResponse = 4    
                        print(countResponse) 
                        break 
                    else:       
                        print(f"Il te reste {5 - tryResponse} essais")
                        takeResponse
            if(nbrMyst2 != response):
                print("Tu as perdu le jeu du nombre mystere")
                break

            while nbrMyst3 != response:
            
                takeResponse = int(input("Trouve le troisieme nombre : "))

                if(nbrMyst3 == takeResponse):
                    print("Bravo tu as trouvé le troisieme nombre")
                    countResponse += 1
                    nbrMyst3 = response
                    break
                elif(nbrMyst3 > takeResponse):
                    print("Le nombre est plus grand")   
                    tryResponse += 1        
                    if(tryResponse == 5):
                        print("Tu as perdu ! ")
                        nbrMyst3 == response
                        print(nbrMyst3)
                        countResponse = 4    
                        print(countResponse)
                        break 
                    else:       
                        print(f"Il te reste {5 - tryResponse} essais")
                        takeResponse
                    
                elif(nbrMyst3 < takeResponse):
                    print("Le nombre est plus petit")
                    tryResponse += 1
                    if(tryResponse == 5):
                        print("Tu as perdu ! ")
                        nbrMyst3 == response
                        print(nbrMyst3)
                        countResponse = 4    
                        print(countResponse) 
                        break 
                    else:       
                        print(f"Il te reste {5 - tryResponse} essais")
                        takeResponse
            if(nbrMyst3 != response):
                print("Tu as perdu le jeu du nombre mystere")
                break

            print("Tu as gagné le premier défi !")
            var.keyOne = True
            
        startNbrMyst = input("Veux tu rejouer au nombre mystere O -> oui N -> non : ").upper()
        if(startNbrMyst == "O"):
            countResponse = 0

nbrMyst()