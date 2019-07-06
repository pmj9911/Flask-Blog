from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,ValidationError
from flaskblog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
	username = StringField('Username' , validators = [DataRequired(), Length(min =2, max =20)]) 
	email = StringField('Email',validators=[DataRequired(),		Email()])
	password = PasswordField('password',validators=[DataRequired()])
	confirm_password = PasswordField('confirm password',validators=[DataRequired(),	EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_email(self , email):

		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('email already exists.')
	def validate_username(self , username):

		user = User.query.filter_by(username=username.data).first()
		if user :
			raise ValidationError('username already exists. Please choose another username')

class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),	Email()])
	password = PasswordField('password',validators=[DataRequired()])
	confirm_password = PasswordField('confirm password',validators=[DataRequired(),	EqualTo('password')])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username' , validators = [DataRequired(), Length(min =2, max =20)]) 
	email = StringField('Email',validators=[DataRequired(),		Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
	submit = SubmitField('Update')

	def validate_email(self , email):
		if email.data != current_user.email :
			email = User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError('email already exists.')
	def validate_username(self , username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user :
				raise ValidationError('username already exists. Please choose another username')

class PostForm(FlaskForm):
	title = StringField('title', validators=[DataRequired()]
		)
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')