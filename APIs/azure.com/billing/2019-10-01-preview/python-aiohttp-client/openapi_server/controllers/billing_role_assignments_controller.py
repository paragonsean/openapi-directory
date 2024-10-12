from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_role_assignment import BillingRoleAssignment
from openapi_server.models.billing_role_assignment_list_result import BillingRoleAssignmentListResult
from openapi_server.models.billing_role_assignment_payload import BillingRoleAssignmentPayload
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_role_assignments_add_by_billing_account(request: web.Request, api_version, billing_account_name, parameters) -> web.Response:
    """billing_role_assignments_add_by_billing_account

    The operation to add a role assignment to a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param parameters: Parameters supplied to add a role assignment.
    :type parameters: dict | bytes

    """
    parameters = BillingRoleAssignmentPayload.from_dict(parameters)
    return web.Response(status=200)


async def billing_role_assignments_add_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name, parameters) -> web.Response:
    """billing_role_assignments_add_by_billing_profile

    The operation to add a role assignment to a billing profile.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param parameters: Parameters supplied to add a role assignment.
    :type parameters: dict | bytes

    """
    parameters = BillingRoleAssignmentPayload.from_dict(parameters)
    return web.Response(status=200)


async def billing_role_assignments_add_by_invoice_section(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name, parameters) -> web.Response:
    """billing_role_assignments_add_by_invoice_section

    The operation to add a role assignment to a invoice Section.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param parameters: Parameters supplied to add a role assignment.
    :type parameters: dict | bytes

    """
    parameters = BillingRoleAssignmentPayload.from_dict(parameters)
    return web.Response(status=200)


async def billing_role_assignments_delete_by_billing_account(request: web.Request, api_version, billing_account_name, billing_role_assignment_name) -> web.Response:
    """billing_role_assignments_delete_by_billing_account

    Delete the role assignment on this billing account

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_role_assignment_name: role assignment id.
    :type billing_role_assignment_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_delete_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name, billing_role_assignment_name) -> web.Response:
    """billing_role_assignments_delete_by_billing_profile

    Delete the role assignment on this Billing Profile

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param billing_role_assignment_name: role assignment id.
    :type billing_role_assignment_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_delete_by_invoice_section(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name, billing_role_assignment_name) -> web.Response:
    """billing_role_assignments_delete_by_invoice_section

    Delete the role assignment on the invoice Section

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param billing_role_assignment_name: role assignment id.
    :type billing_role_assignment_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_get_by_billing_account(request: web.Request, api_version, billing_account_name, billing_role_assignment_name) -> web.Response:
    """billing_role_assignments_get_by_billing_account

    Get the role assignment for the caller

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_role_assignment_name: role assignment id.
    :type billing_role_assignment_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_get_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name, billing_role_assignment_name) -> web.Response:
    """billing_role_assignments_get_by_billing_profile

    Get the role assignment for the caller on the Billing Profile

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param billing_role_assignment_name: role assignment id.
    :type billing_role_assignment_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_get_by_invoice_section(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name, billing_role_assignment_name) -> web.Response:
    """billing_role_assignments_get_by_invoice_section

    Get the role assignment for the caller on the invoice Section

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param billing_role_assignment_name: role assignment id.
    :type billing_role_assignment_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_list_by_billing_account(request: web.Request, api_version, billing_account_name) -> web.Response:
    """billing_role_assignments_list_by_billing_account

    Get the role assignments on the Billing Account

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_list_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name) -> web.Response:
    """billing_role_assignments_list_by_billing_profile

    Get the role assignments on the Billing Profile

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str

    """
    return web.Response(status=200)


async def billing_role_assignments_list_by_invoice_section(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_section_name) -> web.Response:
    """billing_role_assignments_list_by_invoice_section

    Get the role assignments on the invoice Section

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
