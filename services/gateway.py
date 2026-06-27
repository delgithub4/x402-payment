from providers.stripe import StripeProvider
from providers.paystack import PaystackProvider
from providers.flutterwave import FlutterwaveProvider
from providers.paypal import PayPalProvider


class PaymentGateway:

    def __init__(self):

        self.providers = {
            "stripe": StripeProvider(),
            "paystack": PaystackProvider(),
            "flutterwave": FlutterwaveProvider(),
            "paypal": PayPalProvider()
        }

    def get_provider(self, name):

        return self.providers.get(name.lower())
