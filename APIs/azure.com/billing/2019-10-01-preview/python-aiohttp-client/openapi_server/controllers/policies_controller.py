from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_policy import CustomerPolicy
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.policy import Policy
from openapi_server import util


async def policies_get_by_billing_profile(request: web.Request, billing_account_name, billing_profile_name, api_version) -> web.Response:
    """policies_get_by_billing_profile

    The policy for a given billing account name and billing profile name.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def policies_get_by_customer(request: web.Request, billing_account_name, customer_name, api_version) -> web.Response:
    """policies_get_by_customer

    The policy for a given billing account name and customer name.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer name.
    :type customer_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def policies_update(request: web.Request, api_version, billing_account_name, billing_profile_name, parameters) -> web.Response:
    """policies_update

    The operation to update a policy.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param parameters: Parameters supplied to the update policy operation.
    :type parameters: dict | bytes

    """
    parameters = Policy.from_dict(parameters)
    return web.Response(status=200)


async def policies_update_customer(request: web.Request, api_version, billing_account_name, customer_name, parameters) -> web.Response:
    """policies_update_customer

    The operation to update a Customer policy.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer name.
    :type customer_name: str
    :param parameters: Parameters supplied to the update customer policy operation.
    :type parameters: dict | bytes

    """
    parameters = CustomerPolicy.from_dict(parameters)
    return web.Response(status=200)
