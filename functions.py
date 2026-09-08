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
        execution_time = end_time - start_time
        print(f"{func.__name__} tog {execution_time:.4f} sekunder!")
        return result
    return wrapper


def has_it_been_called(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        clear_terminal()
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
                print(f"Du får endast välja ett alternativ mellan 1 och {max_choice}!\n")
        except ValueError as e:
            clear_terminal()
            print("Nu blev det visst fel. Skrev du en siffra?\n")   



# Fixa så att loading baren sker med execution time
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


        days_back = random.randint(0, 700)
        seconds = random.randint(0, 86399)
        random_dt = datetime.now() - timedelta(days=days_back, seconds=seconds)
        timestamp = random_dt.strftime("%a, %d %b %Y %H:%M:%S")



        value = round(random.uniform(0.0, 100.0), 1)

        status = random.choice(["OK", "ERROR", "WARNING"])


        yield SensorData(device_id, timestamp, value, status)


    
# def sort_generated_data(data: list) -> list:
#     data.sort()


def id_sort(data: list) -> list:
    device_id_list = [device_id for device_id in data if data.device_id in device_id]
    for device_ids in device_id_list:
        print(device_ids)


def value_sort(data: list, value_input: float) -> list:
        value_list = [item for item in data if item.value >= value_input]
        for item in value_list:
            print(item)
        print(f"Hittade {len(value_list)} resultat!\n")
        return value_list


def status_sort(data: list, status_input: string) -> list:
    ALLOWED = {"OK", "WARNING", "ERROR"}

    if status_input not in ALLOWED:
        raise ValueError
    else:
        status_list = [item for item in data if item.status == status_input]
        for item in status_list:
            print(item)
        print(f"Hittade {len(status_list)} resultat!\n")
        return status_list



def binary_search(data: list, id_input: string) -> list:
    pass

def device_id_search(data: list, id_input: string) -> list:
    pass





