#hardcoded - aka database
food_name      = "Salad"
food_price     = 50.00
food_availabel = 10


#calculations
client_quantity = int(input ("How many ?")) # <<<<< User: enters data !!!

if client_quantity > 0 and client_quantity <= food_availabel :
    food_total_cost = food_price * client_quantity  
    # output
    print("total cost: ", food_total_cost)
else :   
    print("Wrong value for quantity!!!")

    # if EXPRESSION:
    #    code for True
    # else:
    #    code for False 

    #  if EXPRESSION1:
    #     code for True
    #  elif EXPRESSION2:    
    #      code for True on condtion2
    #  else:
    #    code for False     

    # inst1---> inst2---> ins ----> <EXPRETION ???>  /---> True ---> code for True
    #                                                /---> False ---> code for False
    

    