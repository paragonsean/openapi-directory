from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.transfer_billing_subscription_request_properties import TransferBillingSubscriptionRequestProperties
from openapi_server.models.transfer_billing_subscription_result import TransferBillingSubscriptionResult
from openapi_server.models.transfer_product_request_properties import TransferProductRequestProperties
from openapi_server.models.validate_product_transfer_eligibility_result import ValidateProductTransferEligibilityResult
from openapi_server.models.validate_subscription_transfer_eligibility_result import ValidateSubscriptionTransferEligibilityResult
from openapi_server import util


async def billing_subscriptions_transfer(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, billing_subscription_name, parameters) -> web.Response:
    """billing_subscriptions_transfer

    Transfers the subscription from one invoice section to another within a billing account.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param billing_subscription_name: Billing Subscription Id.
    :type billing_subscription_name: str
    :param parameters: Request parameters supplied to the Transfer Billing Subscription operation.
    :type parameters: dict | bytes

    """
    parameters = TransferBillingSubscriptionRequestProperties.from_dict(parameters)
    return web.Response(status=200)


async def billing_subscriptions_validate_transfer(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, billing_subscription_name, parameters) -> web.Response:
    """billing_subscriptions_validate_transfer

    Validates the transfer of billing subscriptions across invoice sections.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param billing_subscription_name: Billing Subscription Id.
    :type billing_subscription_name: str
    :param parameters: Parameters supplied to the Transfer Billing Subscription operation.
    :type parameters: dict | bytes

    """
    parameters = TransferBillingSubscriptionRequestProperties.from_dict(parameters)
    return web.Response(status=200)


async def products_validate_transfer(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, product_name, parameters) -> web.Response:
    """products_validate_transfer

    Validates the transfer of products across invoice sections.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param product_name: Invoice Id.
    :type product_name: str
    :param parameters: Parameters supplied to the Transfer Products operation.
    :type parameters: dict | bytes

    """
    parameters = TransferProductRequestProperties.from_dict(parameters)
    return web.Response(status=200)
