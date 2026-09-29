# PORTFOLIO ANALYTICS TRACKER
This is an object-oriented engine built in Python which allows a user view portfolio assets, track unrealized profit and loss values, buy and sell these assets, update asset prices and properties and save their session in a JSON file.
I built it to practice object-oriented programming, data persistence and learn how to track real-time data values.

![Python 3.14](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)

---

## Features
* Data Persistence -> Python's JSON module was used to save user sessions and allows users to return to their previous portfolio without deleting all their data.
* Input Validation -> All user inputs were validated using `try/except` blocks to prevent runtime crashes.
* Object-Oriented Style-> This program was built following object oriented programming rules to ensure the code was flexible and maintainable.

---

## Data Structures and Modules Used
* Lists -> Lists like `self.assets` and `saved` were used to store the user's assets for the current session or to save the assets in a JSON file.
* Dictionaries -> dictionaries like `saving_assets` were used to store the assets key-value pairs so they could be appended into the  `saved` list.
* Datetime -> the `datetime` module was used to track the amount of days an active asset was held in a portfolio.

---

## How to Run
### Prerequisites
* Python 3.14 or higher installed (python or python3)

### Run The Code
* Open your terminal and run the main script

``` bash
python main.py
```
---

## Sample Output
* When you run `python main.py`, this should come up on your terminal
``` text
NO EXISTING PORTFOLIO FOUND. STARTING AFRESH
==============================================

----------------------------------------------

==============================================
       QUANT PORTFOLIO TRACKER v1.0
==============================================

Total Portfolio Value: $5526.90
Overall Profit/Loss: +$440.00 (+8.65%)

        PLEASE SELECT AN OPTION BELOW TO PROCEED.
        1. ADD A NEW ASSET (BUY)
        2. UPDATE A MARKET PRICE
        3. SELL AN ASSET
        4. VIEW MY ENTIRE PORTFOLIO
        5. SAVE AND EXIT THE PROGRAM
        
I CHOOSE OPTION --- 4

---------------------------------------------

USER'S PORTFOLIO
[Active] : XAU/USD (FOREX): 2.0 units at $203.45 on 29-09-2026 |
          Currently now at 203.45| Current Total: 406.90| Return: 0.00% | Days held: 0
[Active] : MSFT (STOCK): 200.0 units at $23.40 on 29-09-2026 |
          Currently now at 25.60| Current Total: 5120.00| Return: 9.40% | Days held: 0
[Sold] : TSLA (STOCK): 4.0 units at $301.40 on 29-09-2026 |
          Currently now at 299.40| Current Total: 1197.60| Return: -0.66% | Days held: 0

==============================================

----------------------------------------------

==============================================
       QUANT PORTFOLIO TRACKER v1.0
==============================================

Total Portfolio Value: $5526.90
Overall Profit/Loss: +$440.00 (+8.65%)

        PLEASE SELECT AN OPTION BELOW TO PROCEED.
        1. ADD A NEW ASSET (BUY)
        2. UPDATE A MARKET PRICE
        3. SELL AN ASSET
        4. VIEW MY ENTIRE PORTFOLIO
        5. SAVE AND EXIT THE PROGRAM
        
I CHOOSE OPTION --- 

```

## Planned Improvements
* Live API Integration -> I plan on connecting the app to a free API (Like Alpha Vantage) so market prices update automatically instead of the user having to type them in manually.
* Database Integration -> I would like to upgrade the data storage from JSON files to an SQL database (e.g SQLite) for faster querying and improving the functionality of data persistence.
* Realized Profit and Loss Tracking -> I plan on adding realized profit and loss and current cash balance after an asset has been sold to the code's logic.

