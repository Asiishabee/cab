print("welcome to cardrive")
while True:
            try:
                source= float(input("initial reading:\n"))
                if (source>=0):
                            des=float(input("Ending reading:\n"))
                            if(des<source):
                          

                                distance=des-source
                                print("select vehicle type")
                                print("1.auto\n 2.micro\n 3.mini")
                                type=int(input())

                                if (type==1):
                                            print("your vehicle selected is auto")
                                            a=(10*distance)
                                            break
                                            
                                            
                                elif (type==2):
                                              print("your vehicle selected is micro")
                                              b=(20*distance)
                                              break
                                              
                                              
                                elif(type==3): 
                                              print("your vehicle selected is mini")
                                              c=(30*distance)
                                              break
                                            
                                else:
                                              print("choice is not found")
                            else:
                                print("invalid")
                                
                else:
                      print("invalid") 
                                  

            except:
                    print("invalid")
                    break
print("------------Bill--------------- ")
print("your travelled distance is",distance)
print("bill no:")

  
if (type==1):
  print("$",a)
elif(type==2):
  print("$",b)
elif(type==3):
  print("$",c)
print("      ---welcome again---      ")


