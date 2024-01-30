import fastapi
from fastapi import HTTPException, Depends, APIRouter
import schemas
import models
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/voltage", tags=["voltage"])


@router.post("/", status_code=fastapi.status.HTTP_200_OK)
def ad_tank_post(post: schemas.Voltage, db: Session = Depends(get_db)):

    new_post = models.VOLTAGE(**post.model_dump())
    db.add(new_post)
    db.commit()

    return new_post


@router.get("/", status_code=fastapi.status.HTTP_200_OK, response_model=schemas.Voltage)
def ad_get(db: Session = Depends(get_db), search: str = ''):
    query = db.query(models.VOLTAGE).order_by(models.VOLTAGE.TIME_STAMP.desc()).filter(models.VOLTAGE.DEVICE.contains(search).all())
    return query

