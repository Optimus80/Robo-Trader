from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Candle:

    open_time: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float

    close_time: datetime

    quote_volume: float

    trades: int

    taker_buy_volume: float

    taker_buy_quote_volume: float
