import re
from datetime import datetime
from urllib.parse import quote_plus


def validate_date(value):
    date_formats = ['%d.%m.%Y', '%Y.%m.%d']
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass
    return False


def validate_phone(value):
    pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    phone_encoded = quote_plus(value)
    return re.match(pattern, phone_encoded) is not None


def validate_email(value):
    pattern = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w+$'
    return re.match(pattern, value) is not None
