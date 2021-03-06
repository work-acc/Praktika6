# Вариант 10. Ввести список А из 10 элементов,
# найти произведение положительных элементов кратных 3,
# их количество и вывести результаты на экран.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    # Найти искомую сумму.
    s = 1
    i = 0
    for item in A:
        if item % 3 == 0:
            s *= item
            i += 1
    print(s, i)
