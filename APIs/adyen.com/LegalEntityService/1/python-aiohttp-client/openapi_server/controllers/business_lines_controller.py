from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_line import BusinessLine
from openapi_server.models.business_line_info import BusinessLineInfo
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def delete_business_lines_id(request: web.Request, id) -> web.Response:
    """Delete a business line

    Deletes a business line.   &gt;If you delete a business line linked to a [payment method](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api), it can affect your merchant account&#39;s ability to use the [payment method](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings). The business line is removed from all linked merchant accounts.

    :param id: The unique identifier of the business line to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def get_business_lines_id(request: web.Request, id) -> web.Response:
    """Get a business line

    Returns the detail of a business line.

    :param id: The unique identifier of the business line.
    :type id: str

    """
    return web.Response(status=200)


async def post_business_lines(request: web.Request, body=None) -> web.Response:
    """Create a business line

    Creates a business line.   This resource contains information about your user&#39;s line of business, including their industry and their source of funds. Adyen uses this information to verify your users as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

    :param body: 
    :type body: dict | bytes

    """
    body = BusinessLineInfo.from_dict(body)
    return web.Response(status=200)
