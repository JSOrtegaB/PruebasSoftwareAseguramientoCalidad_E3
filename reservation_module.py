"""
Reservation Module to handle hotel room bookings for customers
"""
from datetime import datetime
from database_module import FileManager  # pylint: disable=import-error
from hotel_module import HotelManager  # pylint: disable=import-error
from customer_module import CustomerManager  # pylint: disable=import-error


# pylint: disable=R0913
class Reservation:
    """
    Reservation Class to handle hotel room bookings for customers
    """
    reservations_file = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id,
                 room_number, start_date, end_date):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def save_reservation(self):
        """
        Method to save the reservation details
        """
        reservations = FileManager.read_file(Reservation.reservations_file)
        reservations[self.reservation_id] = self.__dict__
        FileManager.write_file(Reservation.reservations_file, reservations)

    @staticmethod
    def create_reservation(customer_id, hotel_id,
                           room_number, start_date, end_date):
        """
        Static method to create a reservation
        """
        # Generate a unique reservation ID
        reservation_id = (f"R-{datetime.now().strftime('%Y%m%d%H%M%S')}"
                          f"-{customer_id}-{hotel_id}")

        # Reserve the room
        result, message = HotelManager.reserve_room(hotel_id)
        if not result:
            return False, message

        # Create Reservation instance
        reservation = Reservation(reservation_id, customer_id,
                                  hotel_id, room_number, start_date, end_date)
        reservation.save_reservation()

        # Update customer reservations
        customer = CustomerManager.get_customer(customer_id)
        if customer:
            customer_reservations = customer['reservations']
            customer_reservations[reservation_id] = {
                "hotel_id": hotel_id,
                "room_number": room_number,
                "start_date": start_date,
                "end_date": end_date
            }
            CustomerManager.modify_customer(customer_id,
                                            reservations=customer_reservations)
        else:
            return False, "Customer not found."

        return True, f"Reservation {reservation_id} created successfully."

    @staticmethod
    def cancel_reservation(reservation_id):
        """
        Static method to cancel a reservation
        """
        reservations = FileManager.read_file(Reservation.reservations_file)
        reservation = reservations.get(reservation_id)
        if reservation:
            # Cancel room reservation
            result, message = HotelManager.cancel_room(
                reservation['hotel_id'],
                reservation['room_number'])
            if not result:
                return False, message

            # Remove reservation from customer records
            customer = CustomerManager.get_customer(reservation['customer_id'])
            if customer and reservation_id in customer['reservations']:
                del customer['reservations'][reservation_id]
                CustomerManager.modify_customer(
                    reservation['customer_id'],
                    reservations=customer['reservations'])

            # Delete reservation record
            del reservations[reservation_id]
            FileManager.write_file(Reservation.reservations_file,
                                   reservations)

            return True, (f"Reservation {reservation_id} "
                          f"cancelled successfully.")
        return False, "Reservation not found."
