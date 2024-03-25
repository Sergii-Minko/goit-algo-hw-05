from decimal import Decimal


def generator_numbers(text: str):
    """
    Генерує числа з тексту як генератор, використовуючи модуль decimal.

    Args:
        text (str): Рядок, який містить числа, розділені пробілами.

    Yields:
        Decimal: Дійсне число з тексту.
    """
    words = text.split()
    print(f"words: {words}")
    for word in words:
        try:
            number = Decimal(word)  # Використовуємо Decimal для точного обчислення
            yield number
        except ValueError:
            pass


def sum_profit(text: str, func):
    """
    Обчислює загальний прибуток з чисел у тексті, використовуючи модуль decimal.

    Args:
        text (str): Рядок, який містить числа, розділені пробілами.
        func (Callable): Функція-генератор для отримання чисел.

    Returns:
        Decimal: Загальний прибуток.
    """
    total_profit = Decimal(0)
    for number in func(text):
        total_profit += number
    return total_profit


# Приклад використання:
def main():
    text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
    print(f"text: {text}")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
