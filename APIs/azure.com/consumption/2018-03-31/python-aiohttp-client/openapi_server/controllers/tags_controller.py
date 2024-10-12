from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tags import Tags
from openapi_server import util


async def tags_get(request: web.Request, api_version, billing_account_id) -> web.Response:
    """tags_get

    Get all available tag keys for a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str

    """
    return web.Response(status=200)
