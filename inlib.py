# conditions: {fn(str)->bool: str}
# returns None if q is pressed
def parse_input(shell, conditions):
    succeded = False # This is why named loops are good. 
    while not succeded:
        succeded = True
        user_input = input(shell)
        if user_input == "q":
            return None
        for cond, err_msg in conditions.items():
            if not cond(user_input):
                print(err_msg)
                succeded = False
    return user_input
   
