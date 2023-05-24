S = input("Введите общее количество журавликов, которое сделали дети: ")
S = int(S)
Sergei = S/6
Petr = S/6
Katya = S - (Sergei + Petr)
print("Сережа сделал: ", int(Sergei), "Петя сделал: ", int(Petr), "Катя сделала: ", int(Katya))