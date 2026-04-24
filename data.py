"""
Слой данных (Data Layer).

Хранит начальные конфигурации организмов и популяций.
Бизнес-логика обращается сюда, чтобы получить
стартовые параметры — сама она их не хранит.
"""

# Начальные данные популяций: (название_вида, роль, [(имя, энергия), ...])
POPULATION_DATA: list[tuple[str, str, list[tuple[str, int]]]] = [
    (
        "Зайцы",
        "herbivore",
        [
            ("Борис", 30),
            ("Миша", 25),
        ],
    ),
    (
        "Лисы",
        "predator",
        [
            ("Алиса", 40),
        ],
    ),
]

# Параметры симуляции
SIMULATION_DAYS: int = 3
DAILY_ENERGY_COST: int = 5
GRAZE_GAIN: int = 15
HUNT_GAIN: int = 20
HUNT_DAMAGE: int = 25
HUNGER_LOSS: int = 10


def get_population_data() -> list[tuple[str, str, list[tuple[str, int]]]]:
    """Возвращает список начальных данных для всех популяций.

    Returns:
        Список кортежей (вид, роль, [(имя, энергия)]).
    """
    return POPULATION_DATA


def get_simulation_config() -> dict[str, int]:
    """Возвращает конфигурацию симуляции.

    Returns:
        Словарь с параметрами: дни, затраты, урон и т.д.
    """
    return {
        "days": SIMULATION_DAYS,
        "daily_cost": DAILY_ENERGY_COST,
        "graze_gain": GRAZE_GAIN,
        "hunt_gain": HUNT_GAIN,
        "hunt_damage": HUNT_DAMAGE,
        "hunger_loss": HUNGER_LOSS,
    }
