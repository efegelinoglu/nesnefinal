class Account:
    accounts = []

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        Account.accounts.append(self)
        Bank.track_transaction(f"Hesap olusturuldu: {account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatirildi. Yeni bakiye: {self.balance} TL")
            Bank.track_transaction(f"{self.account_number} hesabina {amount} TL yatirildi.")
        else:
            print("Gecersiz yatirma tutari.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL cekildi. Yeni bakiye: {self.balance} TL")
            Bank.track_transaction(f"{self.account_number} hesabindan {amount} TL cekildi.")
        else:
            print("Yetersiz bakiye veya gecersiz tutar.")

    def view_balance(self):
        print(f"Hesap Sahibi: {self.owner}")
        print(f"Hesap Numarasi: {self.account_number}")
        print(f"Bakiye: {self.balance} TL")

class Bank:
    transaction_history = []

    @staticmethod
    def display_bank_info():
        print(f"Bankamizda toplam {len(Account.accounts)} hesap bulunmaktadir.")
        print("Toplam islemler:")
        for transaction in Bank.transaction_history:
            print(transaction)

    @staticmethod
    def track_transaction(description):
        Bank.transaction_history.append(description)

if __name__ == "__main__":
    while True:
        print("\n--- Banka Hesap Yonetim Sistemi ---")
        print("1. Hesap Ac")
        print("2. Para Yatir")
        print("3. Para Cek")
        print("4. Bakiye Goruntule")
        print("5. Tum Hesaplari Goruntule")
        print("6. Cikis")
        
        secim = input("Lutfen bir secim yapiniz: ")
        
        if secim == "1":
            account_number = input("Hesap Numarasi: ")
            owner = input("Hesap Sahibi: ")
            balance = float(input("Baslangic Bakiyesi: "))
            Account(account_number, owner, balance)
            print("Hesap basariyla olusturuldu.")
        
        elif secim == "2":
            account_number = input("Hesap Numarasi: ")
            amount = float(input("Yatirilacak Tutar: "))
            for account in Account.accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Hesap bulunamadi.")
        
        elif secim == "3":
            account_number = input("Hesap Numarasi: ")
            amount = float(input("Cekilecek Tutar: "))
            for account in Account.accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Hesap bulunamadi.")
        
        elif secim == "4":
            account_number = input("Hesap Numarasi: ")
            for account in Account.accounts:
                if account.account_number == account_number:
                    account.view_balance()
                    break
            else:
                print("Hesap bulunamadi.")
        
        elif secim == "5":
            Bank.display_bank_info()
        
        elif secim == "6":
            print("Cikis yapiliyor...")
            break
        
        else:
            print("Gecersiz secim, tekrar deneyin.")
