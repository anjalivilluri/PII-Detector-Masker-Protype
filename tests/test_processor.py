import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pandas as pd

from processors.web_processor import (
    process_uploaded_csv
)


def test_csv_processing():

    df = pd.DataFrame({

        "Name":
        ["Rahul"],

        "Email":
        ["rahul@gmail.com"],

        "Phone":
        ["9876543210"]

    })

    df.to_csv(
        "sample_test.csv",
        index=False
    )

    report, file = (
        process_uploaded_csv(
            "sample_test.csv"
        )
    )

    assert report["EMAIL"] == 1

    assert report["PHONE"] == 1