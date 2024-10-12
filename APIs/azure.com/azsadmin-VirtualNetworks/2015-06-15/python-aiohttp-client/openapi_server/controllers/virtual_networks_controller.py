from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_networks_list import VirtualNetworksList
from openapi_server import util


async def virtual_networks_list(request: web.Request, subscription_id, api_version, filter=None, order_by=None, top=None, skip=None, inline_count=None) -> web.Response:
    """virtual_networks_list

    Get a list of all virtual networks.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str
    :param order_by: OData orderBy parameter.
    :type order_by: str
    :param top: OData top parameter.
    :type top: str
    :param skip: OData skip parameter.
    :type skip: str
    :param inline_count: OData inline count parameter.
    :type inline_count: str

    """
    return web.Response(status=200)
