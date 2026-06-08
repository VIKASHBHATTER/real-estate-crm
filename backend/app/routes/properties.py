from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Property
from app.schemas import PropertyCreate, PropertyResponse
import uuid

router = APIRouter(prefix="/properties", tags=["properties"])

@router.post("/", response_model=PropertyResponse)
async def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    property_id = f"PROP{str(uuid.uuid4())[:8].upper()}"
    db_property = Property(
        property_id=property_id,
        name=property.name,
        price=property.price,
        address=property.address,
        status="Available"
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

@router.get("/", response_model=list[PropertyResponse])
async def get_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return properties

@router.get("/{property_id}", response_model=PropertyResponse)
async def get_property(property_id: str, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.property_id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property
