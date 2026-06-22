from fastapi import APIRouter
from sqlalchemy import text

from app.database.db import engine

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary():

    with engine.connect() as conn:

        total_consents = conn.execute(
            text("SELECT COUNT(*) FROM consents")
        ).scalar()

        total_fi_requests = conn.execute(
            text("SELECT COUNT(*) FROM fi_requests")
        ).scalar()

        total_financial_data = conn.execute(
            text("SELECT COUNT(*) FROM financial_data")
        ).scalar()

        total_audit_logs = conn.execute(
            text("SELECT COUNT(*) FROM audit_logs")
        ).scalar()

    return {
        "total_consents": total_consents,
        "total_fi_requests": total_fi_requests,
        "total_financial_data": total_financial_data,
        "total_audit_logs": total_audit_logs
    }