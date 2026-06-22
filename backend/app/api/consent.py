from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.consent import ConsentCreate
from app.database.db import get_db
from app.services.digio_service import (
    create_consent,
    get_all_consents,
    get_consent_by_id
)

router = APIRouter(
    prefix="/consents",
    tags=["Consents"]
)


@router.get("/test")
def test():
    return {
        "message": "Consent API Working"
    }
@router.get("/list")
def list_consents(
    db: Session = Depends(get_db)
):
    consents = get_all_consents(db)

    return consents
@router.get("/{consent_id}")
def get_consent(
    consent_id: int,
    db: Session = Depends(get_db)
):
    consent = get_consent_by_id(
        db,
        consent_id
    )

    return consent

@router.post("/create")
def create_consent_api(
    consent: ConsentCreate,
    db: Session = Depends(get_db)
):
    {
  "event_type": "CONSENT_CREATED",
  "entity_type": "CONSENT",
  "entity_id": 1,
  "message": "Consent created successfully"
}

    return {
        "id": result.id,
        "message": "Consent Saved Successfully"
    }