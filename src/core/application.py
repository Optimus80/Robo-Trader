from src.core.dependency_container import Container
from src.core.event_bus import EventBus
from src.core.bot_state import BotState

from common.logger import logger


class Application:

    def __init__(self):

        self.container = Container()
        self.event_bus = EventBus()
        self.state = BotState()

    def register_services(self):

        self.container.register("event_bus", self.event_bus)
        self.container.register("state", self.state)

    def initialize(self):

        logger.info("Inicializando Quant Bot...")

        self.register_services()

        logger.info("Serviços registrados.")

    def run(self):

        self.initialize()

        logger.info("Bot iniciado.")
