class IndicatorEngine:

    def __init__(self):
        self.providers = {}

    def register(self, name, provider):
        self.providers[name] = provider

    def calculate(self, candles):

        result = {}

        for name, provider in self.providers.items():
            result[name] = provider.calculate(candles)

        return result
