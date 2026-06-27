from fastapi import APIRouter

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.get("/")
def get_payments():

    return {
        "message": "Payment endpoint"
    }


@router.post("/")
def create_payment():

    return {
        "message": "Payment created"
    }
