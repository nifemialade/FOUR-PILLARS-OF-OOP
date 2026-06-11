class Car:
    def show_information(self):
        print("This is a car. It drives on roads.")


class Plane:
    def show_information(self):
        print("This is a plane. It flies in the sky.")


class Ship:
    def show_information(self):
        print("This is a ship. It sails on water.")


vehicles = [Car(), Plane(), Ship()]

for vehicle in vehicles:
    vehicle.show_information()