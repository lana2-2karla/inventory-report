from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate_complete_report(cls, products: list, report: str):

        company_name = Counter(
            [product["nome_da_empresa"] for product in products]
        )

        report += "\nProdutos estocados por empresa:\n"

        for company, quantity in company_name.items():
            report += f"- {company}: {quantity}\n"
        return report

    @classmethod
    def generate(cls, products: list):
        simple_report = SimpleReport.generate(products)
        complete_report = cls.generate_complete_report(
            products, simple_report
        )

        return complete_report
