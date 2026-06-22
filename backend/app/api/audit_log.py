from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.audit_log import AuditLogCreate

from app.services.audit_log_service import (
    create_audit_log,
    get_all_audit_logs
)

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


@router.get("/test")
def test():
    return {
        "message": "Audit Log API Working"
    }


@router.post("/create")
def create_audit_log_api(
    audit_log: AuditLogCreate,
    db: Session = Depends(get_db)
):
    result = create_audit_log(
        db=db,
        event_type=audit_log.event_type,
        entity_type=audit_log.entity_type,
        entity_id=audit_log.entity_id,
        message=audit_log.message
    )

    return {
        "id": result.id,
        "message": "Audit Log Saved Successfully"
    }


@router.get("/list")
def list_audit_logs(
    db: Session = Depends(get_db)
):
    return get_all_audit_logs(db)