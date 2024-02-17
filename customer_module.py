""""
Customer Module
"""
from database_module import FileManager  # pylint: disable=import-error


class Customer:
    """
    Customer Class to create customer objects
    """
    def __init__(self, customer_id, name, email, reservations):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.reservations = reservations  # Dictionary of reservations

    def display_info(self):
        """
        Method to display customer information
        """
        return (f"Customer ID: {self.customer_id}, Name: {self.name}, "
                f"Email: {self.email}, Reservations: {self.reservations}"
                )

    def update_email(self, new_email):
        """
        Method to update the customer's email
        """
        self.email = new_email


class CustomerManager:
    """
    Helper class to manage customer objects
    """
    customers_file = "customers.json"

    @staticmethod
    def create_customer(customer):
        """
        Method to create a customer and store their details
        """
        customers = FileManager.read_file(CustomerManager.customers_file)
        customers[customer.customer_id] = customer.__dict__
        FileManager.write_file(CustomerManager.customers_file, customers)

    @staticmethod
    def delete_customer(customer_id):
        """
        Method to delete a customer by their ID
        """
        customers = FileManager.read_file(CustomerManager.customers_file)
        if customer_id in customers:
            del customers[customer_id]
            FileManager.write_file(CustomerManager.customers_file, customers)
            return True
        return False

    @staticmethod
    def modify_customer(customer_id, name=None, email=None, reservations=None):
        """
        Method to modify an existing customer's details
        """
        customers = FileManager.read_file(CustomerManager.customers_file)
        if customer_id in customers:
            if name is not None:
                customers[customer_id]['name'] = name
            if email is not None:
                customers[customer_id]['email'] = email
            if reservations is not None:
                customers[customer_id]['reservations'] = reservations
            FileManager.write_file(CustomerManager.customers_file, customers)
            return True
        return False

    @staticmethod
    def get_customer(customer_id):
        """
        Method to retrieve a customer's details by their ID
        """
        customers = FileManager.read_file(CustomerManager.customers_file)
        customer = customers.get(customer_id)
        if customer:
            return customer
        return None
