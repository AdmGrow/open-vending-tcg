"""Prueba chica: ES y es cuentan juntos.
"""
from src.catalog import Catalog, PackSku

def test_cuenta_set_idioma():
    cat = Catalog()
    cat.add(PackSku("p1", "tcg-a", "set-1", "es", "booster", 400), 3)
    cat.add(PackSku("p2", "tcg-a", "set-1", "ES", "booster", 400), 2)
    cat.add(PackSku("p3", "tcg-a", "set-1", "en", "blister", 900), 1)
    conteo = cat.stock_por_set_idioma()
    assert conteo["set-1|es"] == 5
    assert conteo["set-1|en"] == 1

if __name__ == "__main__":
    test_cuenta_set_idioma()
    print("ok")
