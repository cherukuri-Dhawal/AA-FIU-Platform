from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.fi_request import FIRequestCreate

from app.services.fi_request_service import (
    create_fi_request,
    get_all_fi_requests,
    get_fi_request_by_id
)

router = APIRouter(
    prefix="/fi-requests",
    tags=["FI Requests"]
)
@router.get("/test")
def test():
    return {
        "message": "FI Request API Working"
    }
@router.post("/create")
def create_fi_request_api(
    fi_request: FIRequestCreate,
    db: Session = Depends(get_db)
):
    result = create_fi_request(
        db=db,
        fi_request_id=fi_request.fi_request_id,
        consent_request_id=fi_request.consent_request_id,
        fi_start_date=fi_request.fi_start_date,
        fi_end_date=fi_request.fi_end_date,
        status=fi_request.status
    )

    return {
        "id": result.id,
        "message": "FI Request Saved Successfully"
    }
@router.get("/list")
def list_fi_requests(
    db: Session = Depends(get_db)
):
    return get_all_fi_requests(db)

@router.get("/{request_id}")
def get_fi_request(
    request_id: int,
    db: Session = Depends(get_db)
):
    return get_fi_request_by_id(
        db,
        request_id
    )