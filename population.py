#https://github.com/Koshmarjk/main
"""Модуль для работы с популяциями организмов."""

from organism import Organism


class Population:
    """Популяция — группа организмов одного вида.

    Attributes:
        species (str): Название вида.
        members (list): Список организмов популяции.
    """

    def __init__(self, species: str) -> None:
        """Инициализация популяции.

        Args:
            species: Название вида.
        """
        self.species = species
        self.members: list[Organism] = []

    def add_member(self, organism: Organism) -> None:
        """Добавляет организм в популяцию.

        Args:
            organism: Добавляемый организм.
        """
        self.members.append(organism)
        print(f"{organism.name} добавлен в популяцию '{self.species}'.")

    def remove_dead(self) -> None:
        """Удаляет мёртвых особей из популяции."""
        dead = [m for m in self.members if not m.is_alive()]
        for d in dead:
            print(f"{d.name} погиб и удалён из популяции '{self.species}'.")
        self.members = [m for m in self.members if m.is_alive()]

    def count(self) -> int:
        """Возвращает количество живых особей.

        Returns:
            Количество живых членов популяции.
        """
        return len([m for m in self.members if m.is_alive()])

    def __repr__(self) -> str:
        return f"Population(species={self.species!r}, count={self.count()})"
