# AA FIU Platform

## Technology Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Swagger UI

## Modules

1. Consent Management
2. FI Request Management
3. Financial Data Management
4. Audit Logging
5. Dashboard Summary

## Database Tables

* consents
* fi_requests
* financial_data
* audit_logs

## APIs

### Consent APIs

* Create Consent
* List Consents
* Get Consent By ID

### FI Request APIs

* Create FI Request
* List FI Requests
* Get FI Request By ID

### Financial Data APIs

* Create Financial Data
* List Financial Data
* Get Financial Data By ID

### Audit Log APIs

* Create Audit Log
* List Audit Logs

### Dashboard APIs

* Dashboard Summary

## Compliance

* Consent metadata stored in PostgreSQL
* FI Request metadata stored in PostgreSQL
* Financial data metadata stored in PostgreSQL
* Audit logs maintained for traceability

## Security

* FastAPI request validation using Pydantic
* PostgreSQL persistence layer
* Structured backend architecture

## Observability

* Automatic audit logging for:

  * Consent creation
  * FI Request creation
  * Financial Data creation

## Architecture Flow

Customer
→ Consent
→ FI Request
→ Financial Data
→ Audit Logs
→ Dashboard
