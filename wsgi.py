from main import app as application
from main import db

if __name__ == '__main__':
    application.app_context().push()
    db.drop_all()
    db.create_all()
    application.run(debug=True)
