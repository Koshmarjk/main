"""Точка входа консольного симулятора жизни."""

from ecosystem import Ecosystem
from organism import Herbivore, Predator
from population import Population
from utils import get_simulation_summary, print_separator

REPO_URL = "https://github.com/username/life_simulator"  # ссылка на репозиторий


def main() -> None:
    """Основная функция запуска симуляции."""
    print("Консольный симулятор жизни")
    print_separator("=")

    # Создаём экосистему
    eco = Ecosystem()

    # Создаём популяцию травоядных
    herbivore_pop = Population("Зайцы")
    herbivore_pop.add_member(Herbivore("Заяц Борис", 30))
    herbivore_pop.add_member(Herbivore("Заяц Миша", 25))

    # Создаём популяцию хищников
    predator_pop = Population("Лисы")
    predator_pop.add_member(Predator("Лиса Алиса", 40))

    # Добавляем популяции в экосистему
    eco.add_population(herbivore_pop)
    eco.add_population(predator_pop)

    # Запускаем симуляцию на 3 дня
    for _ in range(3):
        eco.simulate_day()

    # Итог
    print_separator("=")
    print(get_simulation_summary(eco.day, eco.populations))


if __name__ == "__main__":
    main()
