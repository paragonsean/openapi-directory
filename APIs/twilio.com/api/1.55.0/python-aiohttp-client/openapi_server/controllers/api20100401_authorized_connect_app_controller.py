from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_authorized_connect_app import ApiV2010AccountAuthorizedConnectApp
from openapi_server.models.list_authorized_connect_app_response import ListAuthorizedConnectAppResponse
from openapi_server import util


async def fetch_authorized_connect_app(request: web.Request, account_sid, connect_app_sid) -> web.Response:
    """fetch_authorized_connect_app

    Fetch an instance of an authorized-connect-app

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resource to fetch.
    :type account_sid: str
    :param connect_app_sid: The SID of the Connect App to fetch.
    :type connect_app_sid: str

    """
    return web.Response(status=200)


async def list_authorized_connect_app(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_authorized_connect_app

    Retrieve a list of authorized-connect-apps belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resources to read.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
