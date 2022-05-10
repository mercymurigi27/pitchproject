from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import User


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():

    '''
    View root page function that returns the profile page and its data
    '''
   
    
    return render_template('profile.html')