from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_url import DownloadUrl
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def price_sheet_download(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_name) -> web.Response:
    """price_sheet_download

    Download price sheet for an invoice.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_name: Invoice Id.
    :type invoice_name: str

    """
    return web.Response(status=200)


async def price_sheet_download_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name) -> web.Response:
    """price_sheet_download_by_billing_profile

    Download price sheet for a billing profile.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str

    """
    return web.Response(status=200)
