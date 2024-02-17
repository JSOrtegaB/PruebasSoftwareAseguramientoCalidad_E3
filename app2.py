from customer_module import CustomerManager, Customer  # pylint: disable=import-error
from reservation_module import Reservation
from hotel_module import HotelManager, Hotel


#new_customer = Customer("1", "Juan Ortega", "juan@email.com", {101:True})
#customer = CustomerManager.create_customer(new_customer)
#print(customer)


#hotel = Hotel("3", "Hotel California", "California", 100)

#print(HotelManager.create_hotel(hotel))

#print(HotelManager.reserve_room("1"))

cancel = Reservation.cancel_reservation("R-20240217091916-1-1")
#reservation = Reservation.create_reservation("1", "1", "101", "2024-01-01", "2024-01-05")
print(cancel)