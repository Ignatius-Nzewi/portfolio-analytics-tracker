from asset import Asset
from datetime import datetime
import json



class PortfolioTracker:
    def __init__(self) -> None:
        self.assets: list [Asset] = []

    def add_asset(self, asset: Asset) -> None:
        self.assets.append(asset)

    def calculate_total_value(self) -> float:
        total_value = 0.00
        for asset in self.assets:
            if asset.status == "Active":
                asset_value = asset.get_current_value()
                total_value += asset_value

        return total_value

    def update_asset_price(self, updated_symbol: str, new_price: float) -> bool:
        for asset in self.assets:
            if updated_symbol.upper() == asset.symbol.upper():
                asset.update_price(new_price)
                return True
            
        return False
                
    def get_assets(self) -> list[Asset]:
        return self.assets


    def sell_asset(self, sold_symbol: str) -> bool:
    
        for asset in self.assets:
            if asset.status == "Active":
                if sold_symbol.upper() == asset.symbol.upper():
                    asset.status = "Sold"
                    
                    return True

        return False

    def unr_absolute_amount(self) -> float:
        total = 0.0
        for asset in self.assets:
            if asset.status == "Active":
                total += asset.get_profit()
        return total

    def unr_buy_price(self) -> float:
        total = 0.0
        for asset in self.assets:
            if asset.status == "Active":
                total += (asset.buy_price * asset.quantity)
        return total

    def unr_percentage(self) -> float:
        percentage = 0.0
        if self.unr_buy_price() == 0:
            return 0.0
        percentage += ((self.unr_absolute_amount()/self.unr_buy_price()) * 100)
        return percentage

    def save_file(self) -> bool:
        try: 
            saved = []
            for asset in self.assets:

                saving_assets = {
                    "symbol" :  asset.symbol,
                    "buy_price" : asset.buy_price,
                    "category" : asset.category,
                    "quantity" : asset.quantity,
                    "status" : asset.status,
                    "current_price" : asset.current_price,
                    "buy_date" : asset.buy_date.isoformat()
                }
                saved.append(saving_assets)

            with open ("portfolio.json", "w") as file:
                json.dump(saved, file, indent=4)
            return True
        except Exception:
            return False

    def load_file(self) -> bool:
        try:
            with open ("portfolio.json", "r") as file:
                loaded_data = json.load(file)

                for data in loaded_data:
                    restored_data = Asset(
                        symbol = data["symbol"],
                        buy_price = data["buy_price"],
                        category = data["category"],
                        quantity = data["quantity"],
                    )

                    restored_data.status = data["status"]
                    restored_data.current_price = data["current_price"]
                    restored_data.buy_date = datetime.fromisoformat(data["buy_date"])

                    self.assets.append(restored_data)
                return True
            
        except FileNotFoundError:
            return False
        