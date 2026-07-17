class Application:

    def __init__(self):

        self.container = None

        self.event_bus = None

        self.state = None

    def initialize(self):

        from core.event_bus import EventBus

        from core.bot_state import BotState

        from core.dependency_container import Container

        self.container = Container()

        self.event_bus = EventBus()

        self.state = BotState()

        self.container.register("event_bus", self.event_bus)

        self.container.register("state", self.state)

        print("Quant Bot V2 Initialized")
