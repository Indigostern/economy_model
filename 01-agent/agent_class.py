class Agent:
    assets = 0
    debt = 0

    def __init__(self, assets, debt):
        self.assets = assets
        self.debt = debt
        
    def __str__(self) -> str:
        return f"assets: {self.assets}, debt: {self.debt}"