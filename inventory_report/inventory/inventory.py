import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str):

        with open(path, mode="r") as file:
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            products_list = list(products)

        if report_type == "simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)
