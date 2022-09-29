from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def ConvertToDate(cls, text: str):
        return datetime.strptime(text, "%Y-%m-%d")

    @classmethod
    def generate(cls, products: list):

        manufacturing_date = [
            product["data_de_fabricacao"] for product in products
        ]

        oldest_manufacturing_date = min(manufacturing_date)

        expiration_date = [
            cls.ConvertToDate(product["data_de_validade"])
            for product in products
            if cls.ConvertToDate(product["data_de_validade"]) <= datetime.now()
        ]
        print(expiration_date)
        most_current_expiration_date = max(expiration_date)

        company_name = max(
            Counter([product["nome_da_empresa"] for product in products])
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}"
            f"Data de validade mais próxima: {most_current_expiration_date}"
            f"Empresa com mais produtos: {company_name}"
        )
