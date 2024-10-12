from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_key import ApiV2010AccountKey
from openapi_server.models.list_key_response import ListKeyResponse
from openapi_server import util


async def delete_key(request: web.Request, account_sid, sid) -> web.Response:
    """delete_key

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Key resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_key(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_key

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Key resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_key(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_key

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to read.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_key(request: web.Request, account_sid, sid, friendly_name=None) -> web.Response:
    """update_key

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Key resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
