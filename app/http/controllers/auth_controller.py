from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
from app.models.user import User
from app.database import db

class AuthController:
    def register():
        return render_template('auth/register/index.html')
    
    def handle_register():
        email = request.form.get('email')
        jabatan = request.form.get('jabatan')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(
            email=email, 
            password=hashed_password, 
            jabatan=jabatan
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            flash('Account created successfully!', 'success')
            return redirect(url_for('web.show_register'))
        except:
            db.session.rollback()
            flash('Error creating account. Please try again.', 'error')
            return redirect(url_for('web.show_register'))