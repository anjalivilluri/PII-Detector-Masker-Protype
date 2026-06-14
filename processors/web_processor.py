import pandas as pd
import json

from detector.regex_detector import detect_pii

from detector.masker import (
    mask_email,
    mask_phone,
    mask_pan,
    mask_aadhaar
)


def process_uploaded_csv(file_path):

    df = pd.read_csv(
        file_path,
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

            value = str(value)

            pii_type = detect_pii(value)

# -----------------------------
# AI FALLBACK LAYER (IMPORTANT)
# -----------------------------
            if pii_type == "NOT_PII":
             from ai.llm_detector import llm_detect
            pii_type = llm_detect(value)

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

    outputs_file = "outputs/masked.csv"

    df.to_csv(
        outputs_file,
        index=False
    )

    report["TOTAL_PII_FOUND"] = (
        report["EMAIL"]
        + report["PHONE"]
        + report["PAN"]
        + report["AADHAAR"]
    )

    total_records = len(df)

    if total_records > 0:

        compliance_score = max(
            0,
            100 - (
                report["TOTAL_PII_FOUND"] * 5
            )
        )

    else:

        compliance_score = 100

    report["COMPLIANCE_SCORE"] = compliance_score

    report["EMAIL_WIDTH"] = report["EMAIL"] * 20

    report["PHONE_WIDTH"] = report["PHONE"] * 20

    report["PAN_WIDTH"] = report["PAN"] * 20

    report["AADHAAR_WIDTH"] = report["AADHAAR"] * 20

    # --------------------
    # SAVE SCAN HISTORY
    # --------------------

    history = []

    try:

        with open(
            "data/scan_history.json",
            "r"
        ) as file:

            history = json.load(file)

    except:

        history = []

    history.append({

        "emails":
        report["EMAIL"],

        "phones":
        report["PHONE"],

        "pan":
        report["PAN"],

        "aadhaar":
        report["AADHAAR"],

        "total":
        report["TOTAL_PII_FOUND"],

        "compliance":
        report["COMPLIANCE_SCORE"]

    })

    with open(
        "data/scan_history.json",
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )

    return report, outputs_file