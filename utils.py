from data import list_of_soldiers


def find_soldier_by_id(soldier_id: int) -> dict | None:
    for soldier in list_of_soldiers:
        if soldier["soldier_id"] == soldier_id:
            return soldier

    return None