from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_first_last_name_phone_coded_out import BatchFirstLastNamePhoneCodedOut
from openapi_server.models.batch_first_last_name_phone_number_geo_in import BatchFirstLastNamePhoneNumberGeoIn
from openapi_server.models.batch_first_last_name_phone_number_in import BatchFirstLastNamePhoneNumberIn
from openapi_server.models.first_last_name_phone_coded_out import FirstLastNamePhoneCodedOut
from openapi_server import util


async def phone_code(request: web.Request, first_name, last_name, phone_number) -> web.Response:
    """[USES 11 UNITS PER NAME] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param phone_number: 
    :type phone_number: str

    """
    return web.Response(status=200)


async def phone_code_batch(request: web.Request, body=None) -> web.Response:
    """[USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNamePhoneNumberIn.from_dict(body)
    return web.Response(status=200)


async def phone_code_geo(request: web.Request, first_name, last_name, phone_number, country_iso2) -> web.Response:
    """[USES 11 UNITS PER NAME] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param phone_number: 
    :type phone_number: str
    :param country_iso2: 
    :type country_iso2: str

    """
    return web.Response(status=200)


async def phone_code_geo_batch(request: web.Request, body=None) -> web.Response:
    """[USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchFirstLastNamePhoneNumberGeoIn.from_dict(body)
    return web.Response(status=200)


async def phone_code_geo_feedback_loop(request: web.Request, first_name, last_name, phone_number, phone_number_e164, country_iso2) -> web.Response:
    """[CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param phone_number: 
    :type phone_number: str
    :param phone_number_e164: 
    :type phone_number_e164: str
    :param country_iso2: 
    :type country_iso2: str

    """
    return web.Response(status=200)
