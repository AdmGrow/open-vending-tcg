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
        self.stock = {}  # sku -> cantidad

    def add(self, sku: PackSku, qty: int = 0):
        if not sku.sealed:
            raise ValueError("only sealed product")
        self.items[sku.sku] = sku
        self.stock[sku.sku] = qty

    def price(self, sku: str) -> int:
        return self.items[sku].price_cents

    def get_stock(self, sku: str) -> int:
        return self.stock.get(sku, 0)

    def set_stock(self, sku: str, qty: int):
        if sku not in self.items:
            raise KeyError("sku no esta en catalogo")
        if qty < 0:
            raise ValueError("stock no puede ser negativo")
        self.stock[sku] = qty

    def adjust_stock(self, sku: str, delta: int):
        """Suma o resta stock. No deja ir debajo de 0."""
        actual = self.get_stock(sku)
        nuevo = actual + delta
        if nuevo < 0:
            raise ValueError("stock insuficiente")
        self.set_stock(sku, nuevo)

    def stock_por_set_idioma(self):
        """Cuenta sobres por set e idioma. Clave: set_code|language."""
        conteo = {}
        for sku, item in self.items.items():
            clave = item.set_code + "|" + item.language
            conteo[clave] = conteo.get(clave, 0) + self.get_stock(sku)
        return conteo


if __name__ == "__main__":
    cat = Catalog()
    cat.add(PackSku("p1", "tcg-a", "set-1", "es", "booster", 400), 3)
    cat.add(PackSku("p2", "tcg-a", "set-1", "es", "booster", 400), 2)
    cat.add(PackSku("p3", "tcg-a", "set-1", "en", "blister", 900), 1)
    print(cat.stock_por_set_idioma())
    # set-1|es = 5, set-1|en = 1
