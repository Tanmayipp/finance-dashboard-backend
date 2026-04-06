

#  Finance Dashboard Backend

A backend system built using FastAPI for managing financial records with role-based access control.
This project demonstrates API design, data modeling, business logic structuring, and backend architecture.

---

##  Features

*  **User & Role Management**

  * Roles: `Admin`, `Analyst`, `Viewer`
  * Role-based access control using dependencies

*  **Financial Records Management**

  * Create, read, update, delete records
  * Fields: amount, type, category, date, notes
  * Filtering by type, category, and date range

* **Dashboard APIs**

  * Total income
  * Total expenses
  * Net balance

*  **Access Control**

  * Admin → full access
  * Analyst → read + insights
  * Viewer → read-only

*  **Validation & Error Handling**

  * Input validation using Pydantic
  * Proper HTTP status codes

---

## Project Structure

```
app/
│── core/        # Security (RBAC)
│── models/      # SQLAlchemy models
│── schemas/     # Pydantic schemas
│── services/    # Business logic layer
│── routes/      # API endpoints
│── database.py  # DB configuration
│── main.py      # App entry point
```

---

## Tech Stack

* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Tanmayipp/finance-dashboard-backend.git
cd finance-dashboard-backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the server

```
uvicorn app.main:app --reload
```

---

##  API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔄 Example API Flow

1. Create Record → `POST /records/`
2. Get Records → `GET /records/`
3. Update Record → `PUT /records/{id}`
4. Delete Record → `DELETE /records/{id}`

---

##  Design Decisions

* Used **service layer** for clean separation of logic
* Implemented **role-based access control** using dependencies
* Used **Enums** for consistent role and type handling
* Structured project for **scalability and maintainability**

---

##  Assumptions

* Authentication is mocked (no JWT implemented)
* Single-user context for demonstration
* SQLite used for simplicity

---

##  Future Improvements

* JWT-based authentication
* Pagination & search
* Advanced analytics (monthly trends, charts)
* Production-ready deployment

---


## API Preview

Below is a preview of the Swagger UI for interacting with the API:

![Swagger UI](screenshotfin.png)

## AUTHOR - TANMAYI P