from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_subscription_summary import BillingSubscriptionSummary
from openapi_server.models.billing_subscriptions_list_result import BillingSubscriptionsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_subscriptions_get(request: web.Request, billing_account_name, invoice_section_name, billing_subscription_name, api_version) -> web.Response:
    """billing_subscriptions_get

    Get a single billing subscription by name.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param billing_subscription_name: Billing Subscription Id.
    :type billing_subscription_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def billing_subscriptions_get_by_customer_name(request: web.Request, billing_account_name, customer_name, billing_subscription_name, api_version) -> web.Response:
    """billing_subscriptions_get_by_customer_name

    Get a single billing subscription by name.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer Id.
    :type customer_name: str
    :param billing_subscription_name: Billing Subscription Id.
    :type billing_subscription_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def billing_subscriptions_list_by_billing_account_name(request: web.Request, billing_account_name, api_version) -> web.Response:
    """billing_subscriptions_list_by_billing_account_name

    Lists billing subscriptions by billing account name.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def billing_subscriptions_list_by_billing_profile_name(request: web.Request, billing_account_name, billing_profile_name, api_version) -> web.Response:
    """billing_subscriptions_list_by_billing_profile_name

    Lists billing subscriptions by billing profile name.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def billing_subscriptions_list_by_customer_name(request: web.Request, billing_account_name, customer_name, api_version) -> web.Response:
    """billing_subscriptions_list_by_customer_name

    Lists billing subscription by customer name.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer Id.
    :type customer_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def billing_subscriptions_list_by_invoice_section_name(request: web.Request, billing_account_name, invoice_section_name, api_version) -> web.Response:
    """billing_subscriptions_list_by_invoice_section_name

    Lists billing subscription by invoice section name.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
