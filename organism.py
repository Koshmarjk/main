#https://github.com/Koshmarjk/main
# Модуль организмов экосистемы
"""Модуль с классами организмов экосистемы."""


class Organism:
    """Базовый класс организма.

    Attributes:
        name (str): Имя организма.
        energy (int): Уровень энергии (здоровья).
    """

    def __init__(self, name: str, energy: int) -> None:
        """Инициализация организма.

        Args:
            name: Имя организма.
            energy: Начальный уровень энергии.
        """
        self.name = name
        self.energy = energy

    def is_alive(self) -> bool:
        """Проверяет, жив ли организм.

        Returns:
            True, если энергия больше 0.
        """
        return self.energy > 0

    def eat(self, amount: int) -> None:
        """Организм получает энергию от еды.

        Args:
            amount: Количество добавляемой энергии.
        """
        self.energy += amount
        print(f"{self.name} поел и получил {amount} энергии. "
              f"Энергия: {self.energy}")

    def lose_energy(self, amount: int) -> None:
        """Организм теряет энергию.

        Args:
            amount: Количество теряемой энергии.
        """
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} потерял {amount} энергии. "
              f"Энергия: {self.energy}")

    def __repr__(self) -> str:
        return f"Organism(name={self.name!r}, energy={self.energy})"


class Herbivore(Organism):
    """Травоядное животное. Ест растения, теряет энергию каждый день."""

    def __init__(self, name: str, energy: int) -> None:
        super().__init__(name, energy)
        self.role = "травоядное"

    def graze(self) -> None:
        """Пасётся: получает 15 единиц энергии."""
        self.eat(15)


class Predator(Organism):
    """Хищник. Охотится на травоядных."""

    def __init__(self, name: str, energy: int) -> None:
        super().__init__(name, energy)
        self.role = "хищник"

    def hunt(self, prey: Organism) -> None:
        """Охотится на жертву.

        Args:
            prey: Организм-жертва.
        """
        if prey.is_alive():
            gain = 20
            prey.lose_energy(25)
            self.eat(gain)
            print(f"{self.name} поохотился на {prey.name}!")
        else:
            print(f"{self.name} не нашёл живой жертвы.")
