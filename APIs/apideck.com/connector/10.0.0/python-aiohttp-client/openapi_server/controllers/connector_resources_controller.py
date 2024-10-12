from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_connector_resource_response import GetConnectorResourceResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unified_api_id import UnifiedApiId
from openapi_server import util


async def connector_resources_one(request: web.Request, x_apideck_app_id, id, resource_id, unified_api=None) -> web.Response:
    """Get Connector Resource

    Get Connector Resource

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param id: ID of the record you are acting upon.
    :type id: str
    :param resource_id: ID of the resource you are acting upon.
    :type resource_id: str
    :param unified_api: Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs
    :type unified_api: dict | bytes

    """
    unified_api = .from_dict(unified_api)
    return web.Response(status=200)
