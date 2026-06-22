from pydantic import BaseModel


class FinancialDataCreate(BaseModel):
    fi_data_id: str
    fi_request_id: str
    account_id: str
    account_number: str
    fi_type: str
    fip_id: str