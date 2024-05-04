from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Charge(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    government_id = Column(String, index=True)
    email = Column(String, index=True)
    debt_amount = Column(Float)
    debt_due_date = Column(Date)

Base.metadata.create_all(bind=engine)

class ChargeCreate(BaseModel):
    name: str
    government_id: str
    email: str
    debt_amount: float
    debt_due_date: str

app = FastAPI()

def create_charge(charge: ChargeCreate):
    db = SessionLocal()
    try:
        db_charge = Charge(
            name=charge.name,
            government_id=charge.government_id,
            email=charge.email,
            debt_amount=charge.debt_amount,
            debt_due_date=charge.debt_due_date
        )
        db.add(db_charge)
        db.commit()
        db.refresh(db_charge)
        return db_charge
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/charges", response_model=Charge)
def create_charge_endpoint(charge: ChargeCreate):
    return create_charge(charge)