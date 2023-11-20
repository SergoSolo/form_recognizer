import requests

from core import logger, logger_config  # isort: skip

URL = "http://localhost:5000/get_form"
FIRST_PARAMS = {
    "user_name": "serg",
    "email": "serg@mail.ru",
    "phone": "+79857758834"
}
SECOND_PARAMS = {
    "email": "serg@mail.ru",
    "password": "12345",
    "date": "20.11.2023"
}


def script_request(params):
    response = requests.post(URL, params=params)
    return response.text


if __name__ == "__main__":
    logger_config()
    logger.info("Производим первый запрос по которому форма не будет найдена.")
    logger.info(f"Результат: {script_request(FIRST_PARAMS)}")
    logger.info("Производим второй запрос по которому форма будет найдена.")
    logger.info(f"Результат: {script_request(SECOND_PARAMS)}")
