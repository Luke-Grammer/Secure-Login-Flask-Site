# app/models.py
# Written by Luke Grammer (12/19/19)

# local imports
from app import db, login_manager

# third-party imports
from flask_security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('users.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('roles.id')))


class Role(RoleMixin, db.Model):
    """
    Create a role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    users = db.relationship('User', secondary='roles_users',
                            backref=db.backref('users', lazy='dynamic'))


class User(UserMixin, db.Model):
    """
    Create a User table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(30), index=True)
    last_name = db.Column(db.String(30), index=True)
    password = db.Column(db.String(255))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    lessons = db.relationship('Lesson', backref='author', lazy='dynamic')
    confirmed_at = db.Column(db.DateTime())
    active = db.Column(db.Boolean())
    admin = db.Column(db.Boolean(), default=False)
    roles = db.relationship('Role', secondary='roles_users',
                            backref=db.backref('roles', lazy='dynamic'))

    def __repr__(self):
        return '<User: %s %s>'.format(self.first_name, self.lastname)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    users = db.relationship('User', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: %s>'.format(self.name)


class Client(db.Model):
    """
    Create a Client table
    """

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    projects = db.relationship('Project', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<Client: %s>'.format(self.name)


class Project(db.Model):
    """
    Create a Project table
    """

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    name = db.Column(db.String(60), index=True, unique=True)
    date = db.Column(db.String(30), index=True)
    architect = db.Column(db.String(60), index=True)
    lessons = db.relationship('Lesson', backref='project', lazy='dynamic')

    def __repr__(self):
        return '<Project: %s>'.format(self.name)


class Lesson(db.Model):
    """
    Create a Lesson table
    """

    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    field = db.Column(db.String(60), index=True)
    subject = db.Column(db.String(80), index=True)
    keywords = db.Column(db.String(80), index=True)
    lesson = db.Column(db.String(255), index=True)

    def __repr__(self):
        return ('<Lesson:\nProject: %s\nSubject: %s\n\n ' +
                'Lesson:\n%s\n(Keywords: %s)>').format(self.project,
                                                       self.subject,
                                                       self.lesson,
                                                       self.keywords)
