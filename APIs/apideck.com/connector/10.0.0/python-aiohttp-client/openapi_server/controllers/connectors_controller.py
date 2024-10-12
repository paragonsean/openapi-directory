from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.connectors_filter import ConnectorsFilter
from openapi_server.models.get_connector_response import GetConnectorResponse
from openapi_server.models.get_connectors_response import GetConnectorsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server import util


async def connectors_all(request: web.Request, x_apideck_app_id, cursor=None, limit=None, filter=None) -> web.Response:
    """List Connectors

    List Connectors

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int
    :param filter: Apply filters
    :type filter: dict | bytes

    """
    filter = .from_dict(filter)
    return web.Response(status=200)


async def connectors_one(request: web.Request, x_apideck_app_id, id) -> web.Response:
    """Get Connector

    Get Connector

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param id: ID of the record you are acting upon.
    :type id: str

    """
    return web.Response(status=200)
