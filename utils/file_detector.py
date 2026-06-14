import os


def detect_file_type():

    if os.path.exists(
        "input/sample.csv"
    ):

        return "CSV"

    if os.path.exists(
        "input/sample.json"
    ):

        return "JSON"

    return "NONE"