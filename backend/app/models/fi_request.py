from sqlalchemy import Column, Integer, String

from app.database.base import Base


class FIRequest(Base):
    __tablename__ = "fi_requests"

    id = Column(Integer, primary_key=True, index=True)

    fi_request_id = Column(String, unique=True)

    consent_request_id = Column(String)

    fi_start_date = Column(String)

    fi_end_date = Column(String)

    status = Column(String)
    