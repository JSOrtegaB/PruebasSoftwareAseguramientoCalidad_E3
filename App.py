from hotel_module import Hotel, HotelManager

hotel1 = Hotel("1", "Para borrar", "cancun", {100:True, 101:False, 102:False, 103:False})
hotel2 = Hotel("2", "Hotel Grand", "cancun", {1000:False, 1001:False, 1002:False, 1003:False})
HotelManager.create_hotel(hotel1)
HotelManager.create_hotel(hotel2)
print(HotelManager.get_hotel("1"))
# print(HotelManager.get_hotel("2"))

# HotelManager.delete_hotel("1")


HotelManager.modify_hotel("2", "Hotel Grand", "cancun", {100:False, 101:False, 102:False, 103:False})
print(HotelManager.get_hotel("2"))

print(HotelManager.get_reserved_rooms("1"))
