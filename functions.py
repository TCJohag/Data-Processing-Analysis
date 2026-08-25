import os

def clear_terminal() -> None:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def menu_choice(max_choice):
    while True:
        try:
            menu_input = int(input(f"Välj ett alternativ mellan 1-{max_choice}..\n"))
            if 1 <= menu_input <= max_choice:
                return menu_input
            else:
                clear_terminal()
                print("Du får endast välja ett alternativ mellan 1 och 6!\n")
        except ValueError as e:
            clear_terminal()
            print("Nu blev det visst fel. Skrev du en siffra?\n")   
            