from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_property import BillingProperty
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_property_get(request: web.Request, subscription_id, api_version) -> web.Response:
    """billing_property_get

    Get billing property by subscription Id.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
