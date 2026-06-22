from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.financial_data import FinancialDataCreate

from app.services.financial_data_service import (
    create_financial_data,
    get_all_financial_data,
    get_financial_data_by_id
)

router = APIRouter(
    prefix="/financial-data",
    tags=["Financial Data"]
)
@router.get("/test")
def test():
    return {
        "message": "Financial Data API Working"
    }
@router.post("/create")
def create_financial_data_api(
    financial_data: FinancialDataCreate,
    db: Session = Depends(get_db)
):
    result = create_financial_data(
        db=db,
        fi_data_id=financial_data.fi_data_id,
        fi_request_id=financial_data.fi_request_id,
        account_id=financial_data.account_id,
        account_number=financial_data.account_number,
        fi_type=financial_data.fi_type,
        fip_id=financial_data.fip_id
    )

    return {
        "id": result.id,
        "message": "Financial Data Saved Successfully"
    }




@router.get("/list")
def list_financial_data(
    db: Session = Depends(get_db)
):
    return get_all_financial_data(db)


@router.get("/{data_id}")
def get_financial_data(
    data_id: int,
    db: Session = Depends(get_db)
):
    return get_financial_data_by_id(
        db,
        data_id
    )