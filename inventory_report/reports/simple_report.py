from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def ConvertToDate(cls, text: str):
        return date.fromisoformat(text)

    @classmethod
    def generate(cls, products: list):

        manufacturing_date = [
            product["data_de_fabricacao"] for product in products
        ]

        oldest_manufacturing_date = min(manufacturing_date)

        expiration_date = [
            cls.ConvertToDate(product["data_de_validade"])
            for product in products
            if cls.ConvertToDate(product["data_de_validade"]) >= date.today()
        ]

        most_current_expiration_date = min(expiration_date)

        company_name = Counter(
            [product["nome_da_empresa"] for product in products]
        ).most_common(1)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"""Data de validade mais próxima: {
                most_current_expiration_date
                }\n"""
            f"Empresa com mais produtos: {company_name[0][0]}"
        )
