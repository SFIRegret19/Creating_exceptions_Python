class Car:
    
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin).__eq__(True) and self.__is_valid_numbers(numbers).__eq__(True):
            self.__vin = vin
            self.__numbers = numbers
    
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int).__eq__(False):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif (1000000 <= vin_number <= 9999999).__eq__(False):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str).__eq__(False):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers).__eq__(6) == False:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')