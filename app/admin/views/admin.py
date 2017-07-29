# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from jinja2 import TemplateNotFound
from flask_security import login_required, current_user
from flask_principal import Permission, ActionNeed
from markupsafe import escape
from app import db
from app.admin.forms import UserForm


test_perm = Permission(ActionNeed('admin.home'))
admin_blueprint = Blueprint('admin', __name__, template_folder='../templates', static_folder='../static')


@admin_blueprint.route('/')
@admin_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    try:
        return render_template('admin/home.html')
    except TemplateNotFound:
        abort(404)


@admin_blueprint.route('/test', methods=('GET', 'POST'))
@test_perm.require(http_exception=403)
def test():
    form = UserForm()
    if form.validate_on_submit():
        flash('Hello,{}'.format(escape(form.username.data)))
        return redirect(url_for('security.home'))
    flash('test messages')
    return render_template('admin/test.html', form=form)





