from typing import List, Dict
from aiohttp import web

from openapi_server.models.agreement import Agreement
from openapi_server.models.agreement_list_result import AgreementListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def agreements_get(request: web.Request, api_version, billing_account_name, agreement_name, expand=None) -> web.Response:
    """agreements_get

    Get the agreement by name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param agreement_name: Agreement Id.
    :type agreement_name: str
    :param expand: May be used to expand the participants.
    :type expand: str

    """
    return web.Response(status=200)


async def agreements_list_by_billing_account_name(request: web.Request, api_version, billing_account_name, expand=None) -> web.Response:
    """agreements_list_by_billing_account_name

    Lists all agreements for a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the participants.
    :type expand: str

    """
    return web.Response(status=200)
