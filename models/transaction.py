from pydantic import BaseModel


class Transaction(BaseModel):

    transaction_id: str
    status: str
    amount: float
    currency: str
