from detector.regex_detector import detect_pii


def test_email_detection():

    assert (
        detect_pii(
            "rahul@gmail.com"
        )
        ==
        "EMAIL"
    )


def test_phone_detection():

    assert (
        detect_pii(
            "9876543210"
        )
        ==
        "PHONE"
    )


def test_pan_detection():

    assert (
        detect_pii(
            "ABCDE1234F"
        )
        ==
        "PAN"
    )


def test_aadhaar_detection():

    assert (
        detect_pii(
            "123456789012"
        )
        ==
        "AADHAAR"
    )


def test_non_pii():

    assert (
        detect_pii(
            "Rahul Kumar"
        )
        ==
        "NOT_PII"
    )