from typing import List, Dict
from aiohttp import web

from openapi_server.models.numbers_v1_porting_bulk_portability import NumbersV1PortingBulkPortability
from openapi_server import util


async def create_porting_bulk_portability(request: web.Request, phone_numbers) -> web.Response:
    """create_porting_bulk_portability

    Allows to check if a list of phone numbers can be ported to Twilio or not. This is done asynchronous for each phone number.

    :param phone_numbers: The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). .
    :type phone_numbers: List[str]

    """
    return web.Response(status=200)


async def fetch_porting_bulk_portability(request: web.Request, sid) -> web.Response:
    """fetch_porting_bulk_portability

    Fetch a previous portability check. This should return the current status of the validation and the result for all the numbers provided, given that they have been validated (as this process is performed asynchronously).

    :param sid: A 34 character string that uniquely identifies the Portability check.
    :type sid: str

    """
    return web.Response(status=200)
