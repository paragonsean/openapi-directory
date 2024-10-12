from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_role_definition import BillingRoleDefinition
from openapi_server.models.billing_role_definition_list_result import BillingRoleDefinitionListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_role_definitions_get_by_billing_account(request: web.Request, api_version, billing_account_name, billing_role_definition_name) -> web.Response:
    """billing_role_definitions_get_by_billing_account

    Gets the role definition for a role

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_role_definition_name: role definition id.
    :type billing_role_definition_name: str

    """
    return web.Response(status=200)


async def billing_role_definitions_get_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name, billing_role_definition_name) -> web.Response:
    """billing_role_definitions_get_by_billing_profile

    Gets the role definition for a role

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param billing_role_definition_name: role definition id.
    :type billing_role_definition_name: str

    """
    return web.Response(status=200)


async def billing_role_definitions_get_by_invoice_section(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name, billing_role_definition_name) -> web.Response:
    """billing_role_definitions_get_by_invoice_section

    Gets the role definition for a role

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param billing_role_definition_name: role definition id.
    :type billing_role_definition_name: str

    """
    return web.Response(status=200)


async def billing_role_definitions_list_by_billing_account(request: web.Request, api_version, billing_account_name) -> web.Response:
    """billing_role_definitions_list_by_billing_account

    Lists the role definition for a billing account

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str

    """
    return web.Response(status=200)


async def billing_role_definitions_list_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name) -> web.Response:
    """billing_role_definitions_list_by_billing_profile

    Lists the role definition for a Billing Profile

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str

    """
    return web.Response(status=200)


async def billing_role_definitions_list_by_invoice_section(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name) -> web.Response:
    """billing_role_definitions_list_by_invoice_section

    Lists the role definition for an invoice Section

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
