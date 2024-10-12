from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.modern_csp_subscription_creation_parameters import ModernCspSubscriptionCreationParameters
from openapi_server.models.modern_subscription_creation_parameters import ModernSubscriptionCreationParameters
from openapi_server.models.subscription_creation_result import SubscriptionCreationResult
from openapi_server import util


async def subscription_factory_create_csp_subscription(request: web.Request, billing_account_name, customer_name, api_version, body) -> web.Response:
    """subscription_factory_create_csp_subscription

    The operation to create a new CSP subscription.

    :param billing_account_name: The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
    :type billing_account_name: str
    :param customer_name: The name of the customer.
    :type customer_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2018-11-01-preview
    :type api_version: str
    :param body: The subscription creation parameters.
    :type body: dict | bytes

    """
    body = ModernCspSubscriptionCreationParameters.from_dict(body)
    return web.Response(status=200)


async def subscription_factory_create_subscription(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, api_version, body) -> web.Response:
    """subscription_factory_create_subscription

    The operation to create a new WebDirect or EA Azure subscription.

    :param billing_account_name: The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
    :type billing_account_name: str
    :param billing_profile_name: The name of the billing profile in the billing account for which you want to create the subscription.
    :type billing_profile_name: str
    :param invoice_section_name: The name of the invoice section in the billing account for which you want to create the subscription.
    :type invoice_section_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2018-11-01-preview
    :type api_version: str
    :param body: The subscription creation parameters.
    :type body: dict | bytes

    """
    body = ModernSubscriptionCreationParameters.from_dict(body)
    return web.Response(status=200)


async def subscription_operation_get(request: web.Request, operation_id, api_version) -> web.Response:
    """subscription_operation_get

    Get the status of the pending Microsoft.Subscription API operations.

    :param operation_id: The operation ID, which can be found from the Location field in the generate recommendation response header.
    :type operation_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2018-11-01-preview
    :type api_version: str

    """
    return web.Response(status=200)
