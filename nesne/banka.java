import java.util.*;

// Account Sınıfı
class Account {
    private String accountNumber;
    private String owner;
    private double balance;
    
    public static List<Account> accounts = new ArrayList<>();

    public Account(String accountNumber, String owner, double balance) {
        this.accountNumber = accountNumber;
        this.owner = owner;
        this.balance = balance;
        accounts.add(this);
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println(amount + " TL hesaba yatirildi. Yeni bakiye: " + balance + " TL");
            Bank.trackTransaction(accountNumber + " nolu hesaba " + amount + " TL yatirildi.");
        } else {
            System.out.println("Gecersiz yatirma miktari.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            System.out.println(amount + " TL cekildi. Yeni bakiye: " + balance + " TL");
            Bank.trackTransaction(accountNumber + " nolu hesaptan " + amount + " TL cekildi.");
        } else {
            System.out.println("Yetersiz bakiye veya gecersiz cekim miktari.");
        }
    }

    public void viewBalance() {
        System.out.println("Hesap Sahibi: " + owner);
        System.out.println("Hesap Numarasi: " + accountNumber);
        System.out.println("Bakiye: " + balance + " TL");
    }
}

// Bank Sınıfı
class Bank {
    public static List<String> transactionHistory = new ArrayList<>();

    public static void displayBankInfo() {
        System.out.println("Bankamiza hosgeldiniz. Tum hesaplar guven altindadir.");
        System.out.println("Toplam Hesap Sayisi: " + Account.accounts.size());
    }

    public static void trackTransaction(String description) {
        transactionHistory.add(description);
    }
}

// Test Kodları
public class BankSystem {
    public static void main(String[] args) {
        Account acc1 = new Account("12345", "Ali Yilmaz", 1000);
        Account acc2 = new Account("67890", "Ayse Demir", 2000);

        acc1.viewBalance();
        acc1.deposit(500);
        acc1.withdraw(300);
        acc1.viewBalance();
        
        acc2.viewBalance();
        acc2.withdraw(2500);

        Bank.displayBankInfo();
        
        System.out.println("\nIslem Gecmisi:");
        for (String transaction : Bank.transactionHistory) {
            System.out.println(transaction);
        }
    }
}
