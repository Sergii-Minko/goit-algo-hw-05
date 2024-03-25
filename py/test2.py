from decimal import Decimal
import re


# Функція для генерування чисел з тексту
def generator_numbers(text: str):
    # Використовуємо регулярні вирази для знаходження чисел
    pattern = r"[-+]?\d*\.\d+|\d+"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield Decimal(number)  # Використовуємо Decimal для точного обчислення


# Функція для обчислення загального прибутку
def sum_profit(text: str, func):
    total_profit = Decimal(0)
    for number in func(text):
        total_profit += number
    return total_profit


# Приклад використання:
def main():
    text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
