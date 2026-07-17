@dataclass(slots=True)
class MarketFeatures:

    symbol: str

    timeframe: str

    trend_score: float

    momentum_score: float

    volatility_score: float

    volume_score: float

    candle_score: float

    liquidity_score: float

    regime_score: float

    confidence: float

    data: dict
