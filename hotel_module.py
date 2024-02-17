"""
Hotel Module
"""
from database_module import FileManager  # pylint: disable=import-error


class Hotel:

    """
    Hotel Class to create hotel objects
    """
    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def display_info(self):
        """
        Method to display hotel information
        """
        return (f"Hotel ID: {self.hotel_id}, Name: {self.name}, "
                f"Location: {self.location}, Rooms: {self.rooms}"
                )

    def update_name(self, new_name):
        """
        Method to update the hotel name
        """
        self.name = new_name


class HotelManager:
    """
    Helper class to manage hotel objects
    """
    hotels_file = "hotels.json"

    @staticmethod
    def create_hotel(hotel):
        """
        Method to create a hotel
        """
        hotels = FileManager.read_file(HotelManager.hotels_file)
        hotels[hotel.hotel_id] = hotel.__dict__
        FileManager.write_file(HotelManager.hotels_file, hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        """
        Method to delete a hotel by its ID
        """
        hotels = FileManager.read_file(HotelManager.hotels_file)
        if hotel_id in hotels:
            del hotels[hotel_id]
            FileManager.write_file(HotelManager.hotels_file, hotels)
            return True  # Indicate success
        return False  # Indicate failure, hotel ID not found

    @staticmethod
    def modify_hotel(hotel_id, name=None, location=None, rooms=None):
        """
        Method to modify an existing hotel's details.
        """
        hotels = FileManager.read_file(HotelManager.hotels_file)
        if hotel_id in hotels:
            if name is not None:
                hotels[hotel_id]['name'] = name
            if location is not None:
                hotels[hotel_id]['location'] = location
            if rooms is not None:
                hotels[hotel_id]['rooms'] = rooms
            FileManager.write_file(HotelManager.hotels_file, hotels)
            return True  # Indicate success
        return False  # Indicate failure, hotel ID not found

    @staticmethod
    def get_hotel(hotel_id):
        """
        Method to retrieve a hotel's details by its ID.
        Returns the hotel details if found, otherwise returns None.
        """
        hotels = FileManager.read_file(HotelManager.hotels_file)
        hotel = hotels.get(hotel_id)
        if hotel:
            return hotel  # Return the hotel details
        return None  # Hotel ID not found

    @staticmethod
    def reserve_room(hotel_id):
        """Reserve a room in a specified hotel."""
        hotels = FileManager.read_file(HotelManager.hotels_file)
        hotel = hotels.get(hotel_id)
        if not hotel:
            return False, "Hotel not found."
        for room, available in hotel['rooms'].items():
            if not available:  # False means the room is available
                hotel['rooms'][room] = True  # Mark as reserved
                FileManager.write_file(HotelManager.hotels_file, hotels)
                return True, f"Room {room} reserved successfully."
        return False, "No available rooms."

    @staticmethod
    def cancel_room(hotel_id, room_number):
        """Cancel a room reservation in a specified hotel."""
        hotels = FileManager.read_file(HotelManager.hotels_file)
        hotel = hotels.get(hotel_id)
        if hotel and room_number in hotel['rooms']:
            if hotel['rooms'][room_number]:  # Room is reserved
                hotel['rooms'][room_number] = True  # Mark as available
                FileManager.write_file(HotelManager.hotels_file, hotels)
                return True, (f"Reservation for room "
                              f"{room_number} cancelled successfully."
                              )
            return False, "Room is not currently reserved."
        return False, "Hotel or room not found."

    @staticmethod
    def get_reserved_rooms(hotel_id):
        """Get a list of all reserved rooms for a specified hotel."""
        hotels = FileManager.read_file(HotelManager.hotels_file)
        hotel = hotels.get(hotel_id)
        if hotel:
            # Collect rooms that are reserved
            reserved_rooms = [room for room, is_reserved in
                              hotel['rooms'].items() if is_reserved]
            if reserved_rooms:
                return f"Reserved rooms: {', '.join(reserved_rooms)}"
            return "No rooms are currently reserved."
        return False, "Hotel not found."
