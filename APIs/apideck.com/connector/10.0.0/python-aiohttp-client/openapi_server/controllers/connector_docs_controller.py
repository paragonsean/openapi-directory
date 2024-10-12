from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server import util


async def connector_docs_one(request: web.Request, x_apideck_app_id, id, doc_id) -> web.Response:
    """Get Connector Doc content

    Get Connector Doc content

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param id: ID of the record you are acting upon.
    :type id: str
    :param doc_id: ID of the Doc
    :type doc_id: str

    """
    return web.Response(status=200)
