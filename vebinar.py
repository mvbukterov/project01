#from collections import Counter
#text = input("Введите строку: ")
#letters = 'АГЦТагцт'
#freq = Counter(text)
#for letter in letters:
#    print(f"{letter}: {freq.get(letter, 0)}")

# Ввод данных
try:
    day = int(input("Введите день (1-28): "))
    current_weight = float(input("Введите текущий вес (в кг): "))

    if not (1 <= day <= 28):
        print("День должен быть от 1 до 28.")
        exit()
    if not (80 <= current_weight <= 90):
        print("Вес должен быть от 80 до 90 кг.")
        exit()

    # Расчёт ожидаемого веса на этот день
    expected_weight = 90 - (10 / 28) * (day - 1)
    expected_weight = round(expected_weight, 2)

    # Сравнение
    print(f"\nОжидаемый вес на день {day}: {expected_weight} кг")
    print(f"Ваш текущий вес: {current_weight} кг")

    if abs(current_weight - expected_weight) < 0.1:
        print("✅ Вес в норме — вы на графике!")
    elif current_weight < expected_weight:
        print("🟢 Отлично Вы худеете быстрее плана!")
    else:
        print("🟡 Вы немного отстаёте от графика. Нужно поднажать.")

except ValueError:
    print("Ошибка ввода: введите число.")