from portfolio import PortfolioTracker
from asset import Asset

my_portfolio = PortfolioTracker() 

def display_option() -> None:
    print()
    print("----------------------------------------------")
    print()
    print("==============================================")
    print("       QUANT PORTFOLIO TRACKER v1.0")
    print("==============================================")
    print()

    total = my_portfolio.calculate_total_value()
    amount = my_portfolio.unr_absolute_amount()
    percentage = my_portfolio.unr_percentage()
   
    print(f"Total Portfolio Value: ${total:.2f}")
    if my_portfolio.unr_absolute_amount() >= 0: 
        print(f"Overall Profit/Loss: +${amount:.2f} (+{percentage:.2f}%)")
    else:
        n_percentage = -1 * my_portfolio.unr_percentage()
        n_amount = -1 * my_portfolio.unr_absolute_amount()
        print(f"Overall Profit/Loss: -${n_amount:.2f} (-{n_percentage:.2f}%)")

    print(
        """
        PLEASE SELECT AN OPTION BELOW TO PROCEED.
        1. ADD A NEW ASSET (BUY)
        2. UPDATE A MARKET PRICE
        3. SELL AN ASSET
        4. VIEW MY ENTIRE PORTFOLIO
        5. SAVE AND EXIT THE PROGRAM
        """)
  
def start() -> None:
    option = 0
    if my_portfolio.load_file():
        print("EXISTING PORTFOLIO FOUND. PROGRAM CONTINUATION...")
    else:
        print("NO EXISTING PORTFOLIO FOUND. STARTING AFRESH")
    while True:
        try:
            print("==============================================")
            display_option()
            option = int(input("I CHOOSE OPTION --- "))
            if option == 1:
                print("")
                print("---------------------------------------------")
                print("")
                try:
                    category = input("PLEASE ENTER THE CATEGORY OF THE SYMBOL YOU WISH TO BUY --- ")
                    symbol_name = input("PLEASE ENTER THE SYMBOL YOU WISH TO BUY --- ").strip()
                    buy_price = float(input("PLEASE ENTER THE PRICE OF THIS SYMBOL --- "))                     
                    quantity = float(input("PLEASE ENTER THE QUANTITY OF THIS SYMBOL YOU WISH TO BUY--- "))

                    if not category or not symbol_name:
                        continue
                    new_asset = Asset(symbol_name, buy_price, category, quantity)
                    my_portfolio.add_asset(new_asset)
                    print("")
                    print("==============================================")
                    success = "YOUR ASSET HAS BEEN BOUGHT SUCCESSFULLY. \nIT CAN BE VIEWED IN YOUR PORTFOLIO"
                    print(success)

                except ValueError:
                    print("ERROR: THE PRICE AND QUANTITY OF THE SYMBOL MUST BE NUMBERS. \nSYMBOL PURCHASE UNSUCCESFUL.")
                print("")

            elif option == 2:
                print("")
                print("---------------------------------------------")
                print("")
                try:
                    wanted_symbol = input("PLEASE ENTER THE SYMBOL YOU WISH TO UPDATE IT'S PRICE --- ").strip()
                    new_price = float(input("PLEASE ENTER THE NEW PRICE OF THIS SYMBOL --- "))
                    updated_asset = my_portfolio.update_asset_price(wanted_symbol,new_price)

                    if updated_asset == True:
                        print(f"THE PRICE OF {wanted_symbol} HAS BEEN UPDATED SUCCESSFULLY")
                    elif updated_asset == False:
                        print(f"{wanted_symbol} DOES NOT EXIST IN YOUR PORTFOLIO")

                except ValueError:
                    print("ERROR: PRICE MUST BE A NUMBER. \nPRICE CHANGE UNSUCCESSFUL.")
                print("")
                    

            elif option == 3:
                print("")
                print("---------------------------------------------")
                print("")
                sold_symbol = input("WHAT SYMBOL WOULD YOU LIKE TO SELL --- ").strip()
                check_sell = my_portfolio.sell_asset(sold_symbol)

                if check_sell == True:
                    print(f"{sold_symbol} HAS BEEN SOLD SUCCESSFULLY")
                elif check_sell == False:
                    print(f"{sold_symbol} HAS ALREADY BEEN SOLD OR DOES NOT EXIST IN YOUR PORTFOLIO")
                print("")

            elif option == 4:
                print("")
                print("---------------------------------------------")
                print("")
                print("USER'S PORTFOLIO")
                all_assets = my_portfolio.get_assets()
                if not all_assets:
                    print("\nUSER PORTFOLIO EMPTY")
                else:
                    for asset in all_assets:
                        print(asset)
                print("")

            elif option == 5:
                print()
                print("----------------------------------------------")
                print()
                if my_portfolio.save_file():
                    print("FILE SAVED SUCCESSFULLY. ENJOY THE REST OF YOUR DAY")
                    break
                else:
                    print("ERROR: FILE COULD NOT SAVE. RETURNING TO MENU...")
                    continue

            else:
                print()
                print("ERROR: PLEASE PICK A NUMBER BETWEEN 1 - 5.")
                

        except ValueError:
            print("ERROR: YOU MUST SELECT A NUMBER BETWEEN 1 TO 5")

if __name__ == "__main__":
    start()

   