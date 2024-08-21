# payment.py

class Payment:
    def __init__(self, payment_id, policyholder_id, amount, due_date):
        self.payment_id = payment_id  # Unique ID for the payment
        self.policyholder_id = policyholder_id  # ID of the policyholder associated with this payment
        self.amount = amount  # Payment amount
        self.status = 'Pending'  # Payment status (Pending/Completed)
        self.due_date = due_date  # Payment due date

    def process_payment(self):
        self.status = 'Completed'
        print(f"Payment {self.payment_id} for Policyholder {self.policyholder_id} has been processed.")

    def send_reminder(self):
        print(f"Reminder: Payment {self.payment_id} is due on {self.due_date}.")

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        print(f"Penalty applied. New amount due: {self.amount}")
