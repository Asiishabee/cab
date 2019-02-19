def bill():
            print("--------------------------------------------------")
            print("-----------------Bill--------------------")
            print("Your travelled distance is:",distance)
            if (type==1):
              print("Amount to be paid:$",a)
            elif(type==2):
              print("Amount to be paid:$",b)
            elif(type==3):
              print("Amount to be paid:$",c)
            print("      ---Welcome Again---      ")
            print("--------------------------------------------------")







print("*********WELCOME TO CARDRIVE*********")
while True:
            try:
                source= float(input("initial reading:\n"))
                if (source>=0):
                                while True:
                                              try:
                                                    des=float(input("Ending reading:\n"))
                                                    if des<source:
                                                      print("invalid")
                                                    else:
                                                  

                                                            distance=des-source
                                                            while True:
                                                                          try:
                                                                                print("select vehicle type")
                                                                                print("    1.auto\n    2.micro\n    3.mini\n")
                                                                                type=int(input())

                                                                                if (type==1):
                                                                                            print("your vehicle selected is auto\n")
                                                                                            a=(10*distance)
                                                                                            bill()
                                                                                            break
                                                                                elif (type==2):
                                                                                              print("your vehicle selected is micro\n")
                                                                                              b=(20*distance)
                                                                                              bill()
                                                                                              break
                                                                                elif(type==3): 
                                                                                              print("your vehicle selected is mini\n")
                                                                                              c=(30*distance)
                                                                                              bill()
                                                                                              break
                                                                                else:
                                                                                              print("choice is not found")
                                                                          except:
                                                                                  break
                                              except:
                                                    break
                                                                  
                           
                else:
                      print("invalid reading")
            except:
                    print("invalid")
                    break

