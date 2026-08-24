import os

def clear_terminal() -> None:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def menu_choice():
    try:
        menu_input = int(input("Välj ett alternativ mellan 1-6..\n"))
        if 1 <= menu_input <= 6:
            return menu_input
        else:
            print("Du får endast välja ett alternativ mellan 1 och 6!\n")
    except ValueError as e:
        print("Nu blev det visst fel. Skrev du en siffra?\n")   
