from flask import Blueprint, render_template, session
from app.decorators import login_required

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard', template_folder='../templates/dashboard')

@dashboard_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', usuario=session['usuario'])
