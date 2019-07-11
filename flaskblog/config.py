import os
class Config:
	 SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'#os.environ.get('FLASK_SECRET_KEY')
	 SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'#os.environ.get('FLASK_DB')
	 MAIL_SERVER='smtp.gmail.com'
	 MAIL_PORT= 587
	 MAIL_USE_TLS=True
	 EMAIL_HOST_USER = os.environ.get('GMAIL_USER')
	 EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')