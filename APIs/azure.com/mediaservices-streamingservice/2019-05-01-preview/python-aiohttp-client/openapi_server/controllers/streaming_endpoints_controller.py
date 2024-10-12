from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.streaming_endpoint import StreamingEndpoint
from openapi_server.models.streaming_endpoint_list_result import StreamingEndpointListResult
from openapi_server.models.streaming_entity_scale_unit import StreamingEntityScaleUnit
from openapi_server import util


async def streaming_endpoints_create(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version, parameters, auto_start=None) -> web.Response:
    """Create StreamingEndpoint

    Creates a StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: StreamingEndpoint properties needed for creation.
    :type parameters: dict | bytes
    :param auto_start: The flag indicates if the resource should be automatically started on creation.
    :type auto_start: bool

    """
    parameters = StreamingEndpoint.from_dict(parameters)
    return web.Response(status=200)


async def streaming_endpoints_delete(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version) -> web.Response:
    """Delete StreamingEndpoint

    Deletes a StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_endpoints_get(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version) -> web.Response:
    """Get StreamingEndpoint

    Gets a StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_endpoints_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """List StreamingEndpoints

    Lists the StreamingEndpoints in the account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_endpoints_scale(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version, parameters) -> web.Response:
    """Scale StreamingEndpoint

    Scales an existing StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: StreamingEndpoint scale parameters
    :type parameters: dict | bytes

    """
    parameters = StreamingEntityScaleUnit.from_dict(parameters)
    return web.Response(status=200)


async def streaming_endpoints_start(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version) -> web.Response:
    """Start StreamingEndpoint

    Starts an existing StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_endpoints_stop(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version) -> web.Response:
    """Stop StreamingEndpoint

    Stops an existing StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
