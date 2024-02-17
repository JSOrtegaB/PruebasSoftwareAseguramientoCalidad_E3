"""
Hotel Test Module
"""
import unittest
from unittest.mock import patch
from customer_module import Customer, CustomerManager


class TestCustomer(unittest.TestCase):
    """
    Class to test the customer class
    """
    def setUp(self):
        """
        Set up method
        """
        self.customer = Customer('123',
                                 'John Doe',
                                 'johndoe@example.com',
                                 {'res1': 'Reservation 1'})

    def test_display_info(self):
        """
        Test method to display customer information
        """
        expected_info = "Customer ID: 123, Name: John Doe, Email:" \
            " johndoe@example.com, Reservations: {'res1': 'Reservation 1'}"

        self.assertEqual(self.customer.display_info(), expected_info)

    def test_update_email(self):
        """
        Test method to update email
        """
        new_email = 'newemail@example.com'
        self.customer.update_email(new_email)
        self.assertEqual(self.customer.email, new_email)


class TestCustomerManager(unittest.TestCase):
    """
    Customer testmanager class
    """
    def setUp(self):
        self.customer_data = {'123': {'customer_id': '123',
                                      'name': 'John Doe',
                                      'email': 'johndoe@example.com',
                                      'reservations':
                                      {'res1': 'Reservation 1'}}}

    @patch('customer_module.FileManager.read_file', return_value={})
    @patch('customer_module.FileManager.write_file')
    # pylint: disable=unused-argument
    def test_create_customer(self, mock_write_file, mock_read_file):
        """
        test method to create customer
        """
        customer = Customer('123',
                            'John Doe',
                            'johndoe@example.com',
                            {'res1': 'Reservation 1'})
        CustomerManager.create_customer(customer)
        mock_write_file.assert_called_once()
        args = mock_write_file.call_args[0]
        self.assertEqual(args[0], CustomerManager.customers_file)
        self.assertIn('123', args[1])

    @patch('customer_module.FileManager.read_file')
    @patch('customer_module.FileManager.write_file')
    def test_delete_customer(self, mock_write_file, mock_read_file):
        """
        Test method to delete customer
        """
        mock_read_file.return_value = self.customer_data
        result = CustomerManager.delete_customer('123')
        self.assertTrue(result)
        mock_write_file.assert_called_once()

    @patch('customer_module.FileManager.read_file')
    @patch('customer_module.FileManager.write_file')
    def test_modify_customer(self, mock_write_file, mock_read_file):
        """
        Test method to modify customer
        """
        mock_read_file.return_value = self.customer_data
        result = CustomerManager.modify_customer('123',
                                                 email='newemail@example.com')
        self.assertTrue(result)
        mock_write_file.assert_called_once()

    @patch('customer_module.FileManager.read_file')
    def test_get_customer(self, mock_read_file):
        """
        Test method to get customer
        """
        mock_read_file.return_value = self.customer_data
        customer = CustomerManager.get_customer('123')
        self.assertIsNotNone(customer)
        self.assertEqual(customer['email'], 'johndoe@example.com')


if __name__ == '__main__':
    unittest.main()
