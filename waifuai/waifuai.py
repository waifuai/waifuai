import urllib
import requests
import string
import random


def get_response(X_RAPIDAPI_KEY: str, user_id: str = "", message: str = "", from_name="", to_name="", situation="", translate_to='auto',
                 preset_mode='waifu'):
    """
    Gets the response using the Requests method
    All inputs are optional.
    """
    parsed_message = urllib.parse.quote(message)
    parsed_user_id = urllib.parse.quote(user_id)
    parsed_from_name = urllib.parse.quote(from_name)
    parsed_to_name = urllib.parse.quote(to_name)
    parsed_situation = urllib.parse.quote(situation)
    parsed_translate_to = urllib.parse.quote(translate_to)
    parsed_preset_mode = urllib.parse.quote(preset_mode)
    THE_PAYLOAD = f"message={parsed_message}&user_id={parsed_user_id}&from_name={parsed_from_name}&to_name={parsed_to_name}&situation={parsed_situation}&translate_to={parsed_translate_to}&preset_mode={parsed_preset_mode}"

    url = "https://waifu.p.rapidapi.com/path"

    payload = THE_PAYLOAD
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': X_RAPIDAPI_KEY,
        'x-rapidapi-host': "waifu.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


def generate_user_id() -> str:
    alnum = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(alnum) for i in range(64))
    return user_id
