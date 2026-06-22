from pydantic import BaseModel


class FIRequestCreate(BaseModel):
    fi_request_id: str
    consent_request_id: str
    fi_start_date: str
    fi_end_date: str
    status: str