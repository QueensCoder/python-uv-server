from fastapi import Depends, FastAPI
from .dependencies import get_query_token, get_token_header
from .routers.items import router as items_router
from .routers.users import router as user_router
from .db.models.seed import seed_demo_users


# seed_demo_users()  # Call the seeding function to populate the database with demo users
app = FastAPI(
    # dependencies=[Depends(get_query_token)]
)

app.include_router(items_router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
