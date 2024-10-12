from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_logs_response import GetLogsResponse
from openapi_server.models.logs_filter import LogsFilter
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server import util


async def logs_all(request: web.Request, x_apideck_app_id, x_apideck_consumer_id, filter=None, cursor=None, limit=None) -> web.Response:
    """Get all consumer request logs

    This endpoint includes all consumer request logs. 

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param filter: Filter results
    :type filter: dict | bytes
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int

    """
    filter = .from_dict(filter)
    return web.Response(status=200)
