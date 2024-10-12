from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.subscription_definition import SubscriptionDefinition
from openapi_server.models.subscription_definition_list import SubscriptionDefinitionList
from openapi_server import util


async def subscription_definitions_create(request: web.Request, subscription_definition_name, api_version, body) -> web.Response:
    """subscription_definitions_create

    Create an Azure subscription definition.

    :param subscription_definition_name: The name of the Azure subscription definition.
    :type subscription_definition_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str
    :param body: The subscription definition creation.
    :type body: dict | bytes

    """
    body = SubscriptionDefinition.from_dict(body)
    return web.Response(status=200)


async def subscription_definitions_get(request: web.Request, subscription_definition_name, api_version) -> web.Response:
    """subscription_definitions_get

    Get an Azure subscription definition.

    :param subscription_definition_name: The name of the Azure subscription definition.
    :type subscription_definition_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_definitions_get_operation_status(request: web.Request, api_version, operation_id) -> web.Response:
    """subscription_definitions_get_operation_status

    Retrieves the status of the subscription definition PUT operation. The URI of this API is returned in the Location field of the response header.

    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str
    :param operation_id: The operation ID, which can be found from the Location field in the generate recommendation response header.
    :type operation_id: str
    :type operation_id: str

    """
    return web.Response(status=200)


async def subscription_definitions_list(request: web.Request, api_version) -> web.Response:
    """subscription_definitions_list

    List an Azure subscription definition by subscriptionId.

    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_definitions_operation_metadata_list(request: web.Request, api_version) -> web.Response:
    """subscription_definitions_operation_metadata_list

    Lists all of the available Microsoft.Subscription API operations.

    :param api_version: Version of the API to be used with the client request. Current version is 2015-06-01
    :type api_version: str

    """
    return web.Response(status=200)
