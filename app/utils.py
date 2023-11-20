from core.db import collection

from validators import (validate_date, validate_email,  # isort: skip
                        validate_phone)


def type_recognizer(string):
    field_types = {}
    for key, value in string.items():
        if validate_date(value):
            field_types[key] = "DATE"
        elif validate_phone(value):
            field_types[key] = "PHONE"
        elif validate_email(value):
            field_types[key] = "EMAIL"
        else:
            field_types[key] = "TEXT"
    return field_types


def find_matching_template(query_params):
    data = type_recognizer(query_params)
    for form in collection.find():
        if all([field in form for field in data]):
            return {"form_name": form.get("form_name")}
    return data
