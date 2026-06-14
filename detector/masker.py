def mask_email(email):

    username, domain = email.split("@")

    return username[0] + "****@" + domain
def mask_phone(phone):
    phone = str(phone)
    return phone[:2] + "******" + phone[-2:]
def mask_pan(pan):
    return pan[0] + "********" + pan[-1]
def mask_aadhaar(aadhaar):
    aadhaar = str(aadhaar)
    return "********" + aadhaar[-4:]