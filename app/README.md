 FastAPI ML Prediction Project

This project is a FastAPI-based backend application that performs machine learning predictions on the Iris dataset.  
It is designed using a clean, layered architecture to demonstrate proper backend structuring, validation, and ML integration.

---

 Project Overview

- Backend developed using FastAPI
- Machine Learning model integrated using scikit-learn and joblib
- Data validation handled using Pydantic
- Database operations managed using SQLAlchemy
- REST APIs exposed for prediction history management
- Frontend can consume APIs independently

---

 Project Structure

app/
├── api/ 
├── db/ 
├── models/ 
├── repositories/ 
├── schemas/ 
├── services/ 
├── init.py
└── main.py 


---

 Technologies Used

- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Scikit-learn
- Joblib
- Uvicorn

---

Features

- Machine learning-based Iris species prediction
- Input validation using Pydantic schemas
- Persistent storage of predictions
- CRUD operations (Create, Read, Update, Delete)
- Clean separation of concerns using layered architecture
- Swagger UI for API testing

---

How to Run the Project

 1. Create a virtual environment

    python -m venv venv
 
 2. Activate Venv
    pip install -r requirements.txt

 3. Start the server
    uvicorn app.main:app --reload


 
