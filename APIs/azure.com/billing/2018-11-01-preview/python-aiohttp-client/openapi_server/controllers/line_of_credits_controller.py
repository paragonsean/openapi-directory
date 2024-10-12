from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.line_of_credit import LineOfCredit
from openapi_server import util


async def line_of_credits_get(request: web.Request, api_version, subscription_id) -> web.Response:
    """line_of_credits_get

    Get the current line of credit.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def line_of_credits_update(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """line_of_credits_update

    Increase the current line of credit.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription Id.
    :type subscription_id: str
    :param parameters: Parameters supplied to the increase line of credit operation.
    :type parameters: dict | bytes

    """
    parameters = LineOfCredit.from_dict(parameters)
    return web.Response(status=200)
