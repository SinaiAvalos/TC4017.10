"""Hotel module.
"""


class Hotel:
    """
    Represents a hotel with attributes:
    ID, name, location, and available rooms.
    """

    # Class variable to store all hotels data
    hotels_data = {}

    def __init__(self, hotel_id, name, location, rooms_free):
        """
        Initializes a new Hotel object.
        """
        if rooms_free < 0:
            raise ValueError("rooms_free must be non-negative")
        if hotel_id in self.hotels_data:
            raise ValueError("hotel_id must be unique")
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_free = rooms_free
        # Add hotel data to the class variable
        self.hotels_data[hotel_id] = {
            "name": name,
            "location": location,
            "rooms_free": rooms_free
        }

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms_free):
        """
        Creates a new Hotel object and adds it to the hotels_data.
        """
        hotel = cls(hotel_id, name, location, rooms_free)

        return hotel

    def display_info(self):
        """
        Displays hotel information.
        """
        hotel_info = (f"Hotel Name: {self.name}, Location: {self.location}, "
                      f"Rooms Available: {self.rooms_free}")

        print(f"\n{hotel_info} \n")  # Print hotel information
        return hotel_info  # Return hotel information as a string

    def modify_info(self, name=None, location=None, rooms_free=None):
        """
        Modifies the information of the hotel.
        """
        if name:
            self.name = name
            self.hotels_data[self.hotel_id]["name"] = name
        if location:
            self.location = location
            self.hotels_data[self.hotel_id]["location"] = location
        if rooms_free >= 0:
            self.rooms_free = rooms_free
            self.hotels_data[self.hotel_id]["rooms_free"] = rooms_free
        else:
            raise ValueError("rooms_free must be non-negative")

    def reserve_room(self):
        """
        Reserves a room in the hotel.
        """
        if self.rooms_free > 0:
            self.rooms_free -= 1
            self.hotels_data[self.hotel_id]["rooms_free"] -= 1
            return True
        return False

    def cancel_reservation(self):
        """
        Cancels a reservation by incrementing the number of free rooms.
        """
        self.rooms_free += 1
        self.hotels_data[self.hotel_id]["rooms_free"] += 1

    def delete_hotel(self):
        """
        Delete the hotel's data from the data table.
        """
        if self.hotel_id in self.hotels_data:
            del self.hotels_data[self.hotel_id]
            print(f"Hotel '{self.name}' deleted successfully.")
        else:
            raise ValueError(f"Hotel with ID \
                        '{self.hotel_id}' not found and cannot be deleted.")
