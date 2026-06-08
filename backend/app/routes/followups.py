from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import FollowUp
from app.schemas import FollowUpCreate, FollowUpResponse
import uuid

router = APIRouter(prefix="/followups", tags=["followups"])

@router.post("/", response_model=FollowUpResponse)
async def create_followup(followup: FollowUpCreate, db: Session = Depends(get_db)):
    db_followup = FollowUp(
        id=str(uuid.uuid4()),
        lead_id=followup.lead_id,
        followup_date=followup.followup_date,
        followup_time=followup.followup_time,
        call_notes=followup.call_notes,
        next_action=followup.next_action,
        status="Pending"
    )
    db.add(db_followup)
    db.commit()
    db.refresh(db_followup)
    return db_followup

@router.get("/lead/{lead_id}", response_model=list[FollowUpResponse])
async def get_lead_followups(lead_id: str, db: Session = Depends(get_db)):
    followups = db.query(FollowUp).filter(FollowUp.lead_id == lead_id).all()
    return followups

@router.get("/{followup_id}", response_model=FollowUpResponse)
async def get_followup(followup_id: str, db: Session = Depends(get_db)):
    followup = db.query(FollowUp).filter(FollowUp.id == followup_id).first()
    if not followup:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    return followup

@router.put("/{followup_id}", response_model=FollowUpResponse)
async def update_followup(followup_id: str, followup_update: FollowUpCreate, db: Session = Depends(get_db)):
    db_followup = db.query(FollowUp).filter(FollowUp.id == followup_id).first()
    if not db_followup:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    
    for key, value in followup_update.dict().items():
        if value is not None:
            setattr(db_followup, key, value)
    
    db.commit()
    db.refresh(db_followup)
    return db_followup

@router.patch("/{followup_id}/complete", response_model=FollowUpResponse)
async def complete_followup(followup_id: str, outcome: str = "Completed", db: Session = Depends(get_db)):
    db_followup = db.query(FollowUp).filter(FollowUp.id == followup_id).first()
    if not db_followup:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    
    db_followup.status = "Completed"
    db_followup.outcome = outcome
    
    db.commit()
    db.refresh(db_followup)
    return db_followup
