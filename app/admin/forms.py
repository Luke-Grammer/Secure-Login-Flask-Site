# app/admin/forms.py
# Written by Luke Grammer (12/19/19)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Role


class DepartmentForm(FlaskForm):
    """
    For for admin to add or edit departments
    """
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):
    """
    For admins to edit user roles
    """
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')
