from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
def create_app():
	application = Flask(__name__)
	Bootstrap(application)
	application.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
	application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://redhat:redhat@people-management-mysql-db/test_cara'
	db.init_app(application)
	migrate = Migrate(application, db)

	from .user import user as user_blueprint
	application.register_blueprint(user_blueprint)
	from .home import home as home_blueprint
	application.register_blueprint(home_blueprint)
	
	return application

# if we create models.py with the following content
# and we add 'from models import User' in the 'create_app' function
# we will meet the following situation:
# 1. we would meet one error ' Table 'user' is already defined for this MetaData instance.'
# 2. If we fix that error, when we run db migration, nothing will happen 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

