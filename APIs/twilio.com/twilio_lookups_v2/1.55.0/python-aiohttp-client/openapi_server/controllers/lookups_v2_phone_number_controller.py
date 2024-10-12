from typing import List, Dict
from aiohttp import web

from openapi_server.models.lookups_v2_phone_number import LookupsV2PhoneNumber
from openapi_server import util


async def fetch_phone_number(request: web.Request, phone_number, fields=None, country_code=None, first_name=None, last_name=None, address_line1=None, address_line2=None, city=None, state=None, postal_code=None, address_country_code=None, national_id=None, date_of_birth=None, last_verified_date=None) -> web.Response:
    """fetch_phone_number

    

    :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
    :type phone_number: str
    :param fields: A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap, call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number, sms_pumping_risk, phone_number_quality_score.
    :type fields: str
    :param country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
    :type country_code: str
    :param first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
    :type first_name: str
    :param last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
    :type last_name: str
    :param address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
    :type address_line1: str
    :param address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
    :type address_line2: str
    :param city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
    :type city: str
    :param state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
    :type state: str
    :param postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
    :type postal_code: str
    :param address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
    :type address_country_code: str
    :param national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
    :type national_id: str
    :param date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.
    :type date_of_birth: str
    :param last_verified_date: The date you obtained consent to call or text the end-user of the phone number or a date on which you are reasonably certain that the end-user could still be reached at that number. This query parameter is only used (optionally) for reassigned_number package requests.
    :type last_verified_date: str

    """
    return web.Response(status=200)
