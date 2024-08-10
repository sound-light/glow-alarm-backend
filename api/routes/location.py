import logging
from fastapi import APIRouter, Depends, HTTPException, Path, Body
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from api.depends.get_db import get_db
from crud.location import crud_location
from schemas.location import LocationCreate, LocationUpdate, LocationInDB, LocationResponse

router = APIRouter()

@router.post("/locations", response_model=LocationResponse)
def create_locaiton(location: LocationCreate, db: Session = Depends(get_db)):
    try:
        created_location = crud_location.insert(db=db, location_code=location.location_code, location_name=location.location_name)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Location creation failed: {str(e)}")

    return JSONResponse(status_code=201, content=jsonable_encoder(created_location))

@router.get("/location/{id}", response_model=LocationResponse)
def read_location(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    try:
        location = crud_location.get(db, id)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(location))

@router.get("/locations", response_model=List[LocationResponse])
def read_locations(db: Session = Depends(get_db)):
    locations = crud_location.get_all(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(locations))

@router.put("/location/{id}", response_model=LocationResponse)
def update_location(id: str = Path(..., min_length=1), db: Session = Depends(get_db),
                 location: LocationUpdate = Body(...)):
    try:
        updated_location = crud_location.update(db=db, id=id, location_code=location.location_code, location_name=location.location_name)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not updated_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(updated_location))

@router.delete("/location/{id}", response_model=None)
def delete_location(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    deleted_location = crud_location.delete(db, id)
    if not deleted_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return Response(status_code=204)
