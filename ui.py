"""
Слой интерфейса (Interface / Presentation Layer).

Отвечает ТОЛЬКО за вывод информации в консоль.
Получает данные от бизнес-логики (ecosystem.py) и
форматирует их для пользователя.
Не содержит никакой логики симуляции.

Схема взаимодействия:
  ui.py ← получает события от → ecosystem.py
"""

PHASE_LABELS = {
    "phase1": "Фаза 1 | Выпас травоядных",
    "phase2": "Фаза 2 | Охота хищников",
    "phase3": "Фаза 3 | Суточные затраты",
    "phase4": "Фаза 4 | Итоги дня (гибели)",
    "status": "Состояние экосистемы",
}


def show_header() -> None:
    """Выводит заголовок симулятора при запуске."""
    print("╔══════════════════════════════════════════╗")
    print("║     КОНСОЛЬНЫЙ СИМУЛЯТОР ЭКОСИСТЕМЫ      ║")
    print("╚══════════════════════════════════════════╝")


def show_day_header(day: int) -> None:
    """Выводит заголовок нового дня симуляции.

    Args:
        day: Номер текущего дня.
    """
    print(f"\n{'─' * 44}")
    print(f"  ☀  ДЕНЬ {day}")
    print(f"{'─' * 44}")


def show_day_log(log: dict[str, list[str]]) -> None:
    """Выводит в консоль все события одного дня.

    Получает словарь событий от бизнес-логики (Ecosystem.simulate_day)
    и форматирует каждую фазу.

    Args:
        log: Словарь {'phase1': [...], ..., 'status': [...]}.
    """
    for key, label in PHASE_LABELS.items():
        events = log.get(key, [])
        print(f"\n[{label}]")
        if events:
            for event in events:
                print(f"  {event}")
        else:
            print("  (событий нет)")


def show_setup_event(message: str) -> None:
    """Выводит событие при инициализации экосистемы.

    Args:
        message: Строка-событие от бизнес-логики.
    """
    print(f"  + {message}")


def show_final_report(elapsed_days: int,
                      results: list[tuple[str, int]]) -> None:
    """Выводит итоговый отчёт по завершении симуляции.

    Args:
        elapsed_days: Количество прошедших дней.
        results: Список (вид, количество выживших) от бизнес-логики.
    """
    print("\n" + "═" * 44)
    print(f"  Симуляция завершена. Прошло дней: {elapsed_days}")
    for species, count in results:
        outcome = "выжили" if count > 0 else "вымерли"
        print(f"  • {species}: {count} особей ({outcome})")
    print("═" * 44)
