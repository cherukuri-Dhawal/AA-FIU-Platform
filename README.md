# AA FIU Platform

## Overview

AA FIU Platform is a Financial Information User (FIU) application built to simulate the Account Aggregator ecosystem. The platform enables consent management, financial information request processing, financial data retrieval, audit logging, and dashboard monitoring through a modern API-driven architecture.

The project demonstrates how an FIU can securely manage customer consent, request financial data, maintain audit trails, and provide operational visibility through a centralized dashboard.

---

## Problem Statement

Financial institutions require a secure and compliant mechanism to access customer financial data through the Account Aggregator framework.

Traditional approaches involve fragmented workflows, limited transparency, and manual tracking of consent and financial data requests.

The objective of this project is to build an FIU platform that:

* Manages customer consent lifecycle
* Processes Financial Information (FI) requests
* Stores and retrieves financial data
* Maintains complete audit logs
* Provides a dashboard for monitoring system activity

---

## Features

### Consent Management

* Create customer consent records
* Store consent details in the database
* Track consent status

### FI Request Management

* Create Financial Information requests
* Link FI requests to consent records
* Track request status

### Financial Data Management

* Store retrieved financial information
* Associate data with FI requests
* Maintain structured records

### Audit Logging

* Automatic audit log generation
* Tracks consent creation
* Tracks FI request creation
* Tracks financial data creation

### Dashboard Analytics

* Total Consents
* Total FI Requests
* Total Financial Data Records
* Total Audit Logs
* Activity visualization using charts

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite/PostgreSQL Compatible

### Frontend

* Streamlit

### Database

* SQLite

### Version Control

* Git
* GitHub

---

## System Architecture

User → Streamlit Frontend → FastAPI Backend → Database

The frontend interacts with FastAPI APIs. FastAPI performs business logic, stores data in the database, and returns responses to the frontend.

---

## API Modules

### Consent APIs

* Create Consent
* List Consents

### FI Request APIs

* Create FI Request
* List FI Requests

### Financial Data APIs

* Create Financial Data
* List Financial Data

### Audit Log APIs

* Create Audit Log
* List Audit Logs

### Dashboard APIs

* Summary Metrics
* Activity Statistics

---

## Project Structure

backend/
├── app/
│ ├── api/
│ ├── models/
│ ├── schemas/
│ ├── services/
│ ├── database/
│ └── main.py

frontend/
└── app.py

screenshots/
README.md
architecture.md

---

## Screenshots

The screenshots folder contains:

* Dashboard
* Consent Management
* FI Requests
* Financial Data
* Audit Logs
* Streamlit Frontend

---

## Key Learnings

* REST API Development using FastAPI
* Database Design using SQLAlchemy
* Financial Data Workflow Modeling
* Audit Logging Implementation
* Streamlit Dashboard Development
* GitHub Project Management

---

## Future Enhancements

* Digio Sandbox Integration
* Account Aggregator API Integration
* JWT Authentication
* Role Based Access Control
* PostgreSQL Production Deployment
* Docker Containerization

---

## Author

Cherukuri Dhawal 

AI/ML and Software Engineering Student, IIT Madras
