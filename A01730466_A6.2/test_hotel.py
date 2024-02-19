"""Unit Test for hotel.py
"""


import unittest
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Hotel Test Cases."""
    def setUp(self):
        # Clear the hotels_data before each test
        Hotel.hotels_data.clear()
        self.hotel = Hotel.create_hotel(
            "H01", 'Test Hotel 1', 'Test Loc 1', 13)

    def test_create_hotel(self):
        """Test the creation of a hotel."""
        self.assertEqual(self.hotel.hotel_id, "H01")
        self.assertEqual(self.hotel.name, 'Test Hotel 1')
        self.assertEqual(self.hotel.location, 'Test Loc 1')
        self.assertEqual(self.hotel.rooms_free, 13)

    def test_display_info(self):
        """Test displaying hotel information."""
        expected_output = ("Hotel Name: Test Hotel 1, Location: Test Loc 1, "
                           "Rooms Available: 13")
        self.assertEqual(
            self.hotel.display_info().strip(), expected_output.strip())

    def test_modify_info(self):
        """Test modifying hotel information."""
        self.hotel.modify_info(
            name='New Hotel 1', location='New Location 1', rooms_free=11)
        self.assertEqual(self.hotel.name, 'New Hotel 1')
        self.assertEqual(self.hotel.location, 'New Location 1')
        self.assertEqual(self.hotel.rooms_free, 11)

    def test_reserve_room(self):
        """Test reserving a room."""
        result = self.hotel.reserve_room()
        self.assertTrue(result)
        self.assertEqual(self.hotel.rooms_free, 12)

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        self.hotel.reserve_room()  # Reserve a room first
        self.hotel.cancel_reservation()
        self.assertEqual(self.hotel.rooms_free, 13)

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        self.hotel.delete_hotel()
        self.assertNotIn(self.hotel.hotel_id, Hotel.hotels_data)

    # Negative Test Cases
    def test_reserve_full_room(self):
        """Test reserving a room when is full."""
        self.hotel.rooms_free = 0
        result = self.hotel.reserve_room()
        self.assertFalse(result)

    def test_create_hotel_negative_rooms(self):
        """Creating a hotel with negative rooms."""
        with self.assertRaises(ValueError):
            Hotel("H02", "Test Hotel 2", "Test Location 2", -1)

    def test_modify_invalid_rooms(self):
        """Modifying hotel info with negative rooms."""
        with self.assertRaises(ValueError):
            self.hotel.modify_info(
                name='New Hotel 1', location='New Location 1', rooms_free=-1)

    def test_add_hotel_with_duplicate_id(self):
        """Adding a hotel with a duplicate ID."""
        Hotel.create_hotel("H011", "Duplicate Hotel", "Duplicate Location", 11)
        with self.assertRaises(ValueError):
            Hotel.create_hotel(
                "H011", "Duplicate Hotel", "Duplicate Location", 11)


if __name__ == '__main__':
    unittest.main()
