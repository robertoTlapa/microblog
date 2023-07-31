from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Nombre usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Iniciar sesión')


class RegistrationForm(FlaskForm):
    username = StringField('Nombre usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email('email')])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    rep_password = PasswordField('Repetir contraseña', validators=[
                                 DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor ravisa el nombre de usuario.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor revisa el email.')


class EditProfileForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    about_me = TextAreaField('Acerca de mi', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enviar')
    
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Por favor usa un nombre de usuario diferente') 