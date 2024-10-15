from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users = []


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )


@app.get("/users/{user_id}")
async def read_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse(
                "users.html", {"request": request, "user": user}
            )
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: Annotated[int, Path(age=18, le=120, description="Enter age", example="24")],
):
    user_id = 1 if not users else users[-1].id + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: Annotated[int, Path(description="Enter user ID", example="1")],
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanProfi",
        ),
    ],
    age: Annotated[int, Path(age=18, le=120, description="Enter age", example="28")],
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: Annotated[int, Path(description="Enter user ID", example="2")]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
