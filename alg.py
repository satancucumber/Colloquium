from random import randint

conditions = []
# Открытие файла (последняя строка - пустая)
with open("1307Litsevanova.txt", "r") as file:
    line = file.readline()
    while line != "#":
        conditions.append(line[:-1])
        line = file.readline()


# Разделение условия на переменные с отрицанием и без
def splitCondition(condition):
    if "_" in condition:
        cond_true, cond_false = condition.split("_")
    else:
        cond_true, cond_false = condition, ""

    return cond_true, cond_false


# Проверка вектора на выполнение условий
def checkS(conditions, S):
    F = 0  # Кол-во выполненных условий (Фитнес)
    for condition in conditions:
        done = False  # Выполнение условия
        cond_true, cond_false = splitCondition(condition)
        for symbol in cond_true:  # Проверка переменных без отрицания
            if S[ord(symbol) - 97] == 1:
                stop_mut[ord(symbol) - 97] = 1
                done = True
                # break
        if not done:
            for symbol in cond_false:  # Провера переменных с отрицанием
                if S[ord(symbol) - 97] == 0:
                    stop_mut[ord(symbol) - 97] = 1
                    done = True
                    # break
        if done:  # Если условие выполняется
            F += 1

    return F


# Мутация
def mutate(S, n=5):
    for _ in range(n):
        i = randint(0, len(S) - 1)
        if stop_mut[i] != 1:
            S[i] = not S[i]
    return S


print(conditions)

N = 26  # Кол-во переменных
S = [randint(0, 1) for _ in range(N)]  # Случайный вектор
stop_mut = [0 for _ in range(N)]  # Вектор для закрепления мутаций
prevS = S  # Предыдущий случайный вектор
R = len(conditions)  # Необходимое значение фитнеса
F = 0  # Фитнес
prevF = 0  # Предыдущий фитнес
i = 0  # Номер поколения
steps = 0

from datetime import datetime

start = datetime.now()

while (F != R):
    if i > R * 10:  # Если поколений слишком много, возможно эволюция зашла в тупик, начнём с начала
        i = 0
        stop_mut = [0 for _ in range(N)]
        S = [randint(0, 1) for _ in range(N)]
        prevS = S
        F = 0
        prevF = F
        print("Restart", end=" ")
    i += 1
    steps += 1
    prevF = F
    F = checkS(conditions, S)
    if prevF > F:
        S = prevS
        F = prevF
    prevS = S
    S = mutate(S, R - F)
    print(F, end=" ")

end = datetime.now()

print(S)
print("\nРешено за " + str(steps) + " steps")
print("Решено за " + str(end - start) + " ")
