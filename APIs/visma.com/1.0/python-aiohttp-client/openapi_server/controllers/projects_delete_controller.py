from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.phase_member_model import PhaseMemberModel
from openapi_server.models.resource_allocation_action import ResourceAllocationAction
from openapi_server import util


async def keywords_delete_project_keyword(request: web.Request, project_guid, guid) -> web.Response:
    """Delete a keyword from the project

    Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

    :param project_guid: 
    :type project_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def phase_members_delete_phase_member(request: web.Request, user_guid, resource_allocation_action=None, transfer_to_user_guid=None, body=None) -> web.Response:
    """Deletes a phase member

    Returns: No Content (204) if succeeded. Only one of transferToRoleGuid and transferToUserGuid can be provided. Use root phase to delete a project member.

    :param user_guid: GUID of the phase member to remove
    :type user_guid: str
    :param resource_allocation_action: Optional: The action to be applied to the user&#39;s resource allocations
    :type resource_allocation_action: dict | bytes
    :param transfer_to_user_guid: Optional: GUID of the user to whom the resource allocations are transferred.
    :type transfer_to_user_guid: str
    :param body: 
    :type body: dict | bytes

    """
    resource_allocation_action = .from_dict(resource_allocation_action)
    body = PhaseMemberModel.from_dict(body)
    return web.Response(status=200)


async def phases_delete_phase(request: web.Request, guid) -> web.Response:
    """Deletes a phase

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the phase.
    :type guid: str

    """
    return web.Response(status=200)


async def project_custom_values_delete_project_custom_value(request: web.Request, guid) -> web.Response:
    """Deletes a project custom value.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project custom value.
    :type guid: str

    """
    return web.Response(status=200)


async def project_forecasts_delete_forecast(request: web.Request, guid) -> web.Response:
    """Delete a project forecast

    Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

    :param guid: ID for the project forecast to delete
    :type guid: str

    """
    return web.Response(status=200)


async def project_forecasts_delete_forecasts(request: web.Request, project_guid, year=None, month=None) -> web.Response:
    """Delete the project forecasts from a month onward, including the given month.

    

    :param project_guid: Project for the forecasts to delete
    :type project_guid: str
    :param year: Year where to start deleting the forecasts
    :type year: int
    :param month: Month where to start deleting the forecasts
    :type month: int

    """
    return web.Response(status=200)


async def project_invoice_settings_delete_project_invoice_settings_0(request: web.Request, guid) -> web.Response:
    """Delete an project invoice settings.

    Returns: No Content (204) if succeeded. Not found (404) if project invoice settings can&#39;t be found.

    :param guid: ID for the project invoice settings to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def project_products_delete_all_project_products(request: web.Request, project_guid) -> web.Response:
    """Deletes all project products of a project.

    Returns: No Content (204) if succeeded.

    :param project_guid: GUID of the project from where project products to remove.
    :type project_guid: str

    """
    return web.Response(status=200)


async def project_products_delete_project_product(request: web.Request, guid) -> web.Response:
    """Deletes a project product.

    Returns: No Content (204) if succeeded.

    :param guid: GUID of the project product to remove.
    :type guid: str

    """
    return web.Response(status=200)


async def project_work_hour_prices_delete_project_work_hour_price(request: web.Request, guid) -> web.Response:
    """Deletes a work hour price

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the work hour price.
    :type guid: str

    """
    return web.Response(status=200)


async def project_work_types_delete_project_worktype(request: web.Request, guid) -> web.Response:
    """Deletes a project work type.

    Returns: No Content (204) if succeeded. The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

    :param guid: GUID of the project work type to remove.
    :type guid: str

    """
    return web.Response(status=200)


async def projects_delete_project(request: web.Request, guid) -> web.Response:
    """Delete a project

    Returns: No Content (204) if succeeded. Not found (404) if project can&#39;t be found.

    :param guid: ID for the project to delete
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_fees_delete_proposal_fee(request: web.Request, guid) -> web.Response:
    """Delete a proposal fee row

    Returns: No Content (204) if succeeded. Not found (404) if proposal fee row can&#39;t be found.

    :param guid: ID for the proposal fee row to delete
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_subtotals_delete_proposal_subtotal(request: web.Request, guid) -> web.Response:
    """Delete a proposal subtotal

    Returns: No Content (204) if succeeded. Not found (404) if proposal subtotal can&#39;t be found.

    :param guid: ID for the proposal subtotal to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def proposal_workhours_delete_proposal_workhour(request: web.Request, guid) -> web.Response:
    """Delete a proposal work row.

    Returns: No Content (204) if succeeded. Not found (404) if proposal work row can&#39;t be found.

    :param guid: ID for the proposal work row to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def proposals_delete_proposal(request: web.Request, guid) -> web.Response:
    """Delete a proposal

    Returns: No Content (204) if succeeded. Not found (404) if proposal can&#39;t be found.

    :param guid: Guid for the proposal to delete
    :type guid: str

    """
    return web.Response(status=200)


async def sales_notes_delete_project_sales_note(request: web.Request, guid) -> web.Response:
    """Deletes a project sales note.

    Returns: No Content (204) if succeeded. OK (200) if note has child notes and can&#39;t be deleted. It is marked as IsDeleted &#x3D; true. Not found (404) if note can&#39;t be found.

    :param guid: GUID used to delete the project sales note.
    :type guid: str

    """
    return web.Response(status=200)
