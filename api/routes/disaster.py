from fastapi import APIRouter, Depends, HTTPException, Path, Body
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from api.depends.get_db import get_db
from crud.disaster import crud_disaster
from schemas.disaster import DisasterCreate, DisasterUpdate, DisasterInDB, DisasterResponse

router = APIRouter()

@router.post("/disaster", response_model=DisasterResponse)
def create_disaster(disaster: DisasterCreate, db: Session = Depends(get_db)):
    try:
        created_disaster = crud_disaster.insert(db=db, disaster_time=disaster.disaster_time, disaster_level=disaster.disaster_level, disaster_message=disaster.disaster_message, location_id=disaster.location_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Disaster creation failed: {str(e)}")

    return JSONResponse(status_code=201, content=jsonable_encoder(created_disaster))

@router.get("/disaster/{id}", response_model=DisasterResponse)
def read_disaster(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    try:
        disaster = crud_disaster.get(db, id)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not disaster:
        raise HTTPException(status_code=404, detail="Disaster not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(disaster))

@router.get("/disasters/location/{location_id}", response_model=List[DisasterResponse])
def read_disasters_by_location_id(location_id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    disasters = crud_disaster.get_all_by_location_id(db, location_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(disasters))

@router.get("/disasters", response_model=List[DisasterInDB])
def read_disasters(db: Session = Depends(get_db)):
    disasters = crud_disaster.get_all(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(disasters))

@router.put("/disaster/{id}", response_model=DisasterResponse)
def update_disaster(id: str = Path(..., min_length=1), db: Session = Depends(get_db),
                 disaster: DisasterUpdate = Body(...)):
    try:
        updated_disaster = crud_disaster.update(db=db, id=id, disaster_time=disaster.disaster_time, disaster_level=disaster.disaster_level, disaster_message=disaster.disaster_message, location_id=disaster.location_id)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not updated_disaster:
        raise HTTPException(status_code=404, detail="Disaster not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(updated_disaster))

@router.delete("/disaster/{id}", response_model=None)
def delete_disaster(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    deleted_disaster = crud_disaster.delete(db, id)
    if not deleted_disaster:
        raise HTTPException(status_code=404, detail="Disaster not found")
    return Response(status_code=204)
