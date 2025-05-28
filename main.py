from fastapi import FastAPI
from app.routes import subscriptions, plans
from app.routes.token import router as token_router  # import the token route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(token_router)  # include token router
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])
app.include_router(plans.router, prefix="/plans", tags=["Plans"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
