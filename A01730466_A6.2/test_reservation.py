"""Unit Test for reservation.py
"""


import unittest
from reservation import Reservation


class TestReservation(unittest.TestCase):
    """Reservation Test Cases."""
    def setUp(self):
        """
        Setup method to run before each test.
        """
        Reservation.reservations_data.clear()

    def test_create_reservation(self):
        """
        Test creating a reservation.
        """
        reservation_id = "R01"
        customer_id = "C01"
        hotel_id = "H01"
        total_guest = 2

        reservation = Reservation.create_reservation(
            reservation_id, customer_id, hotel_id, total_guest)

        self.assertIsInstance(reservation, Reservation)
        self.assertIn(reservation_id, Reservation.reservations_data)
        self.assertEqual(Reservation.reservations_data[reservation_id], {
            "customer_id": customer_id,
            "hotel_id": hotel_id,
            "total_guest": total_guest
        })

    def test_cancel_reservation(self):
        """
        Test canceling a reservation.
        """
        reservation_id = "R02"
        customer_id = "C02"
        hotel_id = "H02"
        total_guest = 3

        # Create and then cancel the reservation
        reservation = Reservation.create_reservation(
            reservation_id, customer_id, hotel_id, total_guest)
        reservation.cancel_reservation()

        self.assertNotIn(reservation_id, Reservation.reservations_data)

    def test_reservation_data_integrity(self):
        """
        Test the integrity of the data stored in a reservation.
        """
        reservation_id = "R03"
        customer_id = "C03"
        hotel_id = "H03"
        total_guest = 4

        reservation = Reservation.create_reservation(
            reservation_id, customer_id, hotel_id, total_guest)

        self.assertEqual(reservation.reservation_id, reservation_id)
        self.assertEqual(reservation.customer_id, customer_id)
        self.assertEqual(reservation.hotel_id, hotel_id)
        self.assertEqual(reservation.total_guest, total_guest)


if __name__ == '__main__':
    unittest.main()
