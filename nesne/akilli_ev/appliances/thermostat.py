# thermostat.py

from appliances.appliance import Appliance

class Thermostat(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 20

    def set_temperature(self, temp):
        if self.status:
            self.temperature = temp
            print(f"{self.name} sıcaklık {temp} derece olarak ayarlandı.")
        else:
            print(f"{self.name} kapalı, sıcaklık ayarlanamaz.")
