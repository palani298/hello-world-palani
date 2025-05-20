
from sqlmodel import SQLModel, Session
from .models import ItemCreate, ItemRead, Item
from .database import engine, get_session

# SECRET_KEY = "VbDhJJnA_wdb2intu3r_FOOnYoK6T7mlLbvkI9qE7Fc"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
# users_db = {
#     "palani": {
#         "username": "palani",
#         "full_name": "Palaneeswar Chittoor",
#         "hashed_password": 'password',
#         "disabled": False,
#     },
#     "nick": {
#         "username": "nick",
#         "full_name": "Nick Masson",
#         "hashed_password": 'password',
#         "disabled": False,
#     }
# }
#
# def verify_password(plain_password, password):
#     return plain_password == password
#
# def authenticate_user(username: str, password: str):
#     user = users_db.get(username)
#     if not user or not verify_password(password, user["hashed_password"]):
#         return False
#     return user
#
# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = users_db.get(username)
#     if not user or user.get("disabled"):
#         raise credentials_exception
#     return user
# @app.post("/token", summary="Generate access token")
# @app.post("/token/", include_in_schema=False)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_access_token(data={"sub": user["username"]})
#     return {"access_token": access_token, "token_type": "bearer"}
#
# # CRUD endpoints
# @app.post("/items/", response_model=ItemRead, status_code=201)
# async def api_create_item(
#     item: ItemCreate,
#     session: Session = Depends(get_session),
#     current_user=Depends(get_current_user),
# ):
#     db_item = Item.from_orm(item)
#     session.add(db_item)
#     session.commit()
#     session.refresh(db_item)
#     return db_item
#
# @app.get("/items/", response_model=List[ItemRead])
# async def api_list_items(
#     session: Session = Depends(get_session),
#     current_user=Depends(get_current_user),
# ):
#     items = session.query(Item).all()
#     return items
#
# @app.get("/items/{item_id}", response_model=ItemRead)
# async def api_get_item(
#     item_id: int,
#     session: Session = Depends(get_session),
#     current_user=Depends(get_current_user),
# ):
#     db_item = session.get(Item, item_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item
#
# @app.put("/items/{item_id}", response_model=ItemRead)
# async def api_update_item(
#     item_id: int,
#     item: ItemCreate,
#     session: Session = Depends(get_session),
#     current_user=Depends(get_current_user),
# ):
#     db_item = session.get(Item, item_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     for key, value in item.dict().items():
#         setattr(db_item, key, value)
#     session.add(db_item)
#     session.commit()
#     session.refresh(db_item)
#     return db_item
#
# @app.delete("/items/{item_id}", status_code=204)
# async def api_delete_item(
#     item_id: int,
#     session: Session = Depends(get_session),
#     current_user=Depends(get_current_user),
# ):
#     db_item = session.get(Item, item_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     session.delete(db_item)
#     session.commit()