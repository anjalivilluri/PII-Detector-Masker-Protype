import json

from detector.regex_detector import detect_pii

from detector.masker import (
    mask_email,
    mask_phone,
    mask_pan,
    mask_aadhaar
)


def process_json():

    with open(
        "input/sample.json",
        "r"
    ) as file:

        data = json.load(file)

    report = {
        "EMAIL": 0,
        "PHONE": 0,
        "PAN": 0,
        "AADHAAR": 0
    }

    for record in data:

        for key, value in record.items():

            pii_type = detect_pii(value)

            if pii_type in report:

                report[pii_type] += 1

            if pii_type == "EMAIL":

                record[key] = mask_email(value)

            elif pii_type == "PHONE":

                record[key] = mask_phone(value)

            elif pii_type == "PAN":

                record[key] = mask_pan(value)

            elif pii_type == "AADHAAR":

                record[key] = mask_aadhaar(value)

    with open(
        "output/masked.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    report["TOTAL_PII_FOUND"] = (
        report["EMAIL"]
        + report["PHONE"]
        + report["PAN"]
        + report["AADHAAR"]
    )

    with open(
        "output/report_json.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    print("JSON Processing Completed")