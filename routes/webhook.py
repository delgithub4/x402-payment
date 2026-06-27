from fastapi import APIRouter

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)


@router.post("/")
def webhook():

    return {
        "message": "Webhook received"
    }
