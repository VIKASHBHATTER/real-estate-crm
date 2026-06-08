from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Requirement
from app.schemas import RequirementCreate, RequirementResponse
import uuid

router = APIRouter(prefix="/requirements", tags=["requirements"])

@router.post("/", response_model=RequirementResponse)
async def create_requirement(req: RequirementCreate, db: Session = Depends(get_db)):
    db_req = Requirement(
        id=str(uuid.uuid4()),
        lead_id=req.lead_id,
        requirement_type=req.requirement_type,
        property_category=req.property_category,
        property_type=req.property_type,
        budget_min=req.budget_min,
        budget_max=req.budget_max,
        preferred_locations=req.preferred_locations,
        carpet_area_min=req.carpet_area_min,
        carpet_area_max=req.carpet_area_max,
        floor_preference=req.floor_preference,
        facing=req.facing,
        parking_required=req.parking_required,
        furnished=req.furnished,
        purpose=req.purpose,
        timeline=req.timeline,
        special_requirements=req.special_requirements
    )
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req

@router.get("/{lead_id}", response_model=RequirementResponse)
async def get_requirement(lead_id: str, db: Session = Depends(get_db)):
    req = db.query(Requirement).filter(Requirement.lead_id == lead_id).first()
    if not req:
        raise HTTPException(status_code=404, detail="Requirement not found")
    return req

@router.put("/{lead_id}", response_model=RequirementResponse)
async def update_requirement(lead_id: str, req_update: RequirementCreate, db: Session = Depends(get_db)):
    db_req = db.query(Requirement).filter(Requirement.lead_id == lead_id).first()
    if not db_req:
        raise HTTPException(status_code=404, detail="Requirement not found")
    
    for key, value in req_update.dict().items():
        if value is not None:
            setattr(db_req, key, value)
    
    db.commit()
    db.refresh(db_req)
    return db_req
