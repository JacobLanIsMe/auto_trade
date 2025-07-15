class Candidate:
    def __init__(self, id: str, stockCode: str, companyName: str, isHolding: bool, techData: str, gapUpHigh: float = 0.0, gapUpLow: float = 0.0):
        self.id = id
        self.stockCode = stockCode
        self.companyName = companyName
        self.isHolding = isHolding
        self.gapUpHigh = float(gapUpHigh) if gapUpHigh is not None else 0.0
        self.gapUpLow = float(gapUpLow) if gapUpLow is not None else 0.0
        self.techData = techData
        
    def __repr__(self):
        return f"<Candidate id={self.id} stockCode={self.stockCode} companyName={self.companyName} isHolding={self.isHolding} gapUpHigh={self.gapUpHigh} gapUpLow={self.gapUpLow}>"
