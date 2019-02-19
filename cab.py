print("*********welcome to cardrive*********")
while True:
            try:
                source= float(input("initial reading:\n"))
                if (source>=0):
                            des=float(input("Ending reading:\n"))
                            if des<source:
                              print("invalid")
                            else:
                          

                                    distance=des-source
                                    print("select vehicle type")
                                    print("    1.auto\n    2.micro\n    3.mini\n")
                                    type=int(input())

                                    if (type==1):
                                                print("your vehicle selected is auto\n")
                                                a=(10*distance)
                                                break
                                    elif (type==2):
                                                  print("your vehicle selected is micro\n")
                                                  b=(20*distance)
                                                  break
                                    elif(type==3): 
                                                  print("your vehicle selected is mini\n")
                                                  c=(30*distance)
                                                  break
                                    else:
                                                  print("choice is not found")
                           
                else:
                      print("invalid reading")
            except:
                    print("invalid")
                    break
print("-----------------Bill--------------------")
print("your travelled distance is:",distance)
if (type==1):
  print("Amount to be paid:$",a)
elif(type==2):
  print("Amount to be paid:$",b)
elif(type==3):
  print("Amount to be paid:$",c)
print("      ---welcome again---      ")
 
