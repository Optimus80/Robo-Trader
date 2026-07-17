class QuantBotException(Exception):
    """Base Exception"""


class ConfigurationException(QuantBotException):
    pass


class BinanceConnectionException(QuantBotException):
    pass


class StrategyException(QuantBotException):
    pass


class RiskException(QuantBotException):
    pass


class BacktestException(QuantBotException):
    pass
