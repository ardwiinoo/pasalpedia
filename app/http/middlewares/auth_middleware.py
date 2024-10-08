from functools import wraps
from flask import session, redirect, url_for, flash


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to be logged in to access this page.', 'error')
            return redirect(url_for('web.show_login'))
        return f(*args, **kwargs)
    return decorated_function