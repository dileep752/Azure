from abc import ABC, abstractclassmethod
from abc import ABC, abstractmethod  # Fixed import

class Payment(ABC):
    @abstractmethod
    def Payment_Process(self, amount):  # Fixed method name (added missing 'a')
        pass

class CreditCardPayment(Payment):
    def Payment_Process(self, amount):  # Fixed method name to match parent
        return f"Processing credit card payment of - {amount}"

class PhonePay(Payment):  # Fixed class name (added missing 'a')
    def Payment_Process(self, amount):  # Fixed method name to match parent
        return f"Processing PhonePay payment of - {amount}"

def Make_payment(payment_method: Payment, amount: float):
    return payment_method.Payment_Process(amount)  # Fixed method name

# Usage
Credit_Card = CreditCardPayment()
Phone_pay = PhonePay()  # Fixed variable name to match class

print(Make_payment(Credit_Card, 1000))
print(Make_payment(Phone_pay, 2000))  # Fixed variable name