from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_url import DownloadUrl
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def price_sheet_download(request: web.Request, api_version, billing_account_name, invoice_name) -> web.Response:
    """price_sheet_download

    Download price sheet for an invoice.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Azure Billing Account ID.
    :type billing_account_name: str
    :param invoice_name: The name of an invoice resource.
    :type invoice_name: str

    """
    return web.Response(status=200)
