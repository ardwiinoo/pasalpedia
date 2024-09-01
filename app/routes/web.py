from flask import Blueprint, render_template
from app.http.controllers.auth_controller import AuthController

web_bp = Blueprint('web', __name__)

"""
    AUTHENTIKASI
"""
@web_bp.route('/auth/register', methods=['GET'])
def show_register():
    return AuthController.register()

@web_bp.route('/auth/register', methods=['POST'])
def submit_register():
    return AuthController.handle_register()

"""
    DASHBOARD
"""