from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from typing import Optional
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.request_membership import Request


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    user_email: str = Column(String, unique=True, index=True, nullable=False)
    user_password: str = Column(String, nullable=False)
    user_name: Optional[str] = Column(String, nullable=True)
    status: bool = Column(Boolean, default=True, server_default="true", nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: datetime = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    description: Optional[str] = Column(String, nullable=True)
    
    companies = relationship("Company", back_populates="owner",  cascade="all, delete")
    invitations_sent = relationship("Invitation", back_populates="from_user")
    requests_sent = relationship("Request", back_populates="from_user")
    members = relationship("Members", back_populates="user")
    quiz_results = relationship("QuizResult", back_populates="user")
    notification = relationship("Notification", back_populates="user", cascade="all, delete")