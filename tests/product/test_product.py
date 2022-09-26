from inventory_report.inventory.product import Product


def test_cria_produto():
    result_product = Product(
        8,
        "Aspirin",
        "Galena Biopharma",
        "2021-02-22",
        "2024-03-14",
        "KZ63 800H NM4B ZOWB YYUI",
        "instrucao 8"
    )

    assert result_product.id == 8
    assert result_product.nome_do_produto == "Aspirin"
    assert result_product.nome_da_empresa == "Galena Biopharma"
    assert result_product.data_de_fabricacao == "2021-02-22"
    assert result_product.data_de_validade == "2024-03-14"
    assert result_product.numero_de_serie == "KZ63 800H NM4B ZOWB YYUI"
    assert result_product.instrucoes_de_armazenamento == "instrucao 8"
