from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from datetime import datetime
import app.models as models
import app.schemas as schemas
import app.services as services
from app.database import engine, get_db
import logging
import app.import_csv as import_csv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Schools API",
    description="API to manage schools data",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/current-date")
def get_current_date():
    return {"current_date": datetime.now().isoformat()}

@app.get("/read-header/")
def read_header(custom_header: str = Header(None)):
    if custom_header is None:
        raise HTTPException(status_code=400, detail="Header not found")
    return {"custom_header": custom_header}

@app.get("/schools/")
def read_schools(db: Session = Depends(get_db)):
    schools = db.query(models.School).all()
    return schools

@app.get("/first-school/", response_model=schemas.School)
def read_first_school(db: Session = Depends(get_db)):
    first_school = db.query(models.School).first()
    if first_school is None:
        raise HTTPException(status_code=404, detail="No school found")
    return first_school

@app.get("/schools/{school_id}", response_model=schemas.School)
def read_school(school_id: int, db: Session = Depends(get_db)):
    school = db.query(models.School).filter(models.School.id == school_id).first()
    if school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return school

@app.post("/load-data/")
def load_data(db: Session = Depends(get_db)):
    # Vérifier si des données existent déjà
    existing_data = db.query(models.School).first()
    if existing_data:
        return {"message": "Data has already been loaded"}

    try:
        import_csv.import_csv_to_db('/app/app/ips.csv')
        return {"message": "Data loaded successfully"}
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise HTTPException(status_code=500, detail=f"Error loading data: {e}")

