class IndicatorEngine:

    def __init__(

        self,

        market_data,

        cache

    ):

        self.market = market_data

        self.cache = cache

    def update(

        self,

        symbol,

        timeframe

    ):

        candles = self.market.history(symbol)

        self.calculate_all(

            symbol,

            timeframe,

            candles

        )
