from sqlalchemy import Column, Integer, String

from app.database.base import Base


class FinancialData(Base):
    __tablename__ = "financial_data"

    id = Column(Integer, primary_key=True, index=True)

    fi_data_id = Column(String, unique=True)

    fi_request_id = Column(String)

    account_id = Column(String)

    account_number = Column(String)

    fi_type = Column(String)

    fip_id = Column(String)