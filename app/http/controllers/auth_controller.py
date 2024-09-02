from flask import render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.database import db
import re

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
        
    def login():
        return render_template('auth/login/index.html')
     
    def handle_login():
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.query(User).filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # set session
            session['user_id'] = user.id
            session['email'] = user.email
            session['jabatan'] = user.jabatan

            flash('Login successful!', 'success')
            return redirect(url_for('web.show_dashboard_home'))
        else:
            flash('Login failed! Please check your email and password.', 'error')
            return redirect(url_for('web.show_login'))
        
    def logout():
        session.clear()
        
        flash('You have been logged out!', 'success')
        return redirect(url_for('web.show_login'))