from data import list_of_soldiers
from utils import *
from solider_manager import *


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str,) -> None:
    if not is_valid_name(duty_name):
        raise ValueError("duty is not exist")
    if not is_valid_day(day):
        raise ValueError("day is invalid")
    solider = find_soldier_by_id(soldier_id)
    if solider is None:
        raise KeyError("id is invalid")

    for duti in solider["list_duty"]:
        if duti["duty name"] == duty_name and duti["day"] == day:
            raise ValueError("has duty")
    solider["list_duty"].append({"duty name": duty_name, "day": day, "status": "pending"})
    print(solider)
    return list_of_soldiers
def get_soldier_duties(soldier_id: int) -> list:
    solider = find_soldier_by_id(soldier_id)
    return solider["list_duty"]
def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    solider=find_soldier_by_id(soldier_id)
    if solider is None:
        raise KeyError("solider not exist")
    if not is_valid_status(new_status):
        raise ValueError ("status is invalid")
    for duty in solider["list_duty"]:
        if duty["duty name"] == duty_name:
            duty["status"] =new_status
            return None
    raise KeyError ("duty not exist")












