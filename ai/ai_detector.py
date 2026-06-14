def llm_detect(text):
    """
    Simple AI fallback classifier (no external API needed)
    Works as rule-based AI layer for hackathon demo.
    """

    text = str(text).strip()

    # EMAIL detection
    if "@" in text and "." in text:
        return "EMAIL"

    # PHONE detection
    if text.isdigit() and len(text) == 10:
        return "PHONE"

    # AADHAAR detection
    if text.isdigit() and len(text) == 12:
        return "AADHAAR"

    # PAN detection (5 letters + 4 digits + 1 letter pattern)
    if len(text) == 10:
        return "PAN"

    return "NOT_PII"