from typing import List, Dict
from aiohttp import web

from openapi_server.models.cost_tags import CostTags
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def cost_tags_create_or_update(request: web.Request, api_version, billing_account_id, parameters) -> web.Response:
    """cost_tags_create_or_update

    The operation to create or update cost tags associated with a billing account. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param parameters: Parameters supplied to the Create cost tags operation.
    :type parameters: dict | bytes

    """
    parameters = CostTags.from_dict(parameters)
    return web.Response(status=200)


async def cost_tags_get(request: web.Request, api_version, billing_account_id) -> web.Response:
    """cost_tags_get

    Get cost tags for a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str

    """
    return web.Response(status=200)
