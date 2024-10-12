from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_connect_app import ApiV2010AccountConnectApp
from openapi_server.models.connect_app_enum_permission import ConnectAppEnumPermission
from openapi_server.models.list_connect_app_response import ListConnectAppResponse
from openapi_server import util


async def delete_connect_app(request: web.Request, account_sid, sid) -> web.Response:
    """delete_connect_app

    Delete an instance of a connect-app

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_connect_app(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_connect_app

    Fetch an instance of a connect-app

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_connect_app(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_connect_app

    Retrieve a list of connect-apps belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_connect_app(request: web.Request, account_sid, sid, authorize_redirect_url=None, company_name=None, deauthorize_callback_method=None, deauthorize_callback_url=None, description=None, friendly_name=None, homepage_url=None, permissions=None) -> web.Response:
    """update_connect_app

    Update a connect-app with the specified parameters

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
    :type sid: str
    :param authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App.
    :type authorize_redirect_url: str
    :param company_name: The company name to set for the Connect App.
    :type company_name: str
    :param deauthorize_callback_method: The HTTP method to use when calling &#x60;deauthorize_callback_url&#x60;.
    :type deauthorize_callback_method: str
    :param deauthorize_callback_url: The URL to call using the &#x60;deauthorize_callback_method&#x60; to de-authorize the Connect App.
    :type deauthorize_callback_url: str
    :param description: A description of the Connect App.
    :type description: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param homepage_url: A public URL where users can obtain more information about this Connect App.
    :type homepage_url: str
    :param permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: &#x60;get-all&#x60; and &#x60;post-all&#x60;.
    :type permissions: list | bytes

    """
    permissions = [ConnectAppEnumPermission.from_dict(d) for d in permissions]
    return web.Response(status=200)
