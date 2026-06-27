from pydantic import BaseModel


class Payment(BaseModel):

    customer: str
    amount: float
    currency: str
    description: str

    provider: str
