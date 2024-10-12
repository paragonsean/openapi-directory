from typing import List, Dict
from aiohttp import web

from openapi_server.models.remote_rendering_account_page import RemoteRenderingAccountPage
from openapi_server.models.remote_rendering_accounts_list_by_subscription_default_response import RemoteRenderingAccountsListBySubscriptionDefaultResponse
from openapi_server import util


async def remote_rendering_accounts_list_by_subscription_0(request: web.Request, subscription_id, api_version) -> web.Response:
    """remote_rendering_accounts_list_by_subscription_0

    List Remote Rendering Accounts by Subscription

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
