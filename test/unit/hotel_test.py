"""
Hotel Test Module
"""
import unittest
from unittest.mock import patch
from hotel_module import Hotel, HotelManager # pylint: disable=import-error


sample_hotels = {
    "1": {
        "hotel_id": "1",
        "name": "Test Hotel",
        "location": "Test Location",
        "rooms": {
            "100": False,
            "101": True
        }
    }
}


class TestHotelManager(unittest.TestCase):
    """
    Hotel testmanager class
    """
    def setUp(self):
        self.sample_hotels = {
            "1": {
                "hotel_id": "1",
                "name": "Test Hotel",
                "location": "Test Location",
                "rooms": {"100": False, "101": True}
            }  # True indicates the room is reserved
        }
        self.hotel = Hotel("1", "Test Hotel", "Test Location",
                           {"100": False, "101": True})

    def test_create_hotel(self):
        """
        Test mathod to create hotel
        """
        @patch('hotel_module.FileManager.write_file')
        @patch('hotel_module.FileManager.read_file', return_value={})
        #  pylint: disable=unused-argument
        def test_create_hotel(self, mock_read_file, mock_write_file):
            HotelManager.create_hotel(self.hotel)
            HotelManager.create_hotel(self.hotel)
            mock_write_file.assert_called_once()
            args, _ = mock_write_file.call_args
            hotels_data = args[1]
            self.assertIn(self.hotel.hotel_id, hotels_data)

    @patch('hotel_module.FileManager.write_file')
    @patch('hotel_module.FileManager.read_file', return_value=sample_hotels)
    # pylint: disable=unused-argument
    def test_reserve_room(self, mock_read_file, mock_write_file):
        """
        Test mathod to reserve room
        """
        HotelManager.create_hotel(self.hotel)
        success, message = HotelManager.reserve_room("1")
        self.assertTrue(success)
        self.assertIn("reserved successfully", message)

    @patch('hotel_module.FileManager.write_file')
    @patch('hotel_module.FileManager.read_file', return_value=sample_hotels)
    # pylint: disable=unused-argument
    def test_cancel_room(self, mock_read_file, mock_write_file):
        """
        Test mathod to cancel a room
        """
        HotelManager.create_hotel(self.hotel)
        HotelManager.reserve_room("1")  # Ensure a room is reserved first
        success, message = HotelManager.cancel_room("1", "101")
        self.assertTrue(success)
        self.assertIn("cancelled successfully", message)

    @patch('hotel_module.FileManager.read_file', return_value=sample_hotels)
    # pylint: disable=unused-argument
    def test_get_reserved_rooms(self, mock_read_file):
        """
        Test mathod to get reserved rooms
        """
        HotelManager.create_hotel(self.hotel)
        result = HotelManager.get_reserved_rooms("1")
        self.assertIn("101", result)

    @patch('hotel_module.FileManager.read_file', return_value=sample_hotels)
    # pylint: disable=unused-argument
    def test_get_hotel(self, mock_read_file):
        """
        Test mathod to get hotel
        """
        HotelManager.create_hotel(self.hotel)
        # Test retrieving an existing hotel
        hotel = HotelManager.get_hotel("1")
        self.assertIsNotNone(hotel)
        # Test retrieving a non-existing hotel
        hotel = HotelManager.get_hotel("non_existing_id")
        self.assertIsNone(hotel)

    @patch('hotel_module.FileManager.read_file')
    @patch('hotel_module.FileManager.write_file')
    def test_delete_existing_hotel(self, mock_write_file, mock_read_file):
        """
        Test mathod to delete hotel
        """
        mock_read_file.return_value = {
            "1": {
                "hotel_id": "1",
                "name": "Test Hotel",
                "location": "Test Location",
                "rooms": {"100": False, "101": True}
            }
        }
        # Deleting the existing hotel
        result = HotelManager.delete_hotel("1")
        # Assert that FileManager.read_file was called once
        mock_read_file.assert_called_once_with(HotelManager.hotels_file)
        # Assert that FileManager.write_file was called once
        mock_write_file.assert_called_once_with(HotelManager.hotels_file, {})
        # Assert that the method returned True (success)
        self.assertTrue(result)

    @patch('hotel_module.FileManager.read_file')
    @patch('hotel_module.FileManager.write_file')
    def test_delete_non_existing_hotel(self, mock_write_file, mock_read_file):
        """
        Test mathod to delete non existing hotel
        """
        mock_read_file.return_value = {}

        # Deleting a non-existing hotel
        result = HotelManager.delete_hotel("1")

        # Assert that FileManager.read_file was called once
        mock_read_file.assert_called_once_with(HotelManager.hotels_file)

        # Assert that FileManager.write_file was not called
        mock_write_file.assert_not_called()

        # Assert that the method returned False (failure)
        self.assertFalse(result)

    @patch('hotel_module.FileManager.read_file')
    @patch('hotel_module.FileManager.write_file')
    def test_modify_existing_hotel(self, mock_write_file, mock_read_file):
        """
        Test mathod to modify hotel
        """
        # Mocking FileManager.read_file to return a dictionary with a hotel
        mock_read_file.return_value = {
            "1": {
                "hotel_id": "1",
                "name": "Test Hotel",
                "location": "Test Location",
                "rooms": {"100": False, "101": True}
            }
        }

        # Modifying the existing hotel's details
        result = HotelManager.modify_hotel(
            "1",
            name="New Name",
            location="New Location",
            rooms={"102": True}
        )
        # Assert that FileManager.read_file was called once
        mock_read_file.assert_called_once_with(HotelManager.hotels_file)

        # Assert that FileManager.write_file was
        # called once with the updated details
        mock_write_file.assert_called_once_with(HotelManager.hotels_file, {
            "1": {
                "hotel_id": "1",
                "name": "New Name",
                "location": "New Location",
                "rooms": {"102": True}
            }
        })

        # Assert that the method returned True (success)
        self.assertTrue(result)

    @patch('hotel_module.FileManager.read_file')
    @patch('hotel_module.FileManager.write_file')
    def test_modify_non_existing_hotel(self, mock_write_file, mock_read_file):
        """
        Test mathod to modify non existing hotel
        """
        # Mocking FileManager.read_file to return an empty dictionary
        mock_read_file.return_value = {}

        # Modifying a non-existing hotel's details
        result = HotelManager.modify_hotel("1",
                                           name="New Name",
                                           location="New Location",
                                           rooms={"102": True}
                                           )

        # Assert that FileManager.read_file was called once
        mock_read_file.assert_called_once_with(HotelManager.hotels_file)

        # Assert that FileManager.write_file was not called
        mock_write_file.assert_not_called()

        # Assert that the method returned False (failure)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
