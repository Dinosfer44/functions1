def calculate_average (numbers):
    if len (numbers) == 0:
       print ("Список пуст, невозможно посчитать среднее значение")
       return ("Попробуйте еще раз")
    else:
        average = sum(numbers) / len(numbers)
        return (average)
while True:
    user_input = input ("Введите любые чисел через пробел: ")
    try:
        numbers = list(map(int, user_input.split()))
        break
    except ValueError:
        print ("Ошибка: Убедитесь, что все введенные значения являются числами.")
result = calculate_average(numbers)
if result is None:
    print("Список пуст, невозможно посчитать среднее значение.")
else:
    print("Среднее значение:", result)