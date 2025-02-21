from pydantic import BaseModel

class SchoolBase(BaseModel):
    rentree_scolaire: str
    academie: str
    code_du_departement: str
    departement: str
    uai: str
    nom_de_l_etablissment: str
    code_insee_de_la_commune: str
    nom_de_la_commune: str
    secteur: str
    ips: float

class SchoolCreate(SchoolBase):
    pass

class School(SchoolBase):
    id: int

    class Config:
        orm_mode = True
