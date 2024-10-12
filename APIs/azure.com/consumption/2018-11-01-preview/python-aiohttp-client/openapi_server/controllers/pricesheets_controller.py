from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.pricesheet_download_response import PricesheetDownloadResponse
from openapi_server import util


async def billing_profile_pricesheet_download(request: web.Request, api_version, billing_account_id, billing_profile_id) -> web.Response:
    """billing_profile_pricesheet_download

    Get pricesheet data for invoice id (invoiceName).

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_id: Azure Billing Account Id.
    :type billing_account_id: str
    :param billing_profile_id: Azure Billing Profile Id.
    :type billing_profile_id: str

    """
    return web.Response(status=200)


async def invoice_pricesheet_download(request: web.Request, api_version, billing_account_id, invoice_name) -> web.Response:
    """invoice_pricesheet_download

    Get pricesheet data for invoice id (invoiceName).

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_id: Azure Billing Account Id.
    :type billing_account_id: str
    :param invoice_name: The name of an invoice resource.
    :type invoice_name: str

    """
    return web.Response(status=200)
