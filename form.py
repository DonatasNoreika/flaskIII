from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class QueryForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    surname = StringField('Pavardė', [DataRequired()])
    email = StringField('El. paštas', [Email(message=('Neteisingas adresas.')), DataRequired()])
    phone = StringField('Tel. numeris', [DataRequired()])
    message = TextAreaField('Komentaras')
    submit = SubmitField('Įvesti')
