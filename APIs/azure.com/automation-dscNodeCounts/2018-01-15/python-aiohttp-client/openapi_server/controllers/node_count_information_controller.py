from typing import List, Dict
from aiohttp import web

from openapi_server.models.node_count_information_get_default_response import NodeCountInformationGetDefaultResponse
from openapi_server.models.node_counts import NodeCounts
from openapi_server import util


async def node_count_information_get(request: web.Request, resource_group_name, automation_account_name, count_type, subscription_id, api_version) -> web.Response:
    """node_count_information_get

    Retrieve counts for Dsc Nodes.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param count_type: The type of counts to retrieve
    :type count_type: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
