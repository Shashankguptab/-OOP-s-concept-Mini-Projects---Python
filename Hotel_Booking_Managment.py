"""
Hotel Booking System

Class: Room (room_number, price, availability).

Class: Hotel to manage multiple rooms.

Class: Reservation for booking details.
"""


class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_available = True

    def __str__(self):
        return (
            f"Room {self.room_number}-{'Available' if self.is_available else 'Booked'}"
        )


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_room(self):
        for room in self.rooms:
            print(room)

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                room.is_available = False
                print(f"{room_number}booked successfully")
                return
        print("Room is not available!!")


# example output
hotel = Hotel("Brindavan Hotel")
hotel.add_room(Room(101, 1500))
hotel.add_room(Room(102, 2000))

hotel.book_room(101)
hotel.show_room()
