from data import list_of_soldiers


def find_soldier_by_id(soldier_id: int) -> dict | None:
    try:
        for soldier in list_of_soldiers:
            if soldier["soldier_id"] == soldier_id:
                return soldier
    except:

        return None
def is_id(solider_id:str)->bool:
    final_id=solider_id
    if not final_id.isdigit():
        return False
    if len(final_id)>8 or len(final_id)<6:
        return False
    return True
def is_valid_status(status:str)->bool:
    valid_status=["pending","completed","missed"]
    return status in valid_status
def is_valid_name(name:str)->bool:
    if not name:
        return False
    return True
def solider_has_duty(soldier: dict, duty_name: str) -> bool:
    for duty in soldier["list_duty"]:
        if duty["duty_name"] == duty_name:

           return True
    return False
def is_valid_day(day: str) -> bool:
    list_valid_days=["sunday","monday","tuesday","wednesday","thursday"]
    return day in list_valid_days
def find_duty_by_name(duties: list, duty_name: str) -> dict | None:

    if duty_name in duties:
        return



