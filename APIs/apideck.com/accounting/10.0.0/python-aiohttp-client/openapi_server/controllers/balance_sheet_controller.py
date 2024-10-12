from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.balance_sheet_filter import BalanceSheetFilter
from openapi_server.models.get_balance_sheet_response import GetBalanceSheetResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server import util


async def balance_sheet_one(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, pass_through=None, filter=None, raw=None) -> web.Response:
    """Get BalanceSheet

    Get BalanceSheet

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param pass_through: Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads
    :type pass_through: Dict[str, ]
    :param filter: Apply filters
    :type filter: dict | bytes
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool

    """
    filter = .from_dict(filter)
    return web.Response(status=200)
