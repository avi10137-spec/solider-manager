from data import list_of_soldiers
from utils import *

def add_solider(soldier_id,name)->None:
    try:
        
        if not name.isalpha():
            raise ValueError (f"must be string ")
        if find_soldier_by_id(soldier_id) is None:
            dikt_soldier=dict(name=name,soldier_id=soldier_id,list_duty=[])
            list_of_soldiers.append(dikt_soldier)
            print(list_of_soldiers)
            print("1")
        return None
    except ValueError:
        print("invalid input")
    except AttributeError:
        print("name must be string")
def remove_solider(solider_id):

        for sold in list_of_soldiers:
            if find_soldier_by_id(solider_id):
                list_of_soldiers.remove(sold)
                print("the solider sub in sucses ")
            else:
                raise KeyError(f" solider not find ")

def get_all_soliders(list_of_soldiers):
    if list_of_soldiers:
        return list_of_soldiers
    return []






           
        
           
      
   
        
    
       

     


