from flask import Blueprint, redirect
from app.http.controllers.auth_controller import AuthController
from app.http.controllers.home_controller import HomeController
from app.http.middlewares.auth_middleware import auth_required    

web_bp = Blueprint('web', __name__)

@web_bp.route('/', methods=['GET'])
def toLogin():
    return redirect('/auth/login')

"""
    AUTHENTIKASI
"""
@web_bp.route('/auth/register', methods=['GET'])
def show_register():
    return AuthController.register()

@web_bp.route('/auth/register', methods=['POST'])
def submit_register():
    return AuthController.handle_register()

@web_bp.route('/auth/login', methods=['GET'])
def show_login():
    return AuthController.login()

@web_bp.route('/auth/login', methods=['POST'])
def submit_login():
    return AuthController.handle_login()

@web_bp.route('/auth/logout', methods=['POST'])
def submit_logout():
    return AuthController.logout()

"""
    DASHBOARD
"""
@web_bp.route('/dashboard', methods=['GET'])
@auth_required
def show_dashboard_home():
    return HomeController.home()