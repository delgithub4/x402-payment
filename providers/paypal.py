class PayPalProvider:

    def process(self, payment):

        return {
            "provider": "PayPal",
            "status": "success"
        }
