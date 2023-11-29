from fastapi import APIRouter
from models.auth_model import AuthModel

router = APIRouter()

@router.get("/")
async def read_root():
    aa = await AuthModel.test(False)
    return {"Hello": "Auth Router"}
