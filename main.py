
import Data
import os
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

size = os.get_terminal_size()
width = size.columns

user = None # user instance

def printAcountPage():
    '''
    Displays the account page with options:
    1. Login
    2. Register
    3. Exit
    '''
    print(YELLOW+ "Cinema Booking Program".center(width))
    print(CYAN+"—" * width)
    string:str = ""
    string += "1. Login\n2. Register\n3. Exit"
    print(string)
    print("—" * width+RESET)

def printHomePage():
    '''
    Displays the home page for a logged-in user with options:
    1. Book a ticket
    2. Cancel a ticket
    3. View all seats
    4. View my seats
    5. View seat statistics
    6. Logout
    '''
    string:str = ""
    string += "1. Book a ticket\n2. Cancel a ticket\n3. View all seats\n4. View my seats\n5. Statistics\n6. Logout"
    print(MAGENTA+ "—" * width)
    print(string)
    print("—" * width + RESET)

def printAllBookedSeats():
    '''
    Displays the seating chart of the cinema hall.
    ▢ represents an available seat.
    ▣ represents a booked seat.
    Row and seat numbers are displayed for reference.
    '''
    print("  ", end="")
    for j in range(1, 21):
        s = str(j)
        if len(s) > 1:
            print(j, end=" ")
        else:
            print(j, end="  ")
            
    print()
    print()
    for i in range(1, 11):
        print("|", end=" ")
        for j in range(1, 21):
            if Data.isAvailable(i, j):
                print("▢", end="  ")
            else:
                print("▣", end="  ")
                
        print(f"|   {i}")
        
    print(RESET)
     
def printMySeats():
    '''
    Displays the list of seats booked by the currently logged-in user.
    If no seats are booked, prints 'Empty'.
    '''
    if len(user["seats"]) == 0: print("Empty")
    for i in user["seats"]:
        print(i)
        
# rogester page
def rigisterPage():
    '''
    Displays the registration page.
    Prompts the user to enter a username and password.
    Validates that the username is unique and the password is at least 8 characters long.
    Returns the newly created user data as a dictionary if successful.
    '''
    while True:
        user_name = input("user_name: ")
        
        users = Data.getUsers()
        con = True
        for i in users:
            if i["username"] == user_name:
                print(RED + "This username already exists. Please choose another one"+ RESET)
                con = False
        
        if not con: continue
        
        password = input("password: ")
        if len(password) < 8:
            print(RED + " Your password must be at least 8 characters. Please try again"+ RESET)
            continue
        
        user = {
            "username": user_name,
            "password": password,
            "seats": []
        }
        
        return user
  
# login page    
def loginPage():
    '''
    Displays the login page.
    Prompts the user to enter a username and password.
    Checks the credentials against existing user data.
    Returns True if the login is successful, otherwise False.
    '''
    while True:
        user_name = input("user_name: ")
        password = input("password: ")
        
        users = Data.getUsers()
        for i in users:
            if i["username"] == user_name and i["password"] == password:
                print(GREEN+"Welcome {}".format(user_name) + RESET)
                global user
                user = i
                return True
        
        print(RED + "Incorrect username or password. Please try again" + RESET)
        return False       
   
def bookTicketPage():
    '''
    Allows the user to book a seat.
    Prompts the user to enter the row and seat number.
    If the seat is available, reserves it and adds it to the user's booked seats.
    Displays appropriate success or error messages.
    '''
    row = int(input("row: "))
    seat = int(input("seat: "))
    
    if Data.bookASeats(row, seat):
        print(GREEN + "The seat was successfully reserved".center(width)+ RESET)
        user["seats"].append((row, seat))
    else:
        print(RED+"The seat is already reserved or not founded"+ RESET)
    
def CancelTicketPage():
    '''
    Allows the user to cancel a previously booked seat.
    Prompts the user to enter the row and seat number.
    Checks if the seat was booked by the user and cancels it if possible.
    Displays appropriate success or error messages.
    '''
    row = int(input("row: "))
    seat = int(input("seat: "))
    
    if not Data.isAvailable(row, seat):
        if (row, seat) in user["seats"]:
            if Data.cancelASeat(row, seat):
                print(GREEN + "The reservation was successfully canceled" + RESET)
        else:
            print(RED+"You do not have the authority to cancel this seat" + RESET)
    else:
        print(RED + "This seat is not booked" + RESET)

def culculate():
    '''
    Displays statistics about the cinema hall bookings:
    - Total number of booked seats.
    - Number of booked seats per row.
    '''
    print("total number of booked seats: " + str(len(Data.bookedSeats)))
    print("number of booked seats per row: ")
    for i in range(1, 11):
        counter = 0
        for j in range(1, 21):
            if (i, j) in Data.bookedSeats: counter += 1
        
        print(f"row {i} has {counter} booked seats")



# home page      
def homePage():
    '''
    The main home page for a logged-in user.
    Calls the cinema hall setup, displays options, and handles user choices:
    - Booking, canceling, viewing seats, checking statistics, or logging out.
    '''
    Data.createACinemaHall()
    
    user_input = 0
    while user_input != 6:
        printHomePage()
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            bookTicketPage()
        elif user_input == 2:
            CancelTicketPage()
        elif user_input == 3:
            printAllBookedSeats()
        elif user_input == 4:
            printMySeats()
        elif user_input == 5:
            culculate()
        elif user_input == 6:
            global user
            user = None
        else:
            print(RED + "Invalid input, please try again" + RESET)
            


# main --
# Main program loop that displays the account page and handles user input
# for logging in, registering, or exiting the program.
user_input = 0
while user_input != 3:
    printAcountPage()
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        if loginPage(): homePage()
    elif user_input == 2:
        user = rigisterPage()
        Data.addUser(user)
    elif user_input == 3: 
        print(YELLOW + "See you later!." + RESET)
        break
    else:
        print(RED + "Invalid input, please try again" + RESET)