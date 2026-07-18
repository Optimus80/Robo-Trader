@dataclass(slots=True)
class Signal:

    symbol: str

    timeframe: str

    direction: SignalDirection

    confidence: float

    score: float

    entry_price: float

    stop_loss: float

    take_profit: float

    risk_reward: float

    reasons: list[str]

    metadata: dict
