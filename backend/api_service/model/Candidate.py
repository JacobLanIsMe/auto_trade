class Candidate:
    def __init__(self, id: str, stockCode: str, companyName: str, isHolding: bool):
        self.id = id
        self.stockCode = stockCode
        self.companyName = companyName
        self.isHolding = isHolding

    def __repr__(self):
        return f"<Candidate id={self.id} stockCode={self.stockCode} companyName={self.companyName} isHolding={self.isHolding}>"
