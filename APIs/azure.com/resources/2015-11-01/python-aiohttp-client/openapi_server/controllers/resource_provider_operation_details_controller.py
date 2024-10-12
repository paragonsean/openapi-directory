from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_provider_operation_detail_list_result import ResourceProviderOperationDetailListResult
from openapi_server import util


async def resource_provider_operation_details_list(request: web.Request, resource_provider_namespace, api_version) -> web.Response:
    """resource_provider_operation_details_list

    Gets a list of resource providers.

    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)
