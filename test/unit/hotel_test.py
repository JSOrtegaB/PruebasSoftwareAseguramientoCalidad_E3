"""
Modulo de prueba para la clase HotelManager
"""
import unittest
from hotel_module import Hotel, HotelManager




class TestHotelManager(unittest.TestCase):
    """
    This is a test class for the HotelManager. It contains unit tests for all the 
    methods in the HotelManager class.
    """
    def test_create_hotel(self):
        """
        Test method for the create_hotel method of the HotelManager class.
        """
        hotel = Hotel("1", "Test Hotel", "Test Location", 500)
        HotelManager.create_hotel(hotel)
       
if __name__ == "__main__":
    unittest.main()