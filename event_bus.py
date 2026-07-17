from collections import defaultdict
from typing import Callable, Dict, List, Any
import threading


class EventBus:
    """
    Event Bus Thread-Safe

    Responsável pela comunicação entre módulos.
    """

    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = defaultdict(list)
        self._lock = threading.Lock()

    def subscribe(self, event_name: str, callback: Callable):

        with self._lock:
            self._listeners[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable):

        with self._lock:

            if callback in self._listeners[event_name]:
                self._listeners[event_name].remove(callback)

    def publish(self, event_name: str, **kwargs):

        listeners = list(self._listeners.get(event_name, []))

        for callback in listeners:

            try:
                callback(**kwargs)

            except Exception as e:

                print(f"[EVENT ERROR] {event_name}: {e}")
