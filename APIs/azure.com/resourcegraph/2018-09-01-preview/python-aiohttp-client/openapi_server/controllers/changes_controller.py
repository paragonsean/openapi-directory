from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.resource_change_data import ResourceChangeData
from openapi_server.models.resource_change_details_request_parameters import ResourceChangeDetailsRequestParameters
from openapi_server.models.resource_change_list import ResourceChangeList
from openapi_server.models.resource_changes_request_parameters import ResourceChangesRequestParameters
from openapi_server import util


async def resource_change_details(request: web.Request, api_version, parameters) -> web.Response:
    """resource_change_details

    Get resource change details.

    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters for this request for resource change details.
    :type parameters: dict | bytes

    """
    parameters = ResourceChangeDetailsRequestParameters.from_dict(parameters)
    return web.Response(status=200)


async def resource_changes(request: web.Request, api_version, parameters) -> web.Response:
    """resource_changes

    List changes to a resource for a given time interval.

    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: the parameters for this request for changes.
    :type parameters: dict | bytes

    """
    parameters = ResourceChangesRequestParameters.from_dict(parameters)
    return web.Response(status=200)
