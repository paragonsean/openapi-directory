from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_list_result import CustomerListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customers_get(request: web.Request, api_version, billing_account_name, customer_name, expand=None) -> web.Response:
    """customers_get

    Gets a customer by its id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer name.
    :type customer_name: str
    :param expand: May be used to expand enabledAzurePlans, resellers.
    :type expand: str

    """
    return web.Response(status=200)


async def customers_list_by_billing_account(request: web.Request, api_version, billing_account_name, filter=None, skiptoken=None) -> web.Response:
    """customers_list_by_billing_account

    Lists customers which the current user can work with on-behalf of a partner.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param filter: May be used to filter the list of customers.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def customers_list_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name, filter=None, skiptoken=None) -> web.Response:
    """customers_list_by_billing_profile

    Lists customers by billing profile which the current user can work with on-behalf of a partner.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param filter: May be used to filter the list of customers.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)
