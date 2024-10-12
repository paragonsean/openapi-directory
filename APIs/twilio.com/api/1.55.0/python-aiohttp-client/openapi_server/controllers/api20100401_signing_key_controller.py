from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_signing_key import ApiV2010AccountSigningKey
from openapi_server.models.list_signing_key_response import ListSigningKeyResponse
from openapi_server import util


async def delete_signing_key(request: web.Request, account_sid, sid) -> web.Response:
    """delete_signing_key

    

    :param account_sid: 
    :type account_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_signing_key(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_signing_key

    

    :param account_sid: 
    :type account_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_signing_key(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_signing_key

    

    :param account_sid: 
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_signing_key(request: web.Request, account_sid, sid, friendly_name=None) -> web.Response:
    """update_signing_key

    

    :param account_sid: 
    :type account_sid: str
    :param sid: 
    :type sid: str
    :param friendly_name: 
    :type friendly_name: str

    """
    return web.Response(status=200)
