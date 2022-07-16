# Додаткова домашка для тих кому цікаво розібратися з рекурсією:
# зробіть рекурсивну функцію, що порахує суму цілих чисел в заданому діапазоні
# в якості аргументів:

def main():
    def sum_recursive(first_number, last_number):
        if last_number == first_number:
            return 0
        return first_number+sum_recursive(first_number+1, last_number)

    summ = sum_recursive(1, 9)
    print('Рекурсия сумма диапазона, если дан диапазон цифр :', summ)

    def sum_recursive1(number):
        if number == 1:
            return 1
        return number+sum_recursive1(number-1)

    summ1 = sum_recursive1(8)
    print('Рекурсия сумма диапазона, если дана цифра: ', summ1)


if __name__ == '__main__':
    main()
