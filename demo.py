
print("Odgadnij liczbe z od 1 do 50")
liczba = int(input())
warunek = True


while warunek == True:

    if liczba < 0 and liczba >50:
        print("podales liczbe z poza zakresu. Sprobuj ponownie")
else:
       print("czy chesz zagrac ponownie t/n")
       warunek = input()

