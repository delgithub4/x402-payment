class PaymentValidator:

    def validate(self, payment):

        if payment.amount <= 0:

            return False, "Amount must be greater than zero."

        if len(payment.currency) != 3:

            return False, "Currency must be a 3-letter code."

        return True, "Validation successful."
