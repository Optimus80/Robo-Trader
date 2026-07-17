class IndicatorCache:

    def __init__(self):

        self.data = {}

    def store(

        self,

        symbol,

        timeframe,

        indicator,

        value

    ):

        key = (symbol, timeframe, indicator)

        self.data[key] = value

    def get(

        self,

        symbol,

        timeframe,

        indicator

    ):

        return self.data.get(

            (symbol, timeframe, indicator)

        )
