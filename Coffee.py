from datetime import datetime

customerName = str(input("What is your name?: "))

price = 10
userInput = input("Would you like to tip? (Y/N): ")
if userInput == "Y":
    tipAmount = int(input("1. 10%\n2. 15%\n3. 20%\n4. Custom\n5. Back...\nPlease select a following option: "))
    if tipAmount == 1:
        print("$",price * 0.10)
    elif tipAmount == 2:
        print("$",price * 0.15)
    elif tipAmount == 3:
        print("$",price * 0.20)
    elif tipAmount == 4:
        tipCustom = int(input("What percent would you like to tip?: "))
        print("$",tipCustom/10)
    #else:
        #GO BACK TO Y/N PAGE
else:
    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y Time %H:%M:%S")
    print("\nCayden's F'ing Coffee\nOrder #0069 For", customerName)
    print(current_time)
    print("------------------------------------\nQTY  ITEM                        AMT\n------------------------------------")
    