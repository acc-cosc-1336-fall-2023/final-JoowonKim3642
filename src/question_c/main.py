#Q3 main

import question_c

def main():
     
    while True:

        print("MENU\n1-Display stock purchase history\n2-Exit")
        option = int(input("Select 1 or 2: "))

        if option == 1:
            question_c.stock_purchase_history()
             
        elif option == 2:
            print("Exit")
            break
            
        else:
            print("Invalid choice. Select 1 or 2")

main()