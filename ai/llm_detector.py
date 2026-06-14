def llm_detect(text):
    """
    Simulated LLM layer (rule-based fallback)
    """

    text = str(text)

    if "@" in text:
        return "EMAIL"

    if text.isdigit() and len(text) == 10:
        return "PHONE"

    if text.isdigit() and len(text) == 12:
        return "AADHAAR"

    if len(text) == 10 and any(c.isdigit() for c in text):
        return "PAN"

    return "NOT_PII"