from fastapi import APIRouter

from models.payment import Payment

from services.validator import PaymentValidator
from services.processor import PaymentProcessor

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

validator = PaymentValidator()
processor = PaymentProcessor()


@router.post("/")
def create_payment(payment: Payment):

    valid, message = validator.validate(payment)

    if not valid:

        return {
            "success": False,
            "message": message
        }

    transaction = processor.process(payment)

    return {
        "success": True,
        "transaction": transaction
    }
