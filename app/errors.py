from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(erro):
    return render_template('400.html'), 400

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500