#Q2 main

import question_b

def main():
    while True:
        print("MENU\n1-Display stock purchase history\n2-Exit")
        option = int(input("Select 1 or 2: "))

        if option == 1:
            stock_list = question_b.get_stock_list()

            for stock in stock_list:
                print(stock.get_symbol() + " " + stock.get_company_name())

        elif option == 2:
            print("Exit")
            break
            
        else:
            print("Invalid choice. Select 1 or 2")

main()