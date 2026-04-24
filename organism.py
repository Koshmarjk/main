"""
Бизнес-логика (Business Logic Layer) — организмы.

Содержит абстрактный класс Organism и его конкретные
реализации: Herbivore (травоядное) и Predator (хищник).
Не занимается ни выводом в консоль, ни хранением данных.
"""

from abc import ABC, abstractmethod


class Organism(ABC):
    """Абстрактный базовый класс для всех живых существ.

    Attributes:
        name (str): Имя особи.
        energy (int): Текущий запас энергии.
        age (int): Возраст в прожитых днях.
    """

    def __init__(self, name: str, energy: int) -> None:
        """Инициализирует организм.

        Args:
            name: Имя особи.
            energy: Начальный запас энергии.
        """
        self.name = name
        self.energy = energy
        self.age: int = 0

    @abstractmethod
    def act(self, config: dict) -> list[str]:
        """Выполняет действие особи за один день.

        Args:
            config: Словарь параметров симуляции из слоя данных.

        Returns:
            Список строк-событий для передачи в слой интерфейса.
        """

    def is_alive(self) -> bool:
        """Проверяет, жива ли особь.

        Returns:
            True если энергия больше нуля.
        """
        return self.energy > 0

    def gain_energy(self, amount: int) -> str:
        """Пополняет энергию и возвращает описание события.

        Args:
            amount: Количество добавляемой энергии.

        Returns:
            Строка-событие для интерфейса.
        """
        self.energy += amount
        return f"{self.name} получил +{amount} энергии [итого: {self.energy}]"

    def lose_energy(self, amount: int) -> str:
        """Тратит энергию и возвращает описание события.

        Args:
            amount: Количество расходуемой энергии.

        Returns:
            Строка-событие для интерфейса.
        """
        self.energy = max(0, self.energy - amount)
        return f"{self.name} потерял -{amount} энергии [итого: {self.energy}]"

    def age_one_day(self) -> None:
        """Увеличивает возраст на один день."""
        self.age += 1

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(name={self.name!r}, energy={self.energy}, age={self.age})")


class Herbivore(Organism):
    """Травоядное животное.

    Каждый день пасётся и пополняет энергию.
    Является целью для хищников.
    """

    def __init__(self, name: str, energy: int) -> None:
        super().__init__(name, energy)
        self.role = "herbivore"

    def act(self, config: dict) -> list[str]:
        """Пасётся: получает энергию согласно конфигурации.

        Args:
            config: Параметры из слоя данных (graze_gain).

        Returns:
            Список из одного события — результат выпаса.
        """
        event = self.gain_energy(config["graze_gain"])
        return [f"{self.name} пасётся. {event}"]


class Predator(Organism):
    """Хищник.

    Охотится на травоядных. При отсутствии добычи — голодает.
    """

    def __init__(self, name: str, energy: int) -> None:
        super().__init__(name, energy)
        self.role = "predator"
        self._target: Organism | None = None

    def set_target(self, target: Organism) -> None:
        """Назначает жертву для охоты.

        Args:
            target: Особь-жертва.
        """
        self._target = target

    def act(self, config: dict) -> list[str]:
        """Охотится на цель или голодает.

        Args:
            config: Параметры из слоя данных
                    (hunt_gain, hunt_damage, hunger_loss).

        Returns:
            Список строк-событий о результате охоты.
        """
        events = []
        if self._target and self._target.is_alive():
            events.append(f"{self.name} нападает на {self._target.name}!")
            events.append(self._target.lose_energy(config["hunt_damage"]))
            events.append(self.gain_energy(config["hunt_gain"]))
        else:
            events.append(f"{self.name} не нашёл добычи и голодает.")
            events.append(self.lose_energy(config["hunger_loss"]))
        self._target = None
        return events
