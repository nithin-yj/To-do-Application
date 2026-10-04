# To-Do App (Django)
 
A multi-user task manager built with Django. Users register, log in, and manage their own private to-do list with full CRUD.
 
Built as a hands-on project to learn Django's request/response cycle, ORM, forms, authentication, and basic security practices.
 
## Features
 
- User registration with validation (empty fields, duplicate usernames)
- Login / logout with error feedback on wrong credentials
- Create, read, update, and delete tasks
- Mark tasks as Done or Pending from the edit page
- Each user sees only their own tasks
- Ownership enforced on edit and delete (other users' tasks return 404)
- Delete requires a POST request with a confirmation page and CSRF protection
- Pages protected with `@login_required`
## Tech Stack
 
- Python 3
- Django
- SQLite
- HTML
- CSS
## Getting Started
 
```bash
# 1. Clone the repository
git clone https://github.com/nithin-yj/To-do-Application.git
cd To-do-Application
 
# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
 
# 3. Install Django
pip install django
 
# 4. Create the database
python manage.py migrate
 
# 5. Run the server
python manage.py runserver
```
 
Open http://127.0.0.1:8000/ in your browser, register an account, and log in.
 
Optional: create an admin user with `python manage.py createsuperuser` and visit `/admin/`.
 
## URL Routes
 
| URL | Purpose |
|---|---|
| `/register/` | Create an account |
| `/login/` | Log in |
| `/logout/` | Log out |
| `/` | Home page |
| `/list/` | View your tasks |
| `/addtask/` | Add a new task |
| `/edittask/<id>/` | Edit a task |
| `/deletetask/<id>/` | Confirm and delete a task |
 
## Project Structure
 
```
To-do-Application/
├── manage.py
├── static/css           #static files ,added basic UI to make it look good
├── todo_project/        # project settings and root URLs
└── todo/                # app: models, views, forms, urls, templates
    ├── models.py        # Todo model
    ├── views.py         # function-based views
    ├── forms.py         # TodoForm, EditForm
    ├── urls.py
    └── templates/
```
 
## What I Learned
 
- Function-based views and the full CRUD cycle with the Django ORM
- ModelForms, including `save(commit=False)` to attach the logged-in user
- Binding a form to an existing record with `instance=`
- Preventing IDOR by filtering lookups with `get_object_or_404(..., user=request.user)`
- Why destructive actions must use POST, not GET
- Template inheritance and reusable layouts
## Future Improvements
 
- Automated tests
- Due dates and task priorities
- Use Django's built-in auth forms and password validation
- Deployment
