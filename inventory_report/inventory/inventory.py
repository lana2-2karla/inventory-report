import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str):

        products_list = cls.check_file_type(path)

        if report_type == "simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)

    @classmethod
    def check_file_type(cls, path: str):
        with open(path, mode="r") as file:
            if path.endswith(".csv"):
                products = csv.DictReader(file, delimiter=",", quotechar='"')
                return list(products)
            if path.endswith(".json"):
                return json.load(file)
