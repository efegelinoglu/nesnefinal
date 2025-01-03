# appliance.py

from appliances.controllable import Controllable

class Appliance(Controllable):
    def __init__(self, name):
        self.name = name
        self.status = False

    def turn_on(self):
        self.status = True
        print(f"{self.name} açıldı.")

    def turn_off(self):
        self.status = False
        print(f"{self.name} kapandı.")

    def is_on(self):
        return self.status
