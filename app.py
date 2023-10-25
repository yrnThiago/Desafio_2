from app import create_app, db
from flask import render_template

config_name = "development"
app = create_app(config_name)

@app.errorhandler(404)
def not_found(e):
    return render_template('404_not_found.html')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
