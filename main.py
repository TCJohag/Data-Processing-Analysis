from functions import menu_choice, clear_terminal


while True:

    print("AI SENSOR DATA ANALYZER\n")

    print("1. Generera data")
    print("2. Filtrera giltiga värden")
    print("3. Sök efter sensor-ID")
    print("4. Sortera data")
    print("5. Visa tidsstatistik och prestanda")
    print("6. Avsluta\n")

    

    while True:

        menu_input = menu_choice()

        match menu_input:
            case 1:
                pass
            case 2:
                print("Vad vill du filtrera efter?\n")

                print("")
                print("")
                print("")
                print("")
                print("")

                match menu_input:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass

            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break


