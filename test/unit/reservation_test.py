"""Unit tests for the Reservation class in the reservation_module module."""
# pylint: disable=import-error
import unittest
from unittest.mock import patch
from reservation_module import Reservation


class TestReservation(unittest.TestCase):
    """ Test cases for the Reservation class. """

    def setUp(self):
        # Setup mock data for reservations
        self.reservation_id = "R-20240101123456-1-1"
        self.customer_id = 1
        self.hotel_id = 1
        self.room_number = "101"
        self.start_date = "2024-01-01"
        self.end_date = "2024-01-05"
        self.reservation = Reservation(self.reservation_id,
                                       self.customer_id, self.hotel_id,
                                       self.room_number, self.start_date,
                                       self.end_date)

    @patch('reservation_module.FileManager.write_file')
    @patch('reservation_module.FileManager.read_file')
    def test_save_reservation(self, mock_read, mock_write):
        """ Test method for saving a reservation."""
        mock_read.return_value = {}
        self.reservation.save_reservation()
        mock_write.assert_called_once()
        args, _ = mock_write.call_args
        self.assertEqual(args[0], Reservation.reservations_file)
        self.assertTrue(self.reservation_id in args[1])

    @patch('reservation_module.CustomerManager.modify_customer')
    @patch('reservation_module.CustomerManager.get_customer')
    @patch('reservation_module.HotelManager.reserve_room')
    @patch('reservation_module.Reservation.save_reservation')
    def test_create_reservation(self, mock_save, mock_reserve,
                                mock_get_customer, mock_modify_customer):
        """ Test method for creating a reservation."""
        mock_reserve.return_value = (True, "Room reserved successfully")
        mock_get_customer.return_value = {'reservations': {}}
        result, message = Reservation.create_reservation(self.customer_id,
                                                         self.hotel_id,
                                                         self.room_number,
                                                         self.start_date,
                                                         self.end_date)
        self.assertTrue(result)
        self.assertIn("created successfully", message)
        mock_save.assert_called_once()
        mock_modify_customer.assert_called_once()

    @patch('reservation_module.FileManager.write_file')
    @patch('reservation_module.FileManager.read_file')
    @patch('reservation_module.HotelManager.cancel_room')
    @patch('reservation_module.CustomerManager.modify_customer')
    @patch('reservation_module.CustomerManager.get_customer')
    # pylint: disable=unused-argument
    # pylint: disable=R0913
    def test_cancel_reservation(self, mock_get_customer,
                                mock_modify_customer,
                                mock_cancel_room,
                                mock_read, mock_write):
        """ Test method for cancelling a reservation."""
        mock_read.return_value = {
            self.reservation_id: self.reservation.__dict__
        }
        mock_cancel_room.return_value = (True, "Room cancellation successful")
        mock_get_customer.return_value = {
            "reservations": {
                self.reservation_id: {}
            }
        }
        result, message = Reservation.cancel_reservation(self.reservation_id)
        self.assertTrue(result)
        self.assertIn("cancelled successfully", message)
        mock_write.assert_called_once()


if __name__ == '__main__':
    unittest.main()
