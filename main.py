


while True:

    print("AI SENSOR DATA ANALYZER\n")

    print("1. Generera data")
    print("2. Filtrera giltiga värden")
    print("3. Sök efter sensor-ID")
    print("4. Sortera data")
    print("5. Visa tidsstatistik och prestanda")
    print("6. Avsluta\n")

    

    while True:
        try:
            menu_input = int(input("Välj ett alternativ mellan 1-6..\n"))
            if 1 <= menu_input <= 6:
                break
            else:
                print("Du får endast välja ett alternativ mellan 1 och 6!\n")
        except ValueError as e:
            print("Nu blev det visst fel. Skrev du en siffra?\n")   


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
            pass
        case 6:
            break


pass