"""
Бизнес-логика (Business Logic Layer) — популяции.

Класс Population управляет группой особей одного вида:
добавляет, удаляет погибших, предоставляет живых членов.
Не выводит ничего в консоль — возвращает события строками.
"""

from organism import Organism


class Population:
    """Популяция — группа особей одного биологического вида.

    Attributes:
        species (str): Название вида.
        members (list[Organism]): Все особи популяции.
    """

    def __init__(self, species: str) -> None:
        """Создаёт пустую популяцию.

        Args:
            species: Название вида (например, «Зайцы»).
        """
        self.species = species
        self.members: list[Organism] = []

    def add_member(self, organism: Organism) -> str:
        """Добавляет особь и возвращает событие для интерфейса.

        Args:
            organism: Новая особь.

        Returns:
            Строка-событие о добавлении.
        """
        self.members.append(organism)
        return f"{organism.name} добавлен в популяцию «{self.species}»"

    def remove_dead(self) -> list[str]:
        """Удаляет погибших особей.

        Returns:
            Список строк-событий о каждой гибели.
        """
        events = []
        dead = [m for m in self.members if not m.is_alive()]
        for victim in dead:
            events.append(
                f"{victim.name} погиб (прожил {victim.age} дн.), "
                f"исключён из «{self.species}»"
            )
        self.members = [m for m in self.members if m.is_alive()]
        return events

    def living_members(self) -> list[Organism]:
        """Возвращает список живых особей.

        Returns:
            Список с energy > 0.
        """
        return [m for m in self.members if m.is_alive()]

    def count(self) -> int:
        """Количество живых особей.

        Returns:
            Целое число.
        """
        return len(self.living_members())

    def __repr__(self) -> str:
        return f"Population(species={self.species!r}, alive={self.count()})"
