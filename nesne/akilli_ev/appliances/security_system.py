# security_system.py

from appliances.appliance import Appliance

class SecuritySystem(Appliance):
    def __init__(self, name):
        super().__init__(name)

    def activate_alarm(self):
        if self.status:
            print(f"{self.name} alarm aktif!")
        else:
            print(f"{self.name} kapalı, alarm çalışmaz.")
