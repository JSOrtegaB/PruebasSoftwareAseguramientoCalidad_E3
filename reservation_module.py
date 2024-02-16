import json
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, customer_id, hotel_id, room_number, start_date, end_date):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def display_info(self):
        return (
            f"Reservation ID: {self.reservation_id}, Customer ID: {self.customer_id}, "
            f"Hotel ID: {self.hotel_id}, Room: {self.room_number}, Start: {self.start_date}, End: {self.end_date}"
        )