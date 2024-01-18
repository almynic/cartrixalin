from database import db


class Ink(db.Model):
    """
    This class represents a Ink object.

    Attributes:
        id (int): The unique identifier for the ink cartridge.
        brand (str): The brand of the ink cartridge.
        name (str): The name of the ink cartridge.
        color (str): The color of the ink cartridge.
        scope_of_delivery (str): The scope of delivery for the ink cartridge.
        cartridge_no (str): The cartridge number of the ink cartridge.
        cartridge_size (str): The cartridge size of the ink cartridge.
        compatible_printers (str): The compatible printers for the ink cartridge.
        fill_capacity (int): The fill capacity for the ink cartridge.

    Methods:
        to_dict(): Converts the toner object to a dictionary representation.
    """
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))
    scope_of_delivery = db.Column(db.String(100))
    cartridge_no = db.Column(db.String(50))
    cartridge_size = db.Column(db.String(2))
    cartridge_type = db.Column(db.String(50))
    compatible_printers = db.Column(db.String(200))
    fill_capacity = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "brand": self.brand, "name": self.name, "color": self.color,
                "scope_of_delivery": self.scope_of_delivery, "cartridge_no": self.cartridge_no,
                "cartridge_size": self.cartridge_size, "cartridge_type": self.cartridge_type,
                "compatible_printers": self.compatible_printers, "fill_capacity": self.fill_capacity}
