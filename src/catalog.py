"""Lista de sobres. Nombres genericos, no de juegos reales.
"""
from dataclasses import dataclass

@dataclass
class PackSku:
    sku: str
    game: str          # tcg-a, tcg-b
    set_code: str
    language: str
    pack_type: str     # booster | blister | tin
    price_cents: int
    sealed: bool = True

class Catalog:
    def __init__(self):
        self.items = {}

    def add(self, sku: PackSku):
        if not sku.sealed:
            raise ValueError("only sealed product")
        self.items[sku.sku] = sku

    def price(self, sku: str) -> int:
        return self.items[sku].price_cents
