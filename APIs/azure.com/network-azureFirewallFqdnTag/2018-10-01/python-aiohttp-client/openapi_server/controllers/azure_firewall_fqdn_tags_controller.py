from typing import List, Dict
from aiohttp import web

from openapi_server.models.azure_firewall_fqdn_tag_list_result import AzureFirewallFqdnTagListResult
from openapi_server import util


async def azure_firewall_fqdn_tags_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """azure_firewall_fqdn_tags_list_all

    Gets all the Azure Firewall FQDN Tags in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
