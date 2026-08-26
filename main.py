from functions import menu_choice, clear_terminal


while True:

    print("AI SENSOR DATA ANALYZER\n")

    print("1. Generera data")
    print("2. Filtrera giltiga värden")
    print("3. Sök efter sensor-ID")
    print("4. Sortera data")
    print("5. Visa tidsstatistik och prestanda")
    print("6. Avsluta\n")

    



    menu_input = menu_choice(6)

    match menu_input:
        case 1:
            pass
        case 2:

            while True:
                clear_terminal()
                print("Vad vill du filtrera efter?\n")

                menu_input = menu_choice(5)

                print("1. Namn")
                print("2. Datum")
                print("3. Värde")
                print("4. Värde 2")
                print("5. Tillbaka")

                match menu_input:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        clear_terminal()
                        break

        case 3:
            #List comprehension, (data.id for id in dataframe if search_input == data.id) t.ex.
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            break


