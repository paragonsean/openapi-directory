from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoices_list_result import InvoicesListResult
from openapi_server import util


async def invoices_get(request: web.Request, subscription_id, api_version, invoice_name) -> web.Response:
    """invoices_get

    Gets a named invoice resource. When getting a single invoice, the downloadUrl property is expanded automatically.  This is only supported for Azure Web-Direct subscriptions. Other subscription types which were not purchased directly through the Azure web portal are not supported through this preview API.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    :type api_version: str
    :param invoice_name: The name of an invoice resource.
    :type invoice_name: str

    """
    return web.Response(status=200)


async def invoices_get_latest(request: web.Request, subscription_id, api_version) -> web.Response:
    """invoices_get_latest

    Gets the most recent invoice. When getting a single invoice, the downloadUrl property is expanded automatically.  This is only supported for Azure Web-Direct subscriptions. Other subscription types which were not purchased directly through the Azure web portal are not supported through this preview API.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def invoices_list(request: web.Request, subscription_id, api_version, expand=None, filter=None, skiptoken=None, top=None) -> web.Response:
    """invoices_list

    Lists the available invoices for a subscription in reverse chronological order beginning with the most recent invoice. In preview, invoices are available via this API only for invoice periods which end December 1, 2016 or later.  This is only supported for Azure Web-Direct subscriptions. Other subscription types which were not purchased directly through the Azure web portal are not supported through this preview API.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    :type api_version: str
    :param expand: May be used to expand the downloadUrl property within a list of invoices. This enables download links to be generated for multiple invoices at once. By default, downloadURLs are not included when listing invoices.
    :type expand: str
    :param filter: May be used to filter invoices by invoicePeriodEndDate. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N invoices.
    :type top: int

    """
    return web.Response(status=200)
