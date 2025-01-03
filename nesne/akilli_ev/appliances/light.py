# light.py

from appliances.appliance import Appliance

class Light(Appliance):
    def __init__(self, name):
        super().__init__(name)

    def dim(self):
        if self.status:
            print(f"{self.name} ışığı kısıldı.")
        else:
            print(f"{self.name} kapalı, kısma işlemi yapılamaz.")
