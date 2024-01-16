from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField

from models.brand import Brand
from models.color import Color


class TonerForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(TonerForm, self).__init__(*args, **kwargs)
        # Query the database for brands
        self.brand.choices = [(b.id, b.name) for b in Brand.query.all()]
        self.color.choices = [(c.id, c.name) for c in Color.query.all()]

    name = StringField('Name')
    brand = SelectField('Brand', coerce=int)
    color = SelectField('Color', coerce=int)
    cartridge_no = StringField('Cartridge No')
    compatible_printers = StringField('Compatible Printers')
    submit = SubmitField('Submit')

    def to_dict(self):
        # Return a dict but without submit
        return {key: value for key, value in self.data.items() if key != 'submit' and key != 'csrf_token'}
