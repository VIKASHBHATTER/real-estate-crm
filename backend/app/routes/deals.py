from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Deal
from app.schemas import DealCreate, DealUpdate, DealResponse
import uuid

router = APIRouter(prefix="/deals", tags=["deals"])

@router.post("/", response_model=DealResponse)
async def create_deal(deal: DealCreate, db: Session = Depends(get_db)):
    deal_id = f"DEAL{str(uuid.uuid4())[:8].upper()}"
    db_deal = Deal(
        deal_id=deal_id,
        lead_id=deal.lead_id,
        property_id=deal.property_id,
        agent_id=deal.agent_id,
        deal_value=deal.deal_value,
        negotiated_value=deal.negotiated_value,
        token_amount=deal.token_amount,
        stage="Site Visit",
        status="Active"
    )
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal

@router.get("/", response_model=list[DealResponse])
async def get_deals(db: Session = Depends(get_db)):
    deals = db.query(Deal).all()
    return deals

@router.get("/{deal_id}", response_model=DealResponse)
async def get_deal(deal_id: str, db: Session = Depends(get_db)):
    deal = db.query(Deal).filter(Deal.deal_id == deal_id).first()
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal

@router.patch("/{deal_id}", response_model=DealResponse)
async def update_deal(deal_id: str, deal_update: DealUpdate, db: Session = Depends(get_db)):
    db_deal = db.query(Deal).filter(Deal.deal_id == deal_id).first()
    if not db_deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    
    if deal_update.stage:
        db_deal.stage = deal_update.stage
    if deal_update.negotiated_value:
        db_deal.negotiated_value = deal_update.negotiated_value
    if deal_update.token_amount:
        db_deal.token_amount = deal_update.token_amount
    if deal_update.agreement_date:
        db_deal.agreement_date = deal_update.agreement_date
    if deal_update.registration_date:
        db_deal.registration_date = deal_update.registration_date
    if deal_update.received_brokerage:
        db_deal.received_brokerage = deal_update.received_brokerage
    
    db.commit()
    db.refresh(db_deal)
    return db_deal
