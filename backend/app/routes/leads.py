from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Lead
from app.schemas import LeadCreate, LeadResponse
import uuid

router = APIRouter(prefix="/leads", tags=["leads"])

@router.post("/", response_model=LeadResponse)
async def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    lead_id = f"LD{str(uuid.uuid4())[:8].upper()}"
    db_lead = Lead(
        lead_id=lead_id,
        name=lead.name,
        mobile=lead.mobile,
        email=lead.email,
        lead_source=lead.lead_source,
        status="New",
        score=0,
        score_category="COLD"
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.get("/", response_model=list[LeadResponse])
async def get_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).all()
    return leads

@router.get("/{lead_id}", response_model=LeadResponse)
async def get_lead(lead_id: str, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.lead_id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead
