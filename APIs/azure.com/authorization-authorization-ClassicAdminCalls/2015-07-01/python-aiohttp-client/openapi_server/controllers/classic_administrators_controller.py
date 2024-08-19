from typing import List, Dict
from aiohttp import web

from openapi_server.models.classic_administrator_list_result import ClassicAdministratorListResult
from openapi_server import util


async def classic_administrators_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """classic_administrators_list

    Gets service administrator, account administrator, and co-administrators for the subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
