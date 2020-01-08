# app/admin/views.py
# Written by Luke Grammer (12/19/19)

from flask import abort, flash, redirect, render_template, url_for
from flask_security import current_user, login_required
from sqlalchemy import exc

from . import admin
from .forms import DepartmentForm, RoleForm
from .. import db
from ..models import Department, Role


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.admin:
        abort(403)


# Department Views
@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department  to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data)
        try:
            # add department to db
            db.session.add(department)
            db.session.commit()
            flash("'" + department.name + "' has been successfully added.")
        except exc.SQLAlchemyError:
            # if department already exists
            flash("Error: department name already exists", "error")

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        try:
            # add department to db
            department.name = form.name.data
            db.session.commit()
            flash("Department has been successfully modified.")
        except exc.SQLAlchemyError:
            # if department already exists
            flash("Error: department name already exists", "error")

        return redirect(url_for('admin.list_departments'))

    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to departments page
    return redirect(url_for('admin.list_departments'))


# Role Views
@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data)

        try:
            # add role to database
            db.session.add(role)
            db.session.commit()
            flash("'" + role.name + "' successfully added.")
        except exc.SQLAlchemyError:
            flash('Error: role name already exists.', 'error')

        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        try:
            role.name = form.name.data
            # add updated role to database
            db.session.add(role)
            db.session.commit()
            flash("Role successfully updated.")
        except exc.SQLAlchemyError:
            flash('Error: role name already exists.', 'error')

        return redirect(url_for('admin.list_roles'))

    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to roles page
    return redirect(url_for('admin.list_roles'))
