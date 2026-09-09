from datetime import timedelta
from datetime import datetime
from collections.abc import Iterator
import os
from classes import SensorData, NoDataError
import random
import string
import time
from functools import wraps
from tqdm import tqdm


def clear_terminal() -> None:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def pause() -> None:
    print("Tryck valfri tangent och enter för att fortsätta...")
    input()
    clear_terminal()


def progress_bar(total_key="total"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total = kwargs.pop(total_key, None)
            results = []
            for item in tqdm(func(*args, **kwargs), total=total, desc=func.__name__):
                results.append(item)
            return results
        return wrapper
    return decorator


def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            clear_terminal()
            print(f"Det blev visst fel med {func.__name__}. Angav du ett värde likt det som instruerats?\n")
        except NoDataError:
            clear_terminal()
            print("Det verkar som att det inte finns någon data. Har du genererat någon?\n")     
    return wrapper


def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        if isinstance(result, Iterator):
            result = list(result)

        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        print(f"{func.__name__} tog {execution_time:.4f} millisekunder!")
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
                #clear_terminal()
                print(f"Du får endast välja ett alternativ mellan 1 och {max_choice}!\n")
        except ValueError as e:
            #clear_terminal()
            print("Nu blev det visst fel. Skrev du en siffra?\n")   



# Fixa så att loading baren sker med execution time
@has_it_been_called
@execution_timer
@progress_bar()
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
    tqdm.write("Generering klar!\n")



def id_sort(id_input: str) -> list:
    pass



@exception_handler
@execution_timer
@progress_bar()
def value_sort(data: list, value_input: str) -> list:
    if data is None:
        raise NoDataError

    value_input = float(value_input)
    value_list = [item for item in data if item.value >= value_input]
    for item in value_list:
        print(item)
    print(f"Hittade {len(value_list)} resultat!\n")
    return value_list


@exception_handler
@execution_timer
@progress_bar()
def status_sort(data: list, status_input: str) -> list:
    if data is None:
        raise NoDataError

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





