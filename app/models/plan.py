from sqlalchemy import Column, Integer, String
from app.database import Base

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    features = Column(String)
