from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.invoice_section import InvoiceSection
from openapi_server.models.invoice_section_creation_request import InvoiceSectionCreationRequest
from openapi_server.models.invoice_section_list_result import InvoiceSectionListResult
from openapi_server import util


async def invoice_sections_create(request: web.Request, api_version, billing_account_name, parameters) -> web.Response:
    """invoice_sections_create

    The operation to create a InvoiceSection.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param parameters: Parameters supplied to the Create InvoiceSection operation.
    :type parameters: dict | bytes

    """
    parameters = InvoiceSectionCreationRequest.from_dict(parameters)
    return web.Response(status=200)


async def invoice_sections_elevate_to_billing_profile(request: web.Request, billing_account_name, invoice_section_name) -> web.Response:
    """invoice_sections_elevate_to_billing_profile

    Elevates the caller&#39;s access to match their billing profile access.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str

    """
    return web.Response(status=200)


async def invoice_sections_get(request: web.Request, api_version, billing_account_name, invoice_section_name, expand=None) -> web.Response:
    """invoice_sections_get

    Get the InvoiceSection by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param expand: May be used to expand the billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def invoice_sections_list_by_billing_account_name(request: web.Request, api_version, billing_account_name, expand=None) -> web.Response:
    """invoice_sections_list_by_billing_account_name

    Lists all invoice sections for which a user has access.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def invoice_sections_list_by_billing_profile_name(request: web.Request, api_version, billing_account_name, billing_profile_name) -> web.Response:
    """invoice_sections_list_by_billing_profile_name

    Lists all invoice sections under a billing profile for which a user has access.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str

    """
    return web.Response(status=200)


async def invoice_sections_list_by_create_subscription_permission(request: web.Request, api_version, billing_account_name, expand=None) -> web.Response:
    """invoice_sections_list_by_create_subscription_permission

    Lists all invoiceSections with create subscription permission for a user.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def invoice_sections_update(request: web.Request, api_version, billing_account_name, invoice_section_name, parameters) -> web.Response:
    """invoice_sections_update

    The operation to update a InvoiceSection.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param parameters: Parameters supplied to the Create InvoiceSection operation.
    :type parameters: dict | bytes

    """
    parameters = InvoiceSection.from_dict(parameters)
    return web.Response(status=200)
