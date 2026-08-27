from datetime import timedelta
from datetime import datetime
from time import sleep
from time import gmtime
from time import strftime
from collections.abc import Iterator
import os
from classes import SensorData
import random
import string
import time

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

def generate_data() -> Iterator[SensorData]:
    for x in range (0,1000000):
        device_id = ""

        for letters in range(3):
            device_id += random.choice(string.ascii_uppercase)

        device_id += "-"

        for digits in range(4):
            device_id += random.choice(string.digits)


        # Timestamp

        days_back = random.randint(0, 700)
        seconds = random.randint(0, 86399)
        random_dt = datetime.now() - timedelta(days=days_back, seconds=seconds)


        timestamp = random_dt.strftime("%a, %d %b %Y %H:%M:%S")



        value = round(random.uniform(0.0, 100.0), 1)

        status = random.choice(["OK", "ERROR", "WARNING"])


        sleep(3)
        yield SensorData(device_id, timestamp, value, status)


generate_data()

for x in generate_data():
    print(f"{x}")

