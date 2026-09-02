from datetime import timedelta
from datetime import datetime
from collections.abc import Iterator
import os
from classes import SensorData
import random
import string
import time
from functools import wraps

def clear_terminal() -> None:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def pause() -> None:
    print("Tryck valfri tangent och enter för att fortsätta...")
    input()

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        if isinstance(result, Iterator):
            result = list(result)

        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{func.__name__} tog {total_time:.4f} sekunder!")
        return result
    return wrapper


def has_it_been_called(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)
    wrapper.has_been_called = False
    return wrapper

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

@has_it_been_called
@execution_time
def generate_data() -> Iterator[SensorData]:
    for x in range(1_000_000):
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


        yield SensorData(device_id, timestamp, value, status)




    

