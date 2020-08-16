def is_mail(mail):
    if "@" not in mail:
        return False
    if ".com" not in mail:
        return False
    return True
