#sep parameter
print(3,6,7,8,9) #prints the numbers with " "
print(3,6,7,8,9,sep = "/") #prints the numbers with sep value
print("A","B","c",sep = "\n")

#* parameter
print(*"Python") #seperates with " "
print(*"Python",sep = '+') #seperates with sep value
print(*"28383929",sep = '/')

#format fonk
print("{} {} {}".format("Z","E","Y"))
print("{1} {0} {2}".format(4,"Zeynep",1))
print("{:.2f} {:.2f} {:.3f}".format(4.2366,5592.322,98.665))