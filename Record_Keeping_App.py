

while True:
    print("\n================================")
    print("[a] = ADD RECORDS \n[b] = VIEW RECORDS \n[c] = CLEAR ALL RECORDS \n[d] = EXIT")

    choice = input("Enter Choice: ")

    if choice == 'a' or choice == 'A':
        add_name = input("\nEnter Name: ")
        add_email = input("Enter Email: ")
        add_address = input("Enter Address: ")
        f = open("Record.txt", "a")
        f.write("\n\nName: "+add_name+"\nEmail: "+add_email+"\nAddress: "+add_address)
        f.close()
        print("\nAdding Record Success!!")

    elif choice == 'b' or choice == 'B':
        f = open("Record.txt", "r")
        print(f.read())
            


    elif choice == 'c' or choice == 'C':
        while True:
            choice=input("Are you sure to clear record?: [y/n]")
            if choice == 'y' or choice == 'Y':
                f = open("Record.txt", "w")
                f.write("")
                print("\nClearing Text File....")  
                print("\nNo Record Found")  
                break
            elif choice == 'n' or choice == 'N':
                print("Record Clearing Cancel.")
                break
            else:
                print("\nWrong Choice Try Again!") 

    elif choice == 'd' or choice == 'D':
        print("\nThank You!")
        break  

    else:
        print("\nWrong Choice Try Again!") 





