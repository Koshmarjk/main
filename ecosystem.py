"""Модуль экосистемы — управляет симуляцией."""

from organism import Herbivore, Predator
from population import Population


class Ecosystem:
    """Экосистема, содержащая популяции и управляющая симуляцией.

    Attributes:
        populations (list): Список популяций в экосистеме.
        day (int): Текущий день симуляции.
    """

    def __init__(self) -> None:
        """Инициализация экосистемы."""
        self.populations: list[Population] = []
        self.day: int = 0

    def add_population(self, population: Population) -> None:
        """Добавляет популяцию в экосистему.

        Args:
            population: Добавляемая популяция.
        """
        self.populations.append(population)

    def simulate_day(self) -> None:
        """Симулирует один день в экосистеме.

        Травоядные пасутся, хищники охотятся,
        все теряют немного энергии. Мёртвые удаляются.
        """
        self.day += 1
        print(f"\n{'='*40}")
        print(f"  ДЕНЬ {self.day}")
        print(f"{'='*40}")

        herbivores = []
        predators = []

        # Собираем всех живых особей по ролям
        for pop in self.populations:
            for member in pop.members:
                if member.is_alive():
                    if isinstance(member, Herbivore):
                        herbivores.append(member)
                    elif isinstance(member, Predator):
                        predators.append(member)

        # Травоядные пасутся
        print("\n-- Травоядные пасутся --")
        for h in herbivores:
            h.graze()

        # Хищники охотятся
        print("\n-- Хищники охотятся --")
        for p in predators:
            if herbivores:
                prey = herbivores[0]  # охотится на первого доступного
                p.hunt(prey)
            else:
                p.lose_energy(10)
                print(f"{p.name} не нашёл добычи.")

        # Все теряют базовую энергию за день
        print("\n-- Суточные затраты энергии --")
        for pop in self.populations:
            for member in pop.members:
                if member.is_alive():
                    member.lose_energy(5)

        # Убираем погибших
        for pop in self.populations:
            pop.remove_dead()

        self.print_status()

    def print_status(self) -> None:
        """Выводит текущее состояние экосистемы."""
        print("\n-- Состояние экосистемы --")
        for pop in self.populations:
            print(f"  {pop.species}: {pop.count()} особей")
