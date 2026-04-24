#https://github.com/Koshmarjk/main
"""Вспомогательные функции для симулятора жизни."""


def print_separator(char: str = "-", length: int = 40) -> None:
    """Печатает разделитель для вывода в консоль.

    Args:
        char: Символ разделителя.
        length: Длина разделителя.
    """
    print(char * length)


def get_simulation_summary(day: int, populations: list) -> str:
    """Формирует итоговую сводку симуляции.

    Args:
        day: Номер последнего дня симуляции.
        populations: Список популяций экосистемы.

    Returns:
        Строка с итоговым отчётом.
    """
    lines = [f"Симуляция завершена. Прошло дней: {day}"]
    for pop in populations:
        lines.append(f"  {pop.species}: выжило {pop.count()} особей")
    return "\n".join(lines)
