
# Flask CMS

MVP for creating a content management system with Flask. I use poetry for the pip dependances : flask, flask-login and flask-sqlalchemy. User can create account post and delete his own notes.

## Installation

Install FlaskCMS with poetry

```bash
  git clone FlaskCMS
  cd FlaskCMS
```
if you dont have poetry :
```bash
  pip install poetry
```
Launch the app : 
```bash
  poetry run flask run
```
    
## Database
i use sqlalchemy for database building with 2 class Note and User

```python
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
```


## Screenshots

![App Screenshot](https://i.ibb.co/DVQ5Q6c/Capture-d-e-cran-2024-09-23-a-13-01-46.png)


## To-Do

- Switch from Bootstrap to Tailwind

- Add images to post

- add unit testing