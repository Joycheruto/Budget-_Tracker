
#prompt the user for name
name = input("please enter your name:  ") 
print(f"Hello, {name}  😊")


# Ask user for their budget
while True:
    try:
        budget =float(input("Please enter your budget:  "))  # should be a number
        break
    except ValueError:
        print(" INVALID INPUT   ")   #show this error if not number entered
        print()
print("type done when you have completed...")
print()



#dictionary stores the expense items and their amount
item_amount = {}

#loops infinitely unless user types "done"
while True:
    item = input("Please enter your expense:  ")
    if item.lower() =="done":     #stop if user types done
        break
    if not item:                   #prevents an empty expense name
        print("Expense name cannot be empty!")
        continue

    # amount for the expense
    while True:
        try:
            amount = float(input("enter the amount: "))  # cost of the expense
            break
        except ValueError:
            print("INVALID INPUT  ")  #outputs this error message if user inputs anything else other  than a float


    item_amount[item] = amount   #saves the expense name  and the amount into a dictionary


#This function processes the budget ,calculate the total,balance,affordable expenses and creates a report


def budget_tracker(item_amount,budget):
   
    affordable=[]  #the list stores affordable expenses 

    print( )



    print("DESCRIPTION")
    for item,amount in item_amount.items():

        print(f"{item} : ksh{price: .2f}")  #print the expense details

        if amount<=budget:             #if amount of the expense is <= budget,it is affordable
            affordable.append(item)
            affordable.sort()###




   #calculates the total no of expenses,total spent and the balance
    total_of_expenses = len(item_amount.keys())
    total_amount = sum(item_amount.values())
    balance = budget - sum(item_amount.values())


    print("  ")#adds an empty line
    print("Total expenses: ",total_of_expenses)
    print(f"your total is:  ksh {total_amount :.2f}")   
    print(f"your balance is:  ksh {balance:.2f}")
    print( )



    #checks if the user is within budget or is overspending
    if balance < 0:
        print("⚠️  you are above your budget !")
    else:
        print("you are within the budget")


       
    print( )

    #saves the report to a text file
    try:
        with open("Report.txt","w") as file:     # i cna change the mode to append so as to have an history of users budget
            file.write(f"\n----BUDGET DATA FOR {name}----\n")
            file.write("\nDESCRIPTION")
            for item,price in item_amount.items():
                file.write(f"\n{item} : ksh {amount:.2f}")

            file.write(f"\nTotal expenses:  {total_of_expenses}\n")
            file.write(f"Your total is:  ksh {total_amount:.2f}\n")
            file.write(f"Your balance is:  ksh {balance:.2f}\n")
            if balance < 0:
                file.write(" you are above budget!\n")
            else:
                file.write("You are within the budget\n")

        print("Report saved successfully.")

    except OSError as e:
        print("could not save the report!!")
 

 
    print ("AFFORDABLE BILLS")                                                       
    return affordable
  
print(budget_tracker(item_amount,budget))   #calls the function











    

   
                    