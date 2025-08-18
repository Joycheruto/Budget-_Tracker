
#prompt the user for name
name = input("please enter your name:  ") 
print(f"Hello, {name}  😊")

while True:
    try:
        budget =float(input("Please enter your budget:  "))
        break
    except ValueError:
        print(" INVALID INPUT   ")
        print()
print("type done when you have completed..,")
print()

item_prices = {}

while True:
    item = input("Please enter your expense:  ")
    if item.lower() =="done":
        break
    if not item:
        print("Expense name cannot be empty!")
        continue
    while True:
        try:
            price = float(input("enter the amount: "))
            break
        except ValueError:
            print("INVALID INPUT  ")
    item_prices[item] = price













def budget_tracker(item_prices,budget):
   
    affordable=[]

    print( )

    # if not item_prices:
    #     print("You have not entered expenses...")
    #     return []
    

    print("DESCRIPTION")
    for item,price in item_prices.items():

        print(f"{item} : ksh{price: .2f}")

        if price<=budget:
            affordable.append(item)
            affordable.sort()###




    
    total_of_expenses = len(item_prices.keys())
    total_amount = sum(item_prices.values())
     
    balance = budget - sum(item_prices.values())
    print("  ")#adds an empty line
    print("Total expenses: ",total_of_expenses)
    print(f"your total is:  ksh {total_amount :.2f}")   
    print(f"your balance is:  ksh {balance:.2f}")
    print( )




    if balance < 0:
        print("⚠️  you are above your budget !")
    else:
        print("you are within the budget")


       
    print( )
    try:
        with open("Report.txt","w") as file:
            file.write(f"\n----BUDGET DATA FOR {name}----\n")
            file.write("\nDESCRIPTION")
            for item,price in item_prices.items():
                file.write(f"\n{item} : ksh {price:.2f}")

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
    finally:
        print("Process finished .")

 
    print ("AFFORDABLE BILLS")
    # print (affordable)

                                                           
    return affordable
  
print(budget_tracker(item_prices,budget))
# affordable = budget_tracker(item_prices,budget)
# affordable, item_prices = pay_bills(item_prices,affordable)






# def pay_bills(item_prices,affordable):

#     while True:
#         paid_bill = input("Enter the paid bill  ")

#         # if paid_bill == "done":
#         #     break
#         if paid_bill in affordable:
#             affordable.remove(paid_bill)
#             item_prices.pop(paid_bill,None)
#         else:
#             print("item not found in the affordable list")

#         return affordable,item_prices











    

   
                    