from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    id = {"user1046157991"}
    id1 = []
    messages = data['messages']
    for i in messages:
        x = i.get("actor_id",False)
        y = i.get("from_id",False)
        if x != False:
            # id.append(x)
            id.add(x)
        if y != False:
            id.add(y)
            # id.append(y) 
    for n in id:
        id1.append(n)       
    return id1

data = read_data('data/result.json')
print(find_all_users_id(data))