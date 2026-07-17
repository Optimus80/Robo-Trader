from enum import Enum


class MarketRegime(Enum):

    STRONG_BULL = "strong_bull"

    BULL = "bull"

    SIDEWAYS = "sideways"

    BEAR = "bear"

    STRONG_BEAR = "strong_bear"

    HIGH_VOLATILITY = "high_volatility"

    LOW_VOLATILITY = "low_volatility"

    ACCUMULATION = "accumulation"

    DISTRIBUTION = "distribution"
