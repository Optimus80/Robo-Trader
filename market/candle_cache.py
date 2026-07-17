from collections import deque

from market.candle import Candle


class CandleCache:

    def __init__(self, max_size=2000):

        self.cache = {}

        self.max_size = max_size

    def update(self, symbol, candle: Candle):

        if symbol not in self.cache:

            self.cache[symbol] = deque(maxlen=self.max_size)

        self.cache[symbol].append(candle)

    def get(self, symbol):

        return list(self.cache.get(symbol, []))

    def latest(self, symbol):

        candles = self.cache.get(symbol)

        if candles:

            return candles[-1]

        return None
