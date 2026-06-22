from sqlalchemy.orm import Session

from app.models.financial_data import FinancialData
from app.models.audit_log import AuditLog


def create_financial_data(
    db: Session,
    fi_data_id: str,
    fi_request_id: str,
    account_id: str,
    account_number: str,
    fi_type: str,
    fip_id: str
):
    financial_data = FinancialData(
        fi_data_id=fi_data_id,
        fi_request_id=fi_request_id,
        account_id=account_id,
        account_number=account_number,
        fi_type=fi_type,
        fip_id=fip_id
    )

    db.add(financial_data)
    db.commit()
    db.refresh(financial_data)

    audit_log = AuditLog(
        event_type="FINANCIAL_DATA_CREATED",
        entity_type="FINANCIAL_DATA",
        entity_id=financial_data.id,
        message="Financial data created successfully"
    )

    db.add(audit_log)
    db.commit()

    return financial_data


def get_all_financial_data(db: Session):
    return db.query(FinancialData).all()


def get_financial_data_by_id(
    db: Session,
    data_id: int
):
    return (
        db.query(FinancialData)
        .filter(FinancialData.id == data_id)
        .first()
    )