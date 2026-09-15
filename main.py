from functions import timelog
from functions import menu_choice, clear_terminal, generate_data, pause, value_sort,binary_search,status_sort, device_id_input, sort_data, quicksort

data = None

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

            if generate_data.has_been_called == True:
                clear_terminal()
                print("Data har redan genererats. Vill du göra det igen?")

                print("1. Ja")
                print("2. Nej, ta mig tillbaka.")

                menu_input = menu_choice(2)

                match menu_input:
                    case 1:
                        data = generate_data()
                        pause()
                    case 2:
                        clear_terminal()
                        continue
                        
            else:
                data = generate_data()
                pause()
        case 2:

            while True:
                clear_terminal()
                print("Vad vill du filtrera efter?\n")
                print("1. Value")
                print("2. Status")
                print("3. Tillbaka")


                menu_input = menu_choice(3)

                

                match menu_input:
                    case 1:
                        print("Skriv ett värde mellan 0.0 - 100.0\n")
                        value_input = (input(".. "))
                        value_sort(data, value_input)
                        pause()

                    case 2:
                        print("Skriv vilken status du vill söka efter: OK, ERROR eller WARNING\n")
                        status_input = input(".. ").upper()
                        status_sort(data, status_input)
                        pause()

                    case 3:
                        clear_terminal()
                        break

        case 3:
            print("Skriv ett device id! (t.ex. ABC-1234)\n")

            device_id = device_id_input(".. ").upper()
            clear_terminal()

            sorted_data = sort_data(data)
            if sorted_data is not None:
                binary_result = binary_search(sorted_data, device_id)
                if binary_result == -1:
                    print("Det angivna ID:t hittades inte!\n")
                else:
                    found_device = sorted_data[binary_result]
                    print(f"{binary_result}")
            pause()


        case 4:
                
            quicksorted_data = quicksort(data, key=lambda item: item.device_id)
            pause()
            
        case 5:
            if not timelog:
                print("Inga funktioner i programmet har körts än.\nTitta förbi när du har provat någon!\n")
                pause()
            else:
                fulltime = 0.0
                for name, time in timelog:
                    print(f"{name} tog {time} ms.")
                    fulltime += time
    
                print(f"Den totala tiden för körda funktioner är: {fulltime:.4f}\n")
                pause()
                
                
        case 6:
            break


if __name__ == "__main__":
    pass