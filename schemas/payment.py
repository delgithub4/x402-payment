from typing import Any

from pydantic import BaseModel


class PaymentRequest(BaseModel):
    amount: float
    currency: str
    recipient: str
    metadata: dict[str, Any] = {}


class PaymentResponse(BaseModel):
    success: bool
    transaction_id: str
    message: str
    data: Any | None = None
