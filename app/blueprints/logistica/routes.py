from flask import render_template, redirect, url_for
from flask_login import login_required
from . import logistica_bp



@logistica_bp.route('/')
@login_required
def index():
    return render_template('private/logistica/home.html')