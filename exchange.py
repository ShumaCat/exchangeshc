#kolvo = input('Сколько ЛАРИ нужно перевести в АРГЕНТИНСКИЕ ПЕССО: ')

#lari = int(kolvo)

#pesso = lari * 56.11

#print(lari, "лари это", pesso, "пессо")

import time

print("Обменник валюты")
print("Автор: SHUMACAT")
time.sleep(2)
print("  ")
print("[1] Доллары США")
print("  ")
valute1 = input('Какая нужна валюта: ')
valuta1 = int(valute1)
if valuta1 == 1:
    print("Выбрана валюта: USD")
    print("  ")
    print("[1] Грузинские лари")
    print("[2] Русские рубли")
    print("[3] Аргентинские пессо")
    print("[4] Евро")
    print("  ")
    valute2 = input('В какую нужно перевести: ')
    valuta2 = int(valute2)
    if valuta2 == 1:
        kolvo1 = input('Сколько ДОЛЛАРОВ перевести в ЛАРИ: ')
        kolva1 = int(kolvo1)
        itog1 = kolva1 * 2.77
        print(sep="")
        print(kolva1, "ДОЛЛАРОВ это", itog1, "лари")
    if valuta2 == 2:
        kolvo2 = input('Сколько ДОЛЛАРОВ перевести в РУБЛИ: ')
        kolva2 = int(kolvo2)
        itog2 = kolva2 * 61.53
        print(sep="")
        print(kolva2, "ДОЛЛАРОВ это", itog2, "рублей")
    if valuta2 == 3:
        kolvo3 = input('Сколько ДОЛЛАРОВ перевести в ПЕССО: ')
        kolva3 = int(kolvo3)
        itog3 = kolva3 * 155.70
        print(sep="")
        print(kolva3, "ДОЛЛАРОВ это", itog3, "пессо")
    if valuta2 == 4:
        kolvo4 = input('Сколько ДОЛЛАРОВ перевести в ЕВРО: ')
        kolva4 = int(kolvo4)
        itog4 = kolva4 * 1
        print(sep="")
        print(kolva4, "ДОЛЛАРОВ это", itog4, "евро")
print("  ")
print("Спасибо что пользуетесь!")
