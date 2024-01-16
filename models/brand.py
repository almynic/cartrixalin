from database import db


class Brand(db.Model):
    """
    This class represents a Toner object.

    Attributes:
        id (int): The unique identifier for the color.
        name (str): The name of the brand.

    Methods:
        to_dict(): Converts the toner object to a dictionary representation.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def to_dict(self):
        return {"id": self.id, "name": self.name}
