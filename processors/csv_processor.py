import pandas as pd

from detector.regex_detector import detect_pii

from detector.masker import (
    mask_email,
    mask_phone,
    mask_pan,
    mask_aadhaar
)


def process_csv():

    df = pd.read_csv(
        "input/sample.csv",
        dtype=str
    )

    report = {
        "EMAIL": 0,
        "PHONE": 0,
        "PAN": 0,
        "AADHAAR": 0
    }

    for column in df.columns:

        for index, value in enumerate(df[column]):

            pii_type = detect_pii(value)

            if pii_type in report:

                report[pii_type] += 1

            if pii_type == "EMAIL":

                df.at[index, column] = mask_email(value)

            elif pii_type == "PHONE":

                df.at[index, column] = mask_phone(value)

            elif pii_type == "PAN":

                df.at[index, column] = mask_pan(value)

            elif pii_type == "AADHAAR":

                df.at[index, column] = mask_aadhaar(value)

    df.to_csv(
        "output/masked.csv",
        index=False
    )

    report["TOTAL_PII_FOUND"] = sum(
        report.values()
    )

    return report