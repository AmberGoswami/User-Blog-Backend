from fastapi import FastAPI
from .api.blog import blog_controller
from .api.user import user_controller
from .api.authentication import authentication_controller
app=FastAPI()

app.include_router(authentication_controller.router)
app.include_router(user_controller.router)
app.include_router(blog_controller.router)
