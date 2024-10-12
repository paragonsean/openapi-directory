from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_new_key import ApiV2010AccountNewKey
from openapi_server import util


async def create_new_key(request: web.Request, account_sid, friendly_name=None) -> web.Response:
    """create_new_key

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource.
    :type account_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
