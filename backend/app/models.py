from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean, Text, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default="Agent")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Lead(Base):
    __tablename__ = "leads"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    lead_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    mobile = Column(String(20), nullable=False)
    email = Column(String(255), nullable=True)
    lead_source = Column(String(100), nullable=False)
    status = Column(String(50), default="New")
    score = Column(Integer, default=0)
    score_category = Column(String(20), default="COLD")
    created_at = Column(DateTime, default=datetime.utcnow)

class Property(Base):
    __tablename__ = "properties"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    property_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    address = Column(Text, nullable=False)
    status = Column(String(50), default="Available")
    created_at = Column(DateTime, default=datetime.utcnow)

class Deal(Base):
    __tablename__ = "deals"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    deal_id = Column(String(50), unique=True, nullable=False)
    lead_id = Column(String(36), ForeignKey("leads.id"))
    property_id = Column(String(36), ForeignKey("properties.id"))
    deal_value = Column(Float, nullable=False)
    stage = Column(String(50), default="Site Visit")
    created_at = Column(DateTime, default=datetime.utcnow)
