from solider_manager import *
from utils import *
from  duty_manager import *
import data
def show_menu():
    print(" The system for managing soldiers ")
    print("=====================")
    print("1.  add solider ")
    print("2.  sub solider ")
    print("3. show all solider ")
    print("4. add duty ")
    print("5. update status duty ")
    print("6. sow all duties ")
    print("7. exit")
    print("=======================")

def get_user_choice()->str:
    choise=input("please enter your choise :")
    return choise

def handle_add_solider():
    name = input(" enter name :")
    solider_id = (input("enter id :"))
    if is_id(solider_id):
        solider_id =int(solider_id)

    add_solider(solider_id, name)
    return None



def  handle_remove_soldier() -> None:

    solider_id = input("enter id :")
    if is_id(solider_id):
        solider_id=int(solider_id)

    remove_solider(solider_id)
    return None

def handle_view_soldiers() -> None:
    get_all_soliders(list_of_soldiers)
    print(list_of_soldiers)
    return None

def handle_add_duty() -> None:
    solider_id=int(input("enter yor id"))
    duty=input("enter your duty")
    day=input("enter day")
    add_duty_to_soldier(solider_id,duty,day,)
    return None
def handle_update_duty_status() -> None:
    solider_id = int(input("enter yor id"))
    duty_name = input("enter your duty")
    status=input("enter status")
    update_duty_status(solider_id,duty_name,status)
    return None
def handle_view_soldier_duties() -> None:
    solider_id=input("enter id")
    solider=find_soldier_by_id(int(solider_id))
    print(solider["list_duty"])
    return None
def main():
    while True:
        show_menu()
        chois=get_user_choice()
        if chois == "1":
            handle_add_solider()
        if chois == "2":
            handle_remove_soldier()
        if chois == "3":
            handle_view_soldiers()
        if chois == "4":
            handle_add_duty()
        if chois == "5":
            handle_update_duty_status()
        if chois == "6":
            handle_view_soldier_duties()
        if chois == "7":
            break



if __name__ =="__main__":
    main()
