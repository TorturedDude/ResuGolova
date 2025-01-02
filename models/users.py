from sqlalchemy import Column, String, Text, Boolean, Integer, BigInteger, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from models.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_date = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_date = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
    is_blocked = Column(Boolean, nullable=False, default=False)
