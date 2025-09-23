# Django Documentation – Complete Guide

This repository contains a Django project (`Django_Documentation`) with apps, database, and workflow examples.  
It is designed as a step-by-step learning and reference resource for developers, covering basics to advanced Django concepts.

---

## Project Structure

```
Django-Documentation/
│── .github/workflows/     # CI/CD workflows (GitHub Actions)
│── Django_Documentation/  # Project settings and configurations
│── polls/                 # Example Django app (Polls Application)
│── venv/                  # Virtual environment (not required to push usually)
│── db.sqlite3             # SQLite database file
│── manage.py              # Django project management script
```

---

## Getting Started

### 1. Install Dependencies
```
pip install django
```

### 2. Start Development Server
```
python manage.py runserver
```

### 3. Create Superuser (Admin Access)
```
python manage.py createsuperuser
```

### 4. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

---

## Django Basics

- **Project vs App**  
  - Project: The entire configuration and collection of apps.  
  - App: A modular component (e.g., polls, blog).  

- **manage.py**: Command-line utility for Django.  
- **settings.py**: Global configurations (databases, installed apps, middleware).  
- **urls.py**: URL routing system.  
- **views.py**: Handles logic and returns responses.  
- **models.py**: Defines database schema using ORM.  
- **templates/**: HTML templates with Django Template Language (DTL).  

---

## Intermediate Concepts

1. **Django ORM**  
   - Simplifies database operations using Python classes.  
   - Example: `Worker.objects.filter(department="IT")`

2. **Admin Panel**  
   - Auto-generated CRUD interface for models.  

3. **Forms and ModelForms**  
   - Simplify form rendering and validation.  

4. **Middleware**  
   - Hooks that process request/response objects globally.  

5. **Static and Media Files**  
   - Static: CSS, JS, Images.  
   - Media: User-uploaded content.  

---

## Advanced Concepts

1. **Authentication and Authorization**  
   - User model, groups, permissions.  

2. **Class-Based Views (CBVs)**  
   - Reusable and organized alternative to function-based views.  

3. **REST APIs with Django REST Framework (DRF)**  
   - Build APIs using serializers, viewsets, and routers.  

4. **Caching**  
   - Improve performance with in-memory caching (Redis, Memcached).  

5. **Signals**  
   - Trigger actions on events (e.g., after saving a model).  

6. **Testing**  
   - Unit tests and integration tests using Django’s `TestCase`.  

7. **Security**  
   - CSRF protection, SQL injection prevention, HTTPS enforcement.  

---

## Expert Level

1. **Custom Middleware**  
   - Write your own request/response handlers.  

2. **Custom User Models**  
   - Replace default user with extended fields.  

3. **Asynchronous Views**  
   - Use `async` views for concurrency (Django 3.1+).  

4. **Celery Integration**  
   - Distributed task queue for background jobs.  

5. **Deployment**  
   - Gunicorn + Nginx, Docker, or cloud platforms.  

6. **CI/CD with GitHub Actions**  
   - Automate testing and deployment pipelines.  

---

## How to Use This Repository

1. Clone the repository  
   ```
   git clone https://github.com/<your-username>/Django-Documentation.git
   cd Django-Documentation
   ```

2. Activate virtual environment (optional but recommended).  
3. Run the project and explore apps like `polls`.  
4. Extend by adding new apps and practicing features.  

---

## Author
**Srijan Saraswat**  

---

## License
This project is licensed under the MIT License.
