from typing import List, Dict
from aiohttp import web

from openapi_server.models.numbers_v1_porting_portability import NumbersV1PortingPortability
from openapi_server import util


async def fetch_porting_portability(request: web.Request, phone_number, target_account_sid=None) -> web.Response:
    """fetch_porting_portability

    Allows to check if a single phone number can be ported to Twilio or not.

    :param phone_number: The phone number which portability is to be checked. Phone numbers are in E.164 format (e.g. +16175551212).
    :type phone_number: str
    :param target_account_sid: The SID of the account where the phone number(s) will be ported.
    :type target_account_sid: str

    """
    return web.Response(status=200)
