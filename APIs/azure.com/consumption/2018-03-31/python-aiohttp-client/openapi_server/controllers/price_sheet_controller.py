from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.price_sheet_result import PriceSheetResult
from openapi_server import util


async def price_sheet_get(request: web.Request, subscription_id, api_version, expand=None, skiptoken=None, top=None) -> web.Response:
    """price_sheet_get

    Gets the price sheet for a scope by subscriptionId. Price sheet is available via this API only for May 1, 2014 or later.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param expand: May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the top N results.
    :type top: int

    """
    return web.Response(status=200)


async def price_sheet_get_by_billing_period(request: web.Request, subscription_id, api_version, billing_period_name, expand=None, skiptoken=None, top=None) -> web.Response:
    """price_sheet_get_by_billing_period

    Get the price sheet for a scope by subscriptionId and billing period. Price sheet is available via this API only for May 1, 2014 or later.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param expand: May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the top N results.
    :type top: int

    """
    return web.Response(status=200)
