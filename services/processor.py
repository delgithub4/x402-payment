import uuid

from services.gateway import PaymentGateway


class PaymentProcessor:

    def __init__(self):

        self.gateway = PaymentGateway()

    def process(self, payment):

        provider = self.gateway.get_provider(payment.provider)

        if provider is None:

            return {
                "status": "failed",
                "message": "Unsupported payment provider."
            }

        result = provider.process(payment)

        return {
            "transaction_id": str(uuid.uuid4()),
            "provider": result["provider"],
            "status": result["status"],
            "customer": payment.customer,
            "amount": payment.amount,
            "currency": payment.currency
        }
