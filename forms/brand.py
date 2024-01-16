from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class BrandForm(FlaskForm):
    name = StringField('Name')

    def to_dict(self):
        # Return a dict but without submit
        return {key: value for key, value in self.data.items() if key != 'submit' and key != 'csrf_token'}


