from fastapi import APIRouter


router_router = APIRouter()


@router_router.get("/greeter")
def greet():
    return "hello!"
