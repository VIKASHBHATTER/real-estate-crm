from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    mobile: str
    email: Optional[str] = None
    lead_source: str

class LeadResponse(BaseModel):
    id: str
    lead_id: str
    name: str
    mobile: str
    status: str
    score: int

    class Config:
        from_attributes = True

class PropertyCreate(BaseModel):
    name: str
    price: float
    address: str

class PropertyResponse(BaseModel):
    id: str
    property_id: str
    name: str
    price: float
    address: str

    class Config:
        from_attributes = True

class DealCreate(BaseModel):
    lead_id: str
    property_id: str
    deal_value: float

class DealResponse(BaseModel):
    id: str
    deal_id: str
    lead_id: str
    property_id: str
    deal_value: float
    stage: str

    class Config:
        from_attributes = True
