**Django Webhook Service**

A Django-based webhook service that provides user authentication, account management, and data-pushing functionalities with asynchronous processing.

🚀 Features

✅ User Signup & Login (JWT Authentication)

✅ Role-based Authorization (Admin, Normal User)

✅ CRUD APIs for Accounts, Destinations, and Logs

✅ Asynchronous Data Processing (Celery + Redis)

✅ Rate Limiting & Throttling

✅ Swagger API Documentation

✅ Web-based User Authentication & Dashboard


⚙️ Installation
1️⃣ Clone the Repository

git clone https://github.com/harshareen-2024/django-webhook-service.git

cd django-webhook-service
Download required packages 
python manage.py runserver
Starting development server at http://127.0.0.1:8000/


![image](https://github.com/user-attachments/assets/af316af5-973b-4b95-bef7-d9b85f73f47a)


2️⃣ Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate  
On Windows use: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations client
python manage.py migrate

5️⃣ Create a Superuser
  python manage.py createsuperuser

6️⃣ Start the Development Server
python manage.py runserver


**API Endpoints**
Authentication APIs
Account Management APIs
Account Member APIs
Destination APIs
Log APIs
Webhook Data API

**🚀 Technologies Used**

Django & Django REST Framework for backend API

PostgreSQL / SQLite for database management

JWT Authentication for security

Celery + Redis for asynchronous tasks

Swagger (drf-yasg) for API documentation

Docker (optional) for containerized deployment
