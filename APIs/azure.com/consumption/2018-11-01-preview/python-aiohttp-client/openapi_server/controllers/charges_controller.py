from typing import List, Dict
from aiohttp import web

from openapi_server.models.charges_list_by_billing_account import ChargesListByBillingAccount
from openapi_server.models.charges_list_by_billing_profile import ChargesListByBillingProfile
from openapi_server.models.charges_list_by_invoice_section import ChargesListByInvoiceSection
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def charges_by_billing_account_list(request: web.Request, billing_account_id, api_version, start_date, end_date, apply=None) -> web.Response:
    """charges_by_billing_account_list

    Lists the charges by billingAccountId for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param start_date: Start date
    :type start_date: str
    :param end_date: End date
    :type end_date: str
    :param apply: May be used to group charges by properties/billingProfileId, or properties/invoiceSectionId.
    :type apply: str

    """
    return web.Response(status=200)


async def charges_by_billing_profile_list(request: web.Request, billing_account_id, billing_profile_id, api_version, start_date, end_date) -> web.Response:
    """charges_by_billing_profile_list

    Lists the charges by billing profile id for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_profile_id: Billing Profile Id.
    :type billing_profile_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param start_date: Start date
    :type start_date: str
    :param end_date: End date
    :type end_date: str

    """
    return web.Response(status=200)


async def charges_by_invoice_section_list(request: web.Request, billing_account_id, invoice_section_id, api_version, start_date, end_date, apply=None) -> web.Response:
    """charges_by_invoice_section_list

    Lists the charges by invoice section id for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param invoice_section_id: Invoice Section Id.
    :type invoice_section_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param start_date: Start date
    :type start_date: str
    :param end_date: End date
    :type end_date: str
    :param apply: May be used to group charges by properties/productName.
    :type apply: str

    """
    return web.Response(status=200)
