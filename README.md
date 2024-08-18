# FastHTML meets Django

This project shows how to use FastHTML with Django. 
Django has powerful ORM which can be combined with FastHTML to create fast and efficient web applications.

### How to run
1. Clone the repository
2. Install the requirements `pip install -r requirements.txt`
3. Migrate the database
   * `python manage.py makemigrations`
   * `python manage.py migrate`
4. Populate data `python blog/populate_data.py`
5. Run the app `python blog/main.py`

### Coming soon
1. Django admin integration
2. Django User model integration
