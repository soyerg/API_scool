import csv
import logging
import os
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
import app.models as models

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def import_csv_to_db(file_path: str):
    logger.info(f"Starting import from file: {file_path}")
    logger.info(f"Current working directory: {os.getcwd()}")
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    db: Session = SessionLocal()
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            row_count = 0
            for row in reader:
                logger.info(f"Processing row: {row}")
                school = models.School(
                    rentree_scolaire=row['rentree_scolaire'],
                    academie=row['academie'],
                    code_du_departement=row['code_du_departement'],
                    departement=row['departement'],
                    uai=row['uai'],
                    nom_de_l_etablissment=row['nom_de_l_etablissment'],
                    code_insee_de_la_commune=row['code_insee_de_la_commune'],
                    nom_de_la_commune=row['nom_de_la_commune'],
                    secteur=row['secteur'],
                    ips=float(row['ips'])
                )
                db.add(school)
                row_count += 1
                logger.info(f"Added school: {school.nom_de_l_etablissment}")
            db.commit()
            if row_count == 0:
                logger.error("No data imported from CSV file")
                raise ValueError("No data imported from CSV file")
            logger.info("CSV data imported successfully")
    except Exception as e:
        logger.error(f"Error importing CSV data: {e}")
        raise
    finally:
        db.close()

