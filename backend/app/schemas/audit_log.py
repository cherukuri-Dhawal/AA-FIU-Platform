from pydantic import BaseModel


class AuditLogCreate(BaseModel):
    event_type: str
    entity_type: str
    entity_id: int
    message: str