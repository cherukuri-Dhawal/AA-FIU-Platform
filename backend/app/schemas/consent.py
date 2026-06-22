from pydantic import BaseModel


class ConsentCreate(BaseModel):
    consent_request_id: str
    customer_name: str
    customer_mobile: str
    status: str
    gateway_token_id: str