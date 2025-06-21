

users = []
seats = []
bookedSeats = []


def addUser(user):
    '''
    Adds a new user to the users list.

    Args:
        user (dict): A dictionary containing user data (username, password, seats).
    """
    '''
    users.append(user)
    
def getUsers():
    '''
    Returns the list of all registered users.

    Returns:
        list: A list of user dictionaries.
    '''
    return users


def createACinemaHall():
    '''
    Creates a cinema hall layout with 10 rows and 20 seats per row.
    Populates the 'seats' list with tuples representing each seat (row, seat number).
    '''
    global seats
    for i in range(1, 11): # rows
        for j in range(1, 21): # seats
            seats.append((i, j))
            
def getAllSeats():
    '''
    Returns the list of all seats in the cinema hall.

    Returns:
        list: A list of seat position tuples (row, seat number).
    '''
    return seats

def bookASeats(row:int, seat:int):
    '''
    Books a seat if it's available and within valid cinema hall range.

    Args:
        row (int): The row number of the seat.
        seat (int): The seat number within the row.

    Returns:
        bool: True if the seat was successfully booked, False otherwise.
    '''
    global bookedSeats
    if row > 10 or seat > 20: return False
    for i in bookedSeats:
        if i[0] == row and i[1] == seat:
            return False

    bookedSeats.append((row, seat))
    return True
            
def cancelASeat(row:int, seat:int):
    '''
    Cancels a booked seat if it exists.

    Args:
        row (int): The row number of the seat.
        seat (int): The seat number within the row.

    Returns:
        bool: True if the seat was successfully canceled, False if not found.
    '''
    global bookedSeats
    for i in range(len(bookedSeats)):
        if bookedSeats[i][0] == row and bookedSeats[i][1] == seat:
            del bookedSeats[i] 
            return True
    
    return False
        
def isAvailable(row:int, seat:int):
    '''
    Checks if a seat is available (not booked).

    Args:
        row (int): The row number of the seat.
        seat (int): The seat number within the row.

    Returns:
        bool: True if the seat is available, False if it’s already booked.
    '''
    for i in bookedSeats:
        if i[0] == row and i[1] == seat:
            return False
        
    return True

        
        