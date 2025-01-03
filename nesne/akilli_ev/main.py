# main.py

from appliances.light import Light
from appliances.thermostat import Thermostat
from appliances.security_system import SecuritySystem

def main():
    light = Light("Salon Işığı")
    thermostat = Thermostat("Ev Termostatı")
    security = SecuritySystem("Güvenlik Sistemi")

    while True:
        print("\n1. Işığı Aç")
        print("2. Işığı Kapat")
        print("3. Işığı Kıs")
        print("4. Termostatı Aç")
        print("5. Termostatı Kapat")
        print("6. Sıcaklık Ayarla")
        print("7. Güvenlik Sistemini Aç")
        print("8. Güvenlik Sistemini Kapat")
        print("9. Alarmı Aktifleştir")
        print("0. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            light.turn_on()
        elif choice == "2":
            light.turn_off()
        elif choice == "3":
            light.dim()
        elif choice == "4":
            thermostat.turn_on()
        elif choice == "5":
            thermostat.turn_off()
        elif choice == "6":
            temp = int(input("Sıcaklık değeri girin: "))
            thermostat.set_temperature(temp)
        elif choice == "7":
            security.turn_on()
        elif choice == "8":
            security.turn_off()
        elif choice == "9":
            security.activate_alarm()
        elif choice == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
