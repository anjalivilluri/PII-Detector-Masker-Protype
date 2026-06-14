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

from detector.masker import (
    mask_email,
    mask_phone,
    mask_pan,
    mask_aadhaar
)


def test_mask_email():

    assert (
        mask_email(
            "rahul@gmail.com"
        )
        ==
        "r****@gmail.com"
    )


def test_mask_phone():

    assert (
        mask_phone(
            "9876543210"
        )
        ==
        "98******10"
    )


def test_mask_pan():

    assert (
        mask_pan(
            "ABCDE1234F"
        )
        ==
        "A********F"
    )


def test_mask_aadhaar():

    assert (
        mask_aadhaar(
            "123456789012"
        )
        ==
        "********9012"
    )