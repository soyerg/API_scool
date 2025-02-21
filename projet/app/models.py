from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    rentree_scolaire = Column(String)
    academie = Column(String)
    code_du_departement = Column(String)
    departement = Column(String)
    uai = Column(String)
    nom_de_l_etablissment = Column(String)
    code_insee_de_la_commune = Column(String)
    nom_de_la_commune = Column(String)
    secteur = Column(String)
    ips = Column(Float)
