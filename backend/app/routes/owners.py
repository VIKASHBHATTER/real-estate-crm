from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Owner
from app.schemas import OwnerCreate, OwnerResponse
import uuid

router = APIRouter(prefix="/owners", tags=["owners"])

@router.post("/", response_model=OwnerResponse)
async def create_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    owner_id = f"OWN{str(uuid.uuid4())[:8].upper()}"
    db_owner = Owner(
        id=str(uuid.uuid4()),
        owner_id=owner_id,
        name=owner.name,
        mobile=owner.mobile,
        alternate_mobile=owner.alternate_mobile,
        email=owner.email,
        address=owner.address,
        expected_price=owner.expected_price,
        brokerage_terms=owner.brokerage_terms,
        remarks=owner.remarks
    )
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

@router.get("/", response_model=list[OwnerResponse])
async def get_owners(db: Session = Depends(get_db)):
    owners = db.query(Owner).all()
    return owners

@router.get("/{owner_id}", response_model=OwnerResponse)
async def get_owner(owner_id: str, db: Session = Depends(get_db)):
    owner = db.query(Owner).filter(Owner.owner_id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner

@router.put("/{owner_id}", response_model=OwnerResponse)
async def update_owner(owner_id: str, owner_update: OwnerCreate, db: Session = Depends(get_db)):
    db_owner = db.query(Owner).filter(Owner.owner_id == owner_id).first()
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    for key, value in owner_update.dict().items():
        if value is not None:
            setattr(db_owner, key, value)
    
    db.commit()
    db.refresh(db_owner)
    return db_owner

@router.delete("/{owner_id}")
async def delete_owner(owner_id: str, db: Session = Depends(get_db)):
    db_owner = db.query(Owner).filter(Owner.owner_id == owner_id).first()
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    db.delete(db_owner)
    db.commit()
    return {"message": "Owner deleted successfully"}
