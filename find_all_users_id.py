from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    id = []
    messages = data['messages']
    for i in messages:
        x = i.get("actor_id",False)
        y = i.get("from_id",False)
        if x != False:
            id.append(x)
        if y != False:
            id.append(y)               
    return id

data = read_data('data/result.json')
print(find_all_users_id(data))