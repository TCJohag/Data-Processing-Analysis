from classes import SensorData
from functions import menu_choice, clear_terminal, generate_data, pause


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
            #Kolla ifall generate_data har körts tidigare, om så varna användaren

            if generate_data.has_been_called == True:
                print("Data har redan genererats. Vill du göra det igen?")

                print("1. Ja")
                print("2. Nej, ta mig tillbaka.")

                menu_input = menu_choice(2)

                match menu_input:
                    case 1:
                        generate_data()
                        print("Generering klar!")
                        pause()
                    case 2:
                        break
            else:
                generate_data()
                print("Generering klar!")
                pause()
        case 2:

            while True:
                clear_terminal()
                print("Vad vill du filtrera efter?\n")

                menu_input = menu_choice(3)

                print("1. Value")
                print("2. Status")
                print("3. Tillbaka")

                match menu_input:
                    case 1:
                        print("Skriv ett värde mellan 0.0 - 100.0\n")
                        value_input = print("..")

                        value_list = [value for value in SensorData.list if SensorData.value >= value_input in value]
                        for values in value_list:
                            print(values)
                    case 2:
                        pass
                    case 3:
                        clear_terminal()
                        break

        case 3:
            #Binärsökning, listan måste vara sorterad
            #Användaren matar in ett device_id, eller tre fasta värden: första i listan, i mitten och ett som inte finns
            pass
        case 4:
            #Sortera hela datan baserat på device_id eller value. Quicksort
            pass
        case 5:
            #Skriver ut en sammanställning av de senast uppmätta tiderna för generering, filtrering, sortering, sökning
            pass
        case 6:
            break


if __name__ == "__main__":
    pass