from flask import Flask
app = Flask(__name__)


from flask import Flask
app = Flask(__name__)



from flask import Blueprint, render_template
from flask_login import  current_user, login_required
site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    #return "Okay"
    print("current_user")
    #print (current_user.to_json())
    return render_template('profile.html')