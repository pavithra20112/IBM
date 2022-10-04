loopy =1
print("Traffic light simulation programme system")
while true:  #This simulates a loop
    if loopy ==1:
         print("Input signal to run program 1")
         print("Input red for : STOP")
         print ("Input yellow for:READY TO STOP")
         print ("Input green for: GO")
         print ("Input stop for: END PROGRAMME")
         print ("-----------------------------")
    else:
         print ("Input signal to run program :")
         print ("-----------------------------")
    signal = input()
    if signal =="red":
        print("colour = RED")
        print("stop behind the line")
        print("Next 60 seconds")
        print ("-----------------------------")
    else:
     if signal =="yellow":
        print("colour =YELLOW")
        print("stop behind the line")
        print("Next 60 seconds")
        print ("-----------------------------")
    else:
     if signal =="green":
        print("colour = GREEN")
        print("stop behind the line")
        print("Next 60 seconds")
        print ("-----------------------------")
   else:
      if signal =="stop":
        print("you choose to end this programme.")
        print ("-----------------------------")
    else:
        print ("please insert the right signals(red,yellow,green& stop) only.")
        print ("-------------------------------------------------------------")
 loopy=2
 if not(signal!="stop"): break #Exit loop
 print("End Simulation programme")
            
         
            
         
           
         
