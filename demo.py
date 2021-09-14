
print("Odgadnij liczbe z od 1 do 50")
liczba = int(input())
cel = 13

while True:

    if liczba > 50 or liczba < 0:
        print("podales liczbe z poza zakresu. Sprobuj ponownie")
        print("Odgadnij liczbe z od 1 do 50")
        liczba = int(input())
    elif liczba > 13 and liczba < 50:
        print("Troche za duza, wybierz mniejsza")
        print("Odgadnij liczbe z od 1 do 50")
        liczba = int(input())
    elif liczba < 13:
        print("Troche zad mala, wybierz wieksza")
        print("Odgadnij liczbe z od 1 do 50")
        liczba = int(input())
    elif liczba == cel:
        print("trafiles , to ta liczba - ", liczba)
        break


