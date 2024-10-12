from typing import List, Dict
from aiohttp import web

from openapi_server.models.caller_id import CallerId
from openapi_server import util


async def v2_phone_numbers_caller_ids_json_get(request: web.Request, phone_number) -> web.Response:
    """List caller ids

    Each entry is a possible caller ID match for the number. Multiple entries may be returned if the phone number is present on more than one person in the system.  Phone number should be in E.164 format. 

    :param phone_number: E.164 Phone Number
    :type phone_number: str

    """
    return web.Response(status=200)
