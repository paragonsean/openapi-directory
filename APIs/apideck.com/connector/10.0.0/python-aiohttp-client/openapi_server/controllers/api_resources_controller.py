from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_api_resource_coverage_response import GetApiResourceCoverageResponse
from openapi_server.models.get_api_resource_response import GetApiResourceResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server import util


async def api_resource_coverage_one(request: web.Request, x_apideck_app_id, id, resource_id) -> web.Response:
    """Get API Resource Coverage

    Get API Resource Coverage

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param id: ID of the record you are acting upon.
    :type id: str
    :param resource_id: ID of the resource you are acting upon.
    :type resource_id: str

    """
    return web.Response(status=200)


async def api_resources_one(request: web.Request, x_apideck_app_id, id, resource_id) -> web.Response:
    """Get API Resource

    Get API Resource

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param id: ID of the record you are acting upon.
    :type id: str
    :param resource_id: ID of the resource you are acting upon.
    :type resource_id: str

    """
    return web.Response(status=200)
