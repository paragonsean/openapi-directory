from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.invoice_section import InvoiceSection
from openapi_server.models.invoice_section_creation_request import InvoiceSectionCreationRequest
from openapi_server.models.invoice_section_list_result import InvoiceSectionListResult
from openapi_server import util


async def invoice_sections_create(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name, parameters) -> web.Response:
    """invoice_sections_create

    The operation to create an invoice section.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param parameters: Request parameters supplied to the Create InvoiceSection operation.
    :type parameters: dict | bytes

    """
    parameters = InvoiceSectionCreationRequest.from_dict(parameters)
    return web.Response(status=200)


async def invoice_sections_elevate_to_billing_profile(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name) -> web.Response:
    """invoice_sections_elevate_to_billing_profile

    Elevates the caller&#39;s access to match their billing profile access.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str

    """
    return web.Response(status=200)


async def invoice_sections_get(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name) -> web.Response:
    """invoice_sections_get

    Get the InvoiceSection by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str

    """
    return web.Response(status=200)


async def invoice_sections_list_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name) -> web.Response:
    """invoice_sections_list_by_billing_profile

    Lists all invoice sections for a user which he has access to.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str

    """
    return web.Response(status=200)


async def invoice_sections_update(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name, parameters) -> web.Response:
    """invoice_sections_update

    The operation to update a InvoiceSection.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param parameters: Request parameters supplied to the Create InvoiceSection operation.
    :type parameters: dict | bytes

    """
    parameters = InvoiceSection.from_dict(parameters)
    return web.Response(status=200)
