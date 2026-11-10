"""Prueba chica: ES y es cuentan juntos. Vacio da 0.
Tambien pruebo que adjust no deje stock negativo.
Y que idiomas_de_set solo liste los que tienen stock.
"""
from src.catalog import Catalog, PackSku

def test_cuenta_set_idioma():
    cat = Catalog()
    assert cat.total_sobres() == 0
    assert cat.stock_de("set-1", "es") == 0
    cat.add(PackSku("p1", "tcg-a", "set-1", "es", "booster", 400), 3)
    cat.add(PackSku("p2", "tcg-a", "set-1", "ES", "booster", 400), 2)
    cat.add(PackSku("p3", "tcg-a", "set-1", "en", "blister", 900), 1)
    conteo = cat.stock_por_set_idioma()
    assert conteo["set-1|es"] == 5
    assert conteo["set-1|en"] == 1
    assert cat.stock_de("set-1", "es") == 5
    assert cat.stock_de("set-1", "EN") == 1
    assert cat.tiene_stock("set-1", "es")
    assert not cat.tiene_stock("set-2", "es")
    assert cat.total_sobres() == 6
    assert sorted(cat.skus_con_stock()) == ["p1", "p2", "p3"]
    # idiomas que tienen stock
    assert sorted(cat.idiomas_de_set("set-1")) == ["en", "es"]

def test_adjust_no_negativo():
    cat = Catalog()
    cat.add(PackSku("p1", "tcg-a", "set-1", "es", "booster", 400), 2)
    cat.adjust_stock("p1", -1)
    assert cat.get_stock("p1") == 1
    try:
        cat.adjust_stock("p1", -2)
        assert False, "deberia fallar"
    except ValueError:
        pass
    assert cat.get_stock("p1") == 1

if __name__ == "__main__":
    test_cuenta_set_idioma()
    test_adjust_no_negativo()
    print("ok")
