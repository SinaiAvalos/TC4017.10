"""Reservation module.
"""


class Reservation:
    """
    Represents a reservation with attributes:
    reservation ID, customer ID, hotel ID, and number of guests.
    """

    # Class variable to store all reservations' data
    reservations_data = {}

    def __init__(self, reservation_id, customer_id, hotel_id, total_guest):
        """
        Initializes a new Reservation object.
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.total_guest = total_guest
        # Add reservation data to the class variable
        self.reservations_data[reservation_id] = {
            "customer_id": customer_id,
            "hotel_id": hotel_id,
            "total_guest": total_guest
        }

    @classmethod
    def create_reservation(
            cls, reservation_id, customer_id, hotel_id, total_guest):
        """
        Creates a new Reservation object.
        """
        reservation = cls(reservation_id, customer_id, hotel_id, total_guest)
        return reservation

    def cancel_reservation(self):
        """
        Cancel the reservation.
        """
        if self.reservation_id in self.reservations_data:
            del self.reservations_data[self.reservation_id]
            print("Reservation canceled successfully.")
        else:
            print("Reservation data not found.")
