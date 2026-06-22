from fastapi import FastAPI
from app.api.dashboard import router as dashboard_router
from app.models.audit_log import AuditLog
from app.api.audit_log import router as audit_log_router
from app.database.db import engine
from app.database.base import Base

from app.models.consent import Consent
from app.models.fi_request import FIRequest
from app.models.financial_data import FinancialData

from app.api.consent import router as consent_router
from app.api.fi_request import router as fi_request_router
from app.api.financial_data import router as financial_data_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AA FIU Platform",
    version="1.0.0"
)


app.include_router(
    consent_router,
    prefix="/consents",
    tags=["Consents"]
)

app.include_router(
    fi_request_router,
    prefix="/fi-requests",
    tags=["FI Requests"]
)

app.include_router(
    financial_data_router,
    prefix="/financial-data",
    tags=["Financial Data"]
)


@app.get("/")
def home():
    return {
        "message": "AA FIU Platform Running"
    }
app.include_router(
    audit_log_router,
    prefix="/audit-logs",
    tags=["Audit Logs"]

)
app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)