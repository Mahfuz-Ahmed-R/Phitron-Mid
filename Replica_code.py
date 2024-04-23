class Show:
    def __init__(self, id, movie_name, show_time):
        self.id = id
        self.movie_name = movie_name
        self.show_time = show_time

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, show_time):
        show_info = (id, movie_name, show_time)
        self.show_list.append(show_info)
        self.seats[id] = [['free'] * self.cols for _ in range(self.rows)]

    def view_available_seats(self, id):
        if id in self.seats:
            print(f"\nAvailable seats for show {id}:")
            for row in self.seats[id]:
                print(" ".join(row))
        else:
            print(f"Show ID {id} does not exist.")

    def book_seats(self, id, seat_list):
        if id in self.seats:
            for row, col in seat_list:
                if  row <= self.rows and col <= self.cols:
                    if self.seats[id][row - 1][col - 1] == 'free':
                        self.seats[id][row - 1][col - 1] = 'booked'
                        print(f"\nSeat ({row}, {col}) booked successfully.")
                    elif row >= 0 and col >= 0:
                        print(f"Sorry, Seat ({row}, {col}) is nowhere. :(")
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Invalid seat ({row}, {col}).")
        else:
            print(f"Show ID {id} does not exist.")

class Counter:
    def __init__(self):
        self.hall_list = []

    def add_hall(self, hall):
        self.hall_list.append(hall)

class Counter:
    def __init__(self):
        self.hall_list = []

    def add_hall(self, hall):
        self.hall_list.append(hall)

    def view_running_shows(self):
        print("Running shows:")
        for hall in self.hall_list:
            for id, movie_name, show_time in hall.show_list:
                print(f"Show ID: {id}, Movie: {movie_name}, Time: {show_time}")



counter = Counter()

hall1 = Hall(rows=7, cols=7, hall_no=1)
hall1.entry_show(id='969', movie_name='Avatar', show_time='11:00')
hall1.entry_show(id='696', movie_name='Dune', show_time='15:30')

hall2 = Hall(rows=7, cols=7, hall_no=2)
hall2.entry_show(id='888', movie_name='Avatar 2', show_time='13:00')
hall2.entry_show(id='777', movie_name='Dune 2', show_time='18:30')

counter.add_hall(hall1)
counter.add_hall(hall2)

counter.view_running_shows()
hall1.view_available_seats(id='969')
hall1.book_seats(id='969', seat_list=[(5, 5), (6, 6), (7, 7)])

hall2.view_available_seats(id='777')
hall2.book_seats(id='777', seat_list=[(5, 5), (6, 6), (7, 7)])


