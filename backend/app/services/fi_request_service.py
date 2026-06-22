from sqlalchemy.orm import Session

from app.models.fi_request import FIRequest
from app.models.audit_log import AuditLog


def create_fi_request(
    db: Session,
    fi_request_id: str,
    consent_request_id: str,
    fi_start_date: str,
    fi_end_date: str,
    status: str
):
    fi_request = FIRequest(
        fi_request_id=fi_request_id,
        consent_request_id=consent_request_id,
        fi_start_date=fi_start_date,
        fi_end_date=fi_end_date,
        status=status
    )

    db.add(fi_request)
    db.commit()
    db.refresh(fi_request)

    audit_log = AuditLog(
        event_type="FI_REQUEST_CREATED",
        entity_type="FI_REQUEST",
        entity_id=fi_request.id,
        message="FI Request created successfully"
    )

    db.add(audit_log)
    db.commit()

    return fi_request


def get_all_fi_requests(db: Session):
    return db.query(FIRequest).all()


def get_fi_request_by_id(
    db: Session,
    request_id: int
):
    return (
        db.query(FIRequest)
        .filter(FIRequest.id == request_id)
        .first()
    )