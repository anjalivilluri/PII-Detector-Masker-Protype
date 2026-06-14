import json


def generate_report(report_data):

    with open(
        "output/report.json",
        "w"
    ) as file:

        json.dump(
            report_data,
            file,
            indent=4
        )