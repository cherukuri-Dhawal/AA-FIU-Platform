from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Consent(Base):
    __tablename__ = "consents"

    id = Column(Integer, primary_key=True, index=True)

    consent_request_id = Column(String, unique=True)
    customer_name = Column(String)
    customer_mobile = Column(String)

    status = Column(String)
    gateway_token_id = Column(String)