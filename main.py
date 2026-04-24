"""
Точка входа симулятора экосистемы.

Связывает три слоя приложения:
  1. Слой данных    (data.py)      — начальные параметры
  2. Бизнес-логика  (ecosystem.py, population.py, organism.py)
  3. Слой интерфейса (ui.py)       — вывод в консоль

Поток вызовов:
  main → data.get_*()            # получить данные
       → Ecosystem / Population  # выполнить логику
       → ui.show_*()             # отобразить результат
"""

import data
import ui
from ecosystem import Ecosystem
from organism import Herbivore, Predator
from population import Population

REPO_URL = "https://github.com/Koshmarjk/main"  # ссылка на репозиторий


def build_ecosystem(config: dict) -> Ecosystem:
    """Собирает экосистему из данных слоя данных.

    Читает начальные данные через data.get_population_data(),
    создаёт объекты бизнес-логики и регистрирует их в экосистеме.

    Args:
        config: Конфигурация симуляции из data.get_simulation_config().

    Returns:
        Готовая к запуску экосистема.
    """
    eco = Ecosystem(config)

    # Слой данных → бизнес-логика: читаем конфигурацию популяций
    for species, role, members_data in data.get_population_data():
        pop = Population(species)
        for name, energy in members_data:
            if role == "herbivore":
                organism = Herbivore(name, energy)
            else:
                organism = Predator(name, energy)
            # Событие о добавлении уходит в слой интерфейса
            event = pop.add_member(organism)
            ui.show_setup_event(event)
        eco.add_population(pop)

    return eco


def main() -> None:
    """Главная функция: запускает симулятор экосистемы."""

    # Слой интерфейса: приветствие
    ui.show_header()

    # Слой данных → конфигурация
    config = data.get_simulation_config()

    # Бизнес-логика: создаём экосистему
    eco = build_ecosystem(config)

    # Основной цикл симуляции
    for _ in range(config["days"]):
        # Слой интерфейса: заголовок дня
        ui.show_day_header(eco.day + 1)

        # Бизнес-логика: выполняем день → получаем события
        day_log = eco.simulate_day()

        # Слой интерфейса: отображаем события дня
        ui.show_day_log(day_log)

    # Слой интерфейса: итоговый отчёт
    ui.show_final_report(eco.day, eco.get_final_status())


if __name__ == "__main__":
    main()
