from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_text import QueryText
from openapi_server.models.query_texts_result_list import QueryTextsResultList
from openapi_server import util


async def query_texts_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, query_id) -> web.Response:
    """query_texts_get

    Retrieve the Query-Store query texts for the queryId.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param query_id: The Query-Store query identifier.
    :type query_id: str

    """
    return web.Response(status=200)


async def query_texts_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name, query_ids) -> web.Response:
    """query_texts_list_by_server

    Retrieve the Query-Store query texts for specified queryIds.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param query_ids: The query identifiers
    :type query_ids: List[str]

    """
    return web.Response(status=200)
