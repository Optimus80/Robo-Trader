from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class PositionState:

    symbol: str

    quantity: float

    average_price: float

    stop_loss: float | None = None

    trailing_stop: float | None = None

    take_profit: float | None = None

    opened_at: str | None = None


@dataclass
class BotState:

    balance: float = 0

    equity: float = 0

    drawdown: float = 0

    positions: Dict[str, PositionState] = field(default_factory=dict)

    indicators: Dict[str, Any] = field(default_factory=dict)

    market_regime: Dict[str, str] = field(default_factory=dict)

    statistics: Dict[str, Any] = field(default_factory=dict)

    cache: Dict[str, Any] = field(default_factory=dict)
