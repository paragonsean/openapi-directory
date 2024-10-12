from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.bin_lookup_response import BINLookupResponse
from openapi_server.models.convert_response import ConvertResponse
from openapi_server import util


async def b_in_list_download(request: web.Request, include_iso3=None, include_8digit=None) -> web.Response:
    """BIN List Download

    Download our entire BIN database for direct use on your own systems

    :param include_iso3: Include ISO 3-letter country codes and ISO 3-letter currency codes in the data. These will be added to columns 10 and 11 respectively
    :type include_iso3: bool
    :param include_8digit: Include 8-digit and higher BIN codes. This option includes all 6-digit BINs and all 8-digit and higher BINs (including some 9, 10 and 11 digit BINs where available)
    :type include_8digit: bool

    """
    return web.Response(status=200)


async def b_in_lookup(request: web.Request, bin_number, customer_ip=None) -> web.Response:
    """BIN Lookup

    Perform a BIN (Bank Identification Number) or IIN (Issuer Identification Number) lookup

    :param bin_number: The BIN or IIN number. This is the first 6, 8 or 10 digits of a card number, use 8 (or more) digits for the highest level of accuracy
    :type bin_number: str
    :param customer_ip: Pass in the customers IP address and we will return some extra information about them
    :type customer_ip: str

    """
    return web.Response(status=200)


async def convert(request: web.Request, from_value, from_type, to_type) -> web.Response:
    """Convert

    A currency and unit conversion tool

    :param from_value: The value to convert from (e.g. 10.95)
    :type from_value: str
    :param from_type: The type of the value to convert from (e.g. USD)
    :type from_type: str
    :param to_type: The type to convert to (e.g. EUR)
    :type to_type: str

    """
    return web.Response(status=200)
