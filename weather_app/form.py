from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired


class AccessWeather(FlaskForm):
    city = StringField("City", validators=[DataRequired()])
    country = SelectField("Country", coerce=str, validators=[InputRequired()])
    submit = SubmitField("Search")