from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.media_graph import MediaGraph
from openapi_server.models.media_graph_collection import MediaGraphCollection
from openapi_server.models.media_graph_operation_status import MediaGraphOperationStatus
from openapi_server import util


async def media_graphs_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, api_version, parameters) -> web.Response:
    """Create or update a Media Graph

    Create or update a Media Graph in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = MediaGraph.from_dict(parameters)
    return web.Response(status=200)


async def media_graphs_delete(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, api_version) -> web.Response:
    """Delete a Media Graph

    Deletes a Media Graph in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def media_graphs_get(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, api_version) -> web.Response:
    """Get a Media Graph

    Get the details of a Media Graph in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def media_graphs_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version, top=None) -> web.Response:
    """List Media Graphs

    Lists Media Graphs in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param top: Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    :type top: int

    """
    return web.Response(status=200)


async def media_graphs_start(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, api_version) -> web.Response:
    """Start a Media Graph

    Start a Media Graph in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def media_graphs_stop(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, api_version) -> web.Response:
    """Stop a Media Graph

    Stop a Media Graph in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def operation_results_get(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, operation_id, api_version) -> web.Response:
    """Get the operation result

    Get the operation result of a Media Graph in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param operation_id: The operation ID
    :type operation_id: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def operations_status_get(request: web.Request, subscription_id, resource_group_name, account_name, media_graph_name, operation_id, api_version) -> web.Response:
    """Get the operation status

    Get the operation status of a Media Graph in the media services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param media_graph_name: The Media Graph name.
    :type media_graph_name: str
    :param operation_id: The operation ID
    :type operation_id: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
