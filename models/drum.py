from database import db


class Drum(db.Model):
    """
    This class represents a Drum object.

    Attributes:
        id (int): The unique identifier for the drum.
        brand (str): The brand of the drum.
        name (str): The name of the drum.
        color (str): The color of the drum.
        scope_of_delivery (str): The scope of delivery for the drum.
        cartridge_no (str): The cartridge number of the drum.
        compatible_printers (str): The compatible printers for the drum.
        max_printable_pages (int): The maximum number of printable pages for the drum.

    Methods:
        to_dict(): Converts the drum object to a dictionary representation.
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
    max_printable_pages = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "brand": self.brand, "name": self.name, "color": self.color,
                "scope_of_delivery": self.scope_of_delivery, "cartridge_no": self.cartridge_no,
                "cartridge_size": self.cartridge_size, "compatible_printers": self.compatible_printers,
                "max_printable_pages": self.max_printable_pages}
