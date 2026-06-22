from sqlalchemy.orm import Session

from app.models.consent import Consent
from app.models.audit_log import AuditLog


def create_consent(
    db: Session,
    consent_request_id: str,
    customer_name: str,
    customer_mobile: str,
    status: str,
    gateway_token_id: str
):
    consent = Consent(
        consent_request_id=consent_request_id,
        customer_name=customer_name,
        customer_mobile=customer_mobile,
        status=status,
        gateway_token_id=gateway_token_id
    )

    db.add(consent)
    db.commit()
    db.refresh(consent)

    audit_log = AuditLog(
        event_type="CONSENT_CREATED",
        entity_type="CONSENT",
        entity_id=consent.id,
        message="Consent created successfully"
    )

    db.add(audit_log)
    db.commit()

    return consent


def get_all_consents(db: Session):
    return db.query(Consent).all()


def get_consent_by_id(db: Session, consent_id: int):
    return db.query(Consent).filter(
        Consent.id == consent_id
    ).first()