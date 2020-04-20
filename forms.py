from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional

class AddCupcakeForm(FlaskForm):
    """Form for adding cupcake"""

    flavor = StringField('Cupcake Flavor', validators=[InputRequired()])
    size = StringField('Cupcake Size', validators=[InputRequired])
    price = FloatField('Cupcake Price', validators=[InputRequired])
