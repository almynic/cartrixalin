from database import db

# Toner properties
BRAND = "brand"
NAME = "name"
COLOR = "color"
SCOPE_OF_DELIVERY = "scope_of_delivery"
CARTRIDGE_NO = "cartridge_no"
COMPATIBLE_PRINTERS = "compatible_printers"
MAX_PRINTABLE_PAGES = "max_printable_pages"


class Toner(db.Model):
    """
    This class represents a Toner object.

    Attributes:
        id (int): The unique identifier for the toner.
        brand (str): The brand of the toner.
        name (str): The name of the toner.
        color (str): The color of the toner.
        scope_of_delivery (str): The scope of delivery for the toner.
        cartridge_no (str): The cartridge number of the toner.
        compatible_printers (str): The compatible printers for the toner.
        max_printable_pages (int): The maximum number of printable pages for the toner.

    Methods:
        to_dict(): Converts the toner object to a dictionary representation.
    """
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))
    scope_of_delivery = db.Column(db.String(100))
    cartridge_no = db.Column(db.String(50))
    compatible_printers = db.Column(db.String(200))
    max_printable_pages = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, BRAND: self.brand, NAME: self.name, COLOR: self.color,
                SCOPE_OF_DELIVERY: self.scope_of_delivery, CARTRIDGE_NO: self.cartridge_no,
                COMPATIBLE_PRINTERS: self.compatible_printers, MAX_PRINTABLE_PAGES: self.max_printable_pages}
