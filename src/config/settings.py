from dataclasses import dataclass
from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parents[2]


@dataclass
class Settings:
    exchange: dict
    risk: dict
    strategy: dict


def load_settings() -> Settings:

    with open(BASE_DIR / "config" / "exchange.yaml", "r") as f:
        exchange = yaml.safe_load(f)

    with open(BASE_DIR / "config" / "risk.yaml", "r") as f:
        risk = yaml.safe_load(f)

    with open(BASE_DIR / "config" / "strategy.yaml", "r") as f:
        strategy = yaml.safe_load(f)

    return Settings(
        exchange=exchange,
        risk=risk,
        strategy=strategy,
    )
