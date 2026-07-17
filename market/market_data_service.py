class MarketDataService:

    def __init__(self,

                 exchange,

                 candle_cache):

        self.exchange = exchange

        self.cache = candle_cache

    def bootstrap(self,

                  symbol,

                  timeframe,

                  limit):

        candles = self.exchange.get_klines(

            symbol,

            timeframe,

            limit

        )

        for candle in candles:

            self.cache.update(symbol, candle)

    def latest(self,

               symbol):

        return self.cache.latest(symbol)

    def history(self,

                symbol):

        return self.cache.get(symbol)
