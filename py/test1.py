def caching_fibonacci():
    """
    Генерує функцію для обчислення чисел Фібоначчі з використанням кешування.

    Returns:
        function: Функція, яка приймає аргумент `n` і повертає `n`-те число Фібоначчі.
    """
    cache = {}  # Словник для збереження обчислених значень

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]  # Використовуємо кеш, якщо значення вже обчислено
        cache[n] = fibonacci(n - 1) + fibonacci(
            n - 2
        )  # Рекурсивно обчислюємо та зберігаємо результат
        return cache[n]

    return fibonacci


def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()
    n = int(input("Enter n: "))
    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(n))  

if __name__ == "__main__":
    main()
