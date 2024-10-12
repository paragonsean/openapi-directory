from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_v1_safelist import AccountsV1Safelist
from openapi_server import util


async def create_safelist(request: web.Request, phone_number) -> web.Response:
    """create_safelist

    Add a new phone number to SafeList.

    :param phone_number: The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :type phone_number: str

    """
    return web.Response(status=200)


async def delete_safelist(request: web.Request, phone_number=None) -> web.Response:
    """delete_safelist

    Remove a phone number from SafeList.

    :param phone_number: The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :type phone_number: str

    """
    return web.Response(status=200)


async def fetch_safelist(request: web.Request, phone_number=None) -> web.Response:
    """fetch_safelist

    Check if a phone number exists in SafeList.

    :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :type phone_number: str

    """
    return web.Response(status=200)
