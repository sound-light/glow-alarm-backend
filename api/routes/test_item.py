import logging
from fastapi import APIRouter
from fastapi import Depends, HTTPException, Path, Body
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session

from api.depends.get_db import get_db
from crud.test_item import crud_test_item
from schemas.test_item import TestItemCreate, TestItemUpdate, TestItemInDB

router = APIRouter()


@router.post("/test_item", response_model=TestItemInDB)
def create_test_item(test_item: TestItemCreate, db: Session = Depends(get_db)):
    #### db 데이터 생성 ####
    try:
        test_item = crud_test_item.insert(db=db, id=test_item.id, value=test_item.value)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"TestItem creation failed: {str(e)}")

    #### 201 created 응답코드 반환 ####
    return JSONResponse(status_code=201, content=jsonable_encoder(test_item))


@router.get("/test_item/{id}", response_model=TestItemInDB)
def read_test_item(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    try:
        test_item = crud_test_item.get(db, id)
    except:
        raise HTTPException(status_code=422, detail="validation error")
    if not test_item:
        raise HTTPException(status_code=404, detail="TestItem not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(test_item))


@router.get("/test_items", response_model=List[TestItemInDB])
def read_test_items(db: Session = Depends(get_db)):
    test_items = crud_test_item.get_all(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(test_items))


@router.put("/test_item/{id}", response_model=TestItemInDB)
def update_test_item(id: str = Path(..., min_length=1), db: Session = Depends(get_db),
                     test_item: TestItemUpdate = Body(...)):
    try:
        test_item = crud_test_item.update(db=db, id=id, value=test_item.value)
    except:
        raise HTTPException(status_code=422, detail="validation error")
    if not test_item:
        raise HTTPException(status_code=404, detail="TestItem not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(test_item))


@router.delete("/test_item/{id}", response_model=None)
def delete_test_item(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    test_item = crud_test_item.delete(db, id)
    if not test_item:
        raise HTTPException(status_code=404, detail="TestItem not found")
    return Response(status_code=204)
