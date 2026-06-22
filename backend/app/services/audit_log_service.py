from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


def create_audit_log(
    db: Session,
    event_type: str,
    entity_type: str,
    entity_id: int,
    message: str
):
    audit_log = AuditLog(
        event_type=event_type,
        entity_type=entity_type,
        entity_id=entity_id,
        message=message
    )

    db.add(audit_log)
    db.commit()
    db.refresh(audit_log)

    return audit_log


def get_all_audit_logs(db: Session):
    return db.query(AuditLog).all()