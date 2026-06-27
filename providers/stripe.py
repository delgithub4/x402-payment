class StripeProvider:

    def process(self, payment):

        return {
            "provider": "Stripe",
            "status": "success"
        }
