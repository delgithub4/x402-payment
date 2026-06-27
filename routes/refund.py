from fastapi import APIRouter

router = APIRouter(
    prefix="/refunds",
    tags=["Refunds"]
)


@router.post("/")
def refund():

    return {
        "message": "Refund initiated"
    }
