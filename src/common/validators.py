from common.exceptions import ConfigurationException


def validate_percentage(value: float, field: str):

    if value <= 0:
        raise ConfigurationException(
            f"{field} precisa ser maior que zero."
        )

    if value >= 100:
        raise ConfigurationException(
            f"{field} precisa ser menor que 100."
        )
