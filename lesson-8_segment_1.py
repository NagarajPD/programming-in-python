myfile = open(r"C:\Users\Toshiba\Desktop\python genesis\customer.txt", "a")
myfile.write(input("enter your name"))
myfile.write("\n")
myfile.write(input("enter your city"))
myfile.write("\n")
myfile.write(input("enter your subject"))
myfile.close()



myfile = open(r"C:\Users\Toshiba\Desktop\python genesis\customer.txt", "r")
data=myfile.readlines()
for item in data:
    print(item)

