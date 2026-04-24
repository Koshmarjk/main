#https://github.com/Koshmarjk/main/edit/main
"""
Бизнес-логика (Business Logic Layer) — экосистема.

Класс Ecosystem оркестрирует симуляцию:
- получает конфигурацию из слоя данных (data.py),
- управляет популяциями и организмами,
- возвращает события каждого дня в слой интерфейса (ui.py).

Схема взаимодействия слоёв:
  ui.py → ecosystem.py → population.py / organism.py → data.py
"""

from organism import Herbivore, Predator, Organism
from population import Population


class Ecosystem:
    """Экосистема: объединяет популяции и управляет симуляцией.

    Получает данные из слоя данных, выполняет бизнес-логику,
    возвращает результаты в слой интерфейса в виде словаря событий.

    Attributes:
        populations (list[Population]): Популяции экосистемы.
        day (int): Номер текущего дня.
        config (dict): Конфигурация симуляции из слоя данных.
    """

    def __init__(self, config: dict) -> None:
        """Создаёт экосистему с параметрами из слоя данных.

        Args:
            config: Словарь параметров (daily_cost, hunt_gain и т.д.)
                    — получается вызовом data.get_simulation_config().
        """
        self.populations: list[Population] = []
        self.day: int = 0
        self.config = config

    def add_population(self, population: Population) -> None:
        """Регистрирует популяцию в экосистеме.

        Args:
            population: Добавляемая популяция.
        """
        self.populations.append(population)

    def _get_living(self, cls: type) -> list[Organism]:
        """Собирает живых особей заданного класса из всех популяций.

        Args:
            cls: Класс-фильтр (Herbivore или Predator).

        Returns:
            Список живых особей этого класса.
        """
        result = []
        for pop in self.populations:
            for member in pop.living_members():
                if isinstance(member, cls):
                    result.append(member)
        return result

    def simulate_day(self) -> dict[str, list[str]]:
        """Выполняет один день симуляции.

        Бизнес-логика одного дня разбита на 4 фазы.
        Результат каждой фазы — список строк-событий,
        которые слой интерфейса (ui.py) выведет в консоль.

        Returns:
            Словарь {'phase1': [...], 'phase2': [...],
                     'phase3': [...], 'phase4': [...],
                     'status': [...]}
        """
        self.day += 1
        log: dict[str, list[str]] = {
            "phase1": [],
            "phase2": [],
            "phase3": [],
            "phase4": [],
            "status": [],
        }

        herbivores = self._get_living(Herbivore)
        predators = self._get_living(Predator)

        # Фаза 1: травоядные пасутся
        for animal in herbivores:
            log["phase1"].extend(animal.act(self.config))
            animal.age_one_day()

        # Фаза 2: хищники охотятся
        for predator in predators:
            prey_list = self._get_living(Herbivore)
            if prey_list:
                predator.set_target(prey_list[0])
            log["phase2"].extend(predator.act(self.config))
            predator.age_one_day()

        # Фаза 3: суточные затраты энергии
        for pop in self.populations:
            for member in pop.living_members():
                log["phase3"].append(
                    member.lose_energy(self.config["daily_cost"])
                )

        # Фаза 4: удаление погибших
        for pop in self.populations:
            log["phase4"].extend(pop.remove_dead())

        # Статус популяций
        for pop in self.populations:
            bar = "●" * pop.count() if pop.count() > 0 else "—"
            log["status"].append(
                f"{pop.species}: {pop.count()} особей  {bar}"
            )

        return log

    def get_final_status(self) -> list[tuple[str, int]]:
        """Возвращает итоговые данные для отчёта.

        Returns:
            Список кортежей (вид, количество выживших).
        """
        return [(pop.species, pop.count()) for pop in self.populations]
