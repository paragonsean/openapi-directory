from typing import List, Dict
from aiohttp import web

from openapi_server.models.routes_v2_phone_number import RoutesV2PhoneNumber
from openapi_server import util


async def fetch_phone_number(request: web.Request, phone_number) -> web.Response:
    """fetch_phone_number

    Fetch the Inbound Processing Region assigned to a phone number.

    :param phone_number: The phone number in E.164 format
    :type phone_number: str

    """
    return web.Response(status=200)


async def update_phone_number(request: web.Request, phone_number, friendly_name=None, voice_region=None) -> web.Response:
    """update_phone_number

    Assign an Inbound Processing Region to a phone number.

    :param phone_number: The phone number in E.164 format
    :type phone_number: str
    :param friendly_name: A human readable description of this resource, up to 64 characters.
    :type friendly_name: str
    :param voice_region: The Inbound Processing Region used for this phone number for voice
    :type voice_region: str

    """
    return web.Response(status=200)
