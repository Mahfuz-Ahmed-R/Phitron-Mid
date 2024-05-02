import os
#1. Make a class named Star_Cinema which will have one class attribute named hall_list which is an empty list initially. Make a method named entry_hall() to insert an object of class Hall (Described below) inside its hall_list. 	

class Star_Cinema:
    def __init__(self, rows, cols, hall_no):
        hall_obj = Hall(rows, cols, hall_no)
        self._hall_list = [hall_obj]

    def entry_hall(self, halls):
        self._hall_list.append(halls)


#2. Make a class named Hall which will have 5 instance attributes given below	
# seats which is an dictionary of seats information
# show_list which is an list of tuples
# rows which is the row of the seats in that hall
# cols which is the column of the seats in that hall
# hall_no which is the unique no. of that hall

# Initialize an object of class Hall with rows, cols and hall_no. And insert that object to the Star_Cinema class attribute named hall_list inside the initializer using inheritance. seats and show_list will be empty initially.
class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no


#3. Make a method in Hall class named entry_show() which will take id, movie_name and time in string format. Make a tuple with all of the information and append it to the show_list attribute. Allocate seats with rows and cols using 2d list, initially all seats will be free. Make a key with id to the attribute seats and value will be the 2d list.
    def entry_show(self, id, movie_name, time):
        show_details = (id, movie_name, time)
        self._show_list.append(show_details)
        self._seats[id] = [['0'] * self._cols for _ in range(self._rows)]

#4. Make a method in Hall class named book_seats() which will take an id of the show and list of tuples where every tuple contains the row and col of the seat. You need to check the id of the show, and book the seats. 
    def book_seats(self, id, total_seats):
        if id in self._seats:
            for row, col in total_seats:
                if  row <= self._rows and col <= self._cols:
                    if self._seats[id][row - 1][col - 1] == '0':
                        self._seats[id][row - 1][col - 1] = '*'
                        print(f"Congratulaitons, Seat ({row}, {col}) booked successfully!!!")
                    elif row >= 0 and col >= 0:
                        print(f"Sorry, Seat ({row}, {col}) is nowhere. :(")
                    else:
                        print(f"Sorry, Seat ({row}, {col}) is already booked. :(")
                else:
                    print(f"Invalid seat ({row}, {col}).")
        else:
            print(f"ID {id} not exist.")

#5. Make a method in Hall class named view_show_list() which will view all the shows running.
    def view_show_list(self):
        print("Currently running shows:")
        for i in self._show_list:
            print(f"ID: {i[0]}, Movie: {i[1]}, Time: {i[2]}")

#6. Make a method in Hall class named view_available_seats() which will take an id of show, and view the seats that are available in that show	
    def view_available_seats(self, id):
        if id in self._seats:
            print(f"Available seats for show {id}:")
            for row in self._seats[id]:
                print(" ".join(row))
        else:
            print(f"Show ID {id} does not exist.")


# Execution

cinema = Star_Cinema(7, 7, 1)


hall = cinema._hall_list[0]
hall.entry_show(1, "Avatar", "11:00")
hall.entry_show(2, "Avatar 2", "15:00")
hall.entry_show(3, "Dune", "18:00")
hall.entry_show(4, "Dune 2", "09:00")

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("Choose any of the options from below: ")
    print("1 : View the running shows")
    print("2 : View the available seats")
    print("3 : Book a ticket/tickets")
    print("4 : Exit")
    inputt = int(input("Enter the option: "))
    if inputt == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        hall.view_show_list()
        print("----x------x------x----")
        print("----x------x------x----")
    elif inputt == 2:
        id = int(input("Enter the show's ID: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        hall.view_available_seats(id)
        print("----x------x------x----")
        print("----x------x------x----")
    elif inputt == 3:
        id = int(input("Enter the show's ID: "))
        tic = int(input("Number of tickets: "))
        seat_list = []
        for i in range(tic):
            print("Ticket no:", i+1)
            r1 = int(input("Enter the row: "))
            c1 = int(input("Enter the column: "))
            seat_list.append((r1, c1))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        hall.book_seats(id, seat_list)
        print("----x------x------x----")
        print("----x------x------x----")
    elif inputt == 4:
        break
