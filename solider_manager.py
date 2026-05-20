from data import list_of_soldiers
from utils import find_soldier_by_id
def add_solider(soldier_id,name)->None:
    try:
        
        if not name.isalpha():
            raise ValueError (f"must be string ")
        if find_soldier_by_id(soldier_id) is None:
            dikt_soldier=dict(name=name,soldier_id=soldier_id,list_duty=[])
            list_of_soldiers.append(dikt_soldier)
            print(list_of_soldiers)
            print("1")
    except ValueError:
        print("invalid input")
    except AttributeError:
        print("name must be string")
print(add_solider(313,"avi"))
           
        
           
      
   
        
    
       

     


