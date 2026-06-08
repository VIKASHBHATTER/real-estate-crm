from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import SiteVisit
from app.schemas import SiteVisitCreate, SiteVisitResponse
import uuid

router = APIRouter(prefix="/site-visits", tags=["site-visits"])

@router.post("/", response_model=SiteVisitResponse)
async def create_site_visit(visit: SiteVisitCreate, db: Session = Depends(get_db)):
    visit_id = f"SV{str(uuid.uuid4())[:8].upper()}"
    db_visit = SiteVisit(
        id=str(uuid.uuid4()),
        visit_id=visit_id,
        lead_id=visit.lead_id,
        property_id=visit.property_id,
        visit_date=visit.visit_date,
        visit_time=visit.visit_time,
        agent_id=visit.agent_id,
        owner_id=visit.owner_id,
        status="Scheduled"
    )
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit

@router.get("/", response_model=list[SiteVisitResponse])
async def get_site_visits(db: Session = Depends(get_db)):
    visits = db.query(SiteVisit).all()
    return visits

@router.get("/{visit_id}", response_model=SiteVisitResponse)
async def get_site_visit(visit_id: str, db: Session = Depends(get_db)):
    visit = db.query(SiteVisit).filter(SiteVisit.visit_id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Site visit not found")
    return visit

@router.get("/lead/{lead_id}", response_model=list[SiteVisitResponse])
async def get_lead_site_visits(lead_id: str, db: Session = Depends(get_db)):
    visits = db.query(SiteVisit).filter(SiteVisit.lead_id == lead_id).all()
    return visits

@router.put("/{visit_id}", response_model=SiteVisitResponse)
async def update_site_visit(visit_id: str, visit_update: SiteVisitCreate, db: Session = Depends(get_db)):
    db_visit = db.query(SiteVisit).filter(SiteVisit.visit_id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Site visit not found")
    
    for key, value in visit_update.dict().items():
        if value is not None:
            setattr(db_visit, key, value)
    
    db.commit()
    db.refresh(db_visit)
    return db_visit

@router.patch("/{visit_id}/feedback", response_model=SiteVisitResponse)
async def add_site_visit_feedback(visit_id: str, feedback: str, interest_level: str, db: Session = Depends(get_db)):
    db_visit = db.query(SiteVisit).filter(SiteVisit.visit_id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Site visit not found")
    
    db_visit.feedback = feedback
    db_visit.interest_level = interest_level
    db_visit.status = "Completed"
    
    db.commit()
    db.refresh(db_visit)
    return db_visit
