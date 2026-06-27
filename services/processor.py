import uuid


class PaymentProcessor:

    def process(self, payment):

        return {
            "transaction_id": str(uuid.uuid4()),
            "status": "success",
            "customer": payment.customer,
            "amount": payment.amount,
            "currency": payment.currency
        }
