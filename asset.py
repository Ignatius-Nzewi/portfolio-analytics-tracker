from datetime import datetime
class Asset:

    def __init__ (self, symbol: str, buy_price: float, category: str, quantity:float):
        self.symbol = symbol
        self.buy_price = buy_price
        self.category = category
        self.quantity = quantity
        self.buy_date: datetime = datetime.now()
        self.current_price: float = buy_price
        self.status: str = "Active"

    def update_price(self, new_price: float) -> None:
        self.current_price = new_price

    def get_current_value(self) -> float:
        value = self.current_price * self.quantity
        return value

    def get_percentage_return(self) -> float:
        if self.buy_price*self.quantity == 0:
            return 0.00
        percentage = (((self.get_profit())/ (self.buy_price*self.quantity)) * 100)
        return percentage

    def get_profit(self) -> float:
        profit = (self.current_price - self.buy_price)* self.quantity
        return profit

    def get_days_held(self) -> int:
        time_difference = datetime.now() - self.buy_date 
        number_days = time_difference.days
        return number_days

    def __str__(self) -> str:
        return f"[{self.status}] : {self.symbol} ({self.category}): {self.quantity} units at ${self.buy_price:.2f} on {self.buy_date.strftime("%d-%m-%Y")} |\n          Currently now at {self.current_price:.2f}| Current Total: {self.get_current_value():.2f}| Return: {self.get_percentage_return():.2f}% | Days held: {self.get_days_held()}"