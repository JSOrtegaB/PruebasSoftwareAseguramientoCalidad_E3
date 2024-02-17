"""
class CustomerManager:
customers_file = "customers.json"

    @staticmethod
    def create_customer(customer):
        customers = FileManager.read_file(CustomerManager.customers_file)
        customers[customer.customer_id] = customer.__dict__
        FileManager.write_file(CustomerManager.customers_file, customers)

    # Additional methods for delete, display, and modify

class ReservationManager:
reservations_file = "reservations.json"

    @staticmethod
    def create_reservation(reservation):
        reservations = FileManager.read_file(ReservationManager.reservations_file)
        reservations[reservation.reservation_id] = reservation.__dict__
        FileManager.write_file(ReservationManager.reservations_file, reservations)

    # Additional method for cancel

"""
