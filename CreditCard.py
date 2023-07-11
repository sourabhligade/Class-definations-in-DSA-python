class CreditCard:
”””A consumer credit card.”””
def     init     (self, customer, bank, acnt, limit): ”””Create a new credit card instance.
The initial balance is zero.
customer the name of the customer (e.g., John Bowman )
bank
acnt
limit
”””
self.   customer = customer self.   bank = bank
the name of the bank (e.g., California Savings ) the acount identifier (e.g., 5391 0375 9387 5309 ) credit limit (measured in dollars)
self.   account = acnt self.   limit = limit self.   balance = 0
def get customer(self):
”””Return name of the customer.””” return self. customer
def get bank(self):
”””Return the bank s name.””” return self. bank
def get account(self):
”””Return the card identifying number (typically stored as a string).””” return self. account
def get limit(self):
”””Return current credit limit.””” return self. limit
def get balance(self): ”””Return current balance.””” return self. balance
def charge(self, price):
”””Charge given price to the card, assuming suðcient credit limit.
Return True if charge was processed; False if charge was denied. ”””
if price + self. balance > self. limit: return False
else:
self. balance += price return True
# if charge would exceed limit, # cannot accept charge
def make payment(self, amount):
”””Process customer payment that reduces balance.””” self. balance != amount

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr,late_fee,min_payment_percentage):
        """Create a new predatory credit card instance."""
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self.apr = apr
        self.late_fee=late_fee
        self.minimum_payment_percentage=min_payment_percentage

    def charge(self, price):
        """Charge the given price to the card, assuming sufficient credit limit.
        Return True if the charge was processed.
        Return False and assess a $5 fee if the charge is denied.
        """
        success = super().charge(price)
        if not success:
            self.balance += 5
        else:
            self.minimum_payment_percentage=False
        return success

    def process_month(self):
        """Assess monthly interest on the outstanding balance."""
        if not self.minimum_payment_made:
            self.balance+=self.late_fee
            if self.balance>0:
                min_payment=self.minimum_payment_percentage/100 *self.balance
                if not self.minimum_payment_made:
                    self.balance+=min_payment

            # if positive balance, convert APR to monthly multiplicative factor

            
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self.balance *= monthly_factor
        self.minimum_payment_made=True
