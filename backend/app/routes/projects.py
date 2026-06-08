from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Project
from app.schemas import ProjectCreate, ProjectResponse
import uuid

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    project_id = f"PROJ{str(uuid.uuid4())[:8].upper()}"
    db_project = Project(
        id=str(uuid.uuid4()),
        project_id=project_id,
        name=project.name,
        builder_name=project.builder_name,
        rera_number=project.rera_number,
        property_category=project.property_category,
        location=project.location,
        launch_date=project.launch_date,
        possession_date=project.possession_date,
        inventory_total=project.inventory_total,
        inventory_available=project.inventory_available,
        brochure_link=project.brochure_link,
        video_link=project.video_link,
        google_map_link=project.google_map_link
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=list[ProjectResponse])
async def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: str, project_update: ProjectCreate, db: Session = Depends(get_db)):
    db_project = db.query(Project).filter(Project.project_id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    for key, value in project_update.dict().items():
        if value is not None:
            setattr(db_project, key, value)
    
    db.commit()
    db.refresh(db_project)
    return db_project
