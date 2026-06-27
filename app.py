from fastapi import FastAPI

from routes.payment import router as payment_router
from routes.refund import router as refund_router
from routes.webhook import router as webhook_router

app = FastAPI(
    title="x402 Payment",
    version="1.0.0"
)

app.include_router(payment_router)
app.include_router(refund_router)
app.include_router(webhook_router)


@app.get("/")
def home():

    return {
        "service": "x402-payment",
        "status": "running"
    }
