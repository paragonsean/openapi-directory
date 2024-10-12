from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def identity_company_address_get(request: web.Request, limit=None) -> web.Response:
    """identity_company_address_get

    Generate postal addresses

    :param limit: No of addresses to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_company_get(request: web.Request, ) -> web.Response:
    """identity_company_get

    Generate full company identity


    """
    return web.Response(status=200)


async def identity_company_name_get(request: web.Request, limit=None) -> web.Response:
    """identity_company_name_get

    Generate company name(s)

    :param limit: No of names to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_company_phonenumber_get(request: web.Request, limit=None) -> web.Response:
    """identity_company_phonenumber_get

    Generate random company phone number(s)

    :param limit: No of phone numbers to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_address_get(request: web.Request, limit=None) -> web.Response:
    """identity_person_address_get

    Generate postal addresses

    :param limit: No of addresses to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_creditcard_get(request: web.Request, limit=None) -> web.Response:
    """identity_person_creditcard_get

    Generate credit card details (number, type, expiration date, name on the card etc).

    :param limit: No of credit card details to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_email_get(request: web.Request, limit=None) -> web.Response:
    """identity_person_email_get

    Generate random email ids

    :param limit: No of email ids to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_get(request: web.Request, ) -> web.Response:
    """identity_person_get

    Generate full identity name, phone, email, address, credit card etc.


    """
    return web.Response(status=200)


async def identity_person_name_first_get(request: web.Request, gender=None, limit=None) -> web.Response:
    """identity_person_name_first_get

    Generate first name (in a given gender)

    :param gender: Gender of the names. If not specified both gender names will be returned.
    :type gender: str
    :param limit: No of names to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_name_get(request: web.Request, gender=None, limit=None) -> web.Response:
    """identity_person_name_get

    Generate full name(s)

    :param gender: Gender of the names. If not specified both gender names will be returned.
    :type gender: str
    :param limit: No of names to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_name_last_get(request: web.Request, limit=None) -> web.Response:
    """identity_person_name_last_get

    Generate last name(s)

    :param limit: No of names to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)


async def identity_person_phonenumber_get(request: web.Request, limit=None) -> web.Response:
    """identity_person_phonenumber_get

    Generate random phone number(s)

    :param limit: No of phone numbers to return. Defaults to 1.
    :type limit: int

    """
    return web.Response(status=200)
