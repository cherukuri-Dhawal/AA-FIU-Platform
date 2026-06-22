from sqlalchemy import Column, Integer, String

from app.database.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    event_type = Column(String)

    entity_type = Column(String)

    entity_id = Column(Integer)

    message = Column(String)