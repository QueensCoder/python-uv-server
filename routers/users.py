from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus
from ..dependencies import get_token_header
from ..db.queries.api_queries import get_all_users, get_user_by_id, create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=HTTPStatus.OK)
async def get_all_users():
    all_users = get_all_users()
    return all_users


@router.get("/{user_id}", status_code=HTTPStatus.OK)
async def get_user_by_id(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return user


@router.post("/", status_code=HTTPStatus.CREATED)
async def create_new_user(username: str, email: str):
    new_user = create_user(username=username, email=email)
    if not new_user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="User creation failed"
        )
    return new_user
