from inventory_report.inventory.product import Product


def test_relatorio_produto():
    result_product = Product(
        8,
        "Aspirin",
        "Galena Biopharma",
        "2021-02-22",
        "2024-03-14",
        "KZ63 800H NM4B ZOWB YYUI",
        "instrucao 8"
    )

    result_rpr = Product.__repr__(result_product)
    assert result_rpr == (
        f"O produto {result_product.nome_do_produto}"
        f" fabricado em {result_product.data_de_fabricacao}"
        f" por {result_product.nome_da_empresa} com validade"
        f" até {result_product.data_de_validade}"
        f" precisa ser armazenado {result_product.instrucoes_de_armazenamento}."
    )
