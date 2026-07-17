class Application:

    def __init__(self):

self.container.register("market_data",MarketData())

self.container.register("strategy",StrategyEngine())

self.container.register("risk",RiskManager())

self.container.register("execution",ExecutionEngine())

    def initialize(self):

        from core.event_bus import EventBus

        from core.bot_state import BotState

        from core.dependency_container import Container

        try: self.container = Container()

except Exception as e: logger.error(e) shutdown()

        self.event_bus = EventBus()

        self.state = BotState()

        self.container.register("event_bus", self.event_bus)

        self.container.register("state", self.state)

       logger.info("Quant Bot V2 Initialized")
