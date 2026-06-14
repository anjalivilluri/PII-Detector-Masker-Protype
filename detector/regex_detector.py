import re
from ai.ai_detector import llm_detect

EMAIL_PATTERN = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
PHONE_PATTERN = r'\b[6-9]\d{9}\b'
PAN_PATTERN = r'\b[A-Z]{5}[0-9]{4}[A-Z]\b'
AADHAAR_PATTERN = r'\b\d{12}\b'

def detect_email(value):

    return bool(
        re.fullmatch(
            EMAIL_PATTERN,
            
            str(value)
        )
    )

def detect_phone(value):

    return bool(
        re.fullmatch(
            PHONE_PATTERN,
            str(value)
        )
    )

def detect_pan(value):

    return bool(
        re.fullmatch(
            PAN_PATTERN,
            str(value)
        )
    )

def detect_aadhaar(value):

    return bool(
        re.fullmatch(
            AADHAAR_PATTERN,
            str(value)
        )
    )
def detect_pii(value):

    value = str(value)

    if detect_email(value):

        return "EMAIL"

    elif detect_phone(value):

        return "PHONE"

    elif detect_pan(value):

        return "PAN"

    elif detect_aadhaar(value):

        return "AADHAAR"

    ai_result = llm_detect(value)

    return ai_result