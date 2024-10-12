from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.cell import Cell
from openapi_server.models.cell_update import CellUpdate
from openapi_server.models.create_cell import CreateCell
from openapi_server.models.create_dashboard_request import CreateDashboardRequest
from openapi_server.models.dashboard import Dashboard
from openapi_server.models.dashboards import Dashboards
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.patch_dashboard_request import PatchDashboardRequest
from openapi_server.models.post_dashboards201_response import PostDashboards201Response
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.view import View
from openapi_server import util


async def delete_dashboards_id(request: web.Request, dashboard_id, zap_trace_span=None) -> web.Response:
    """Delete a dashboard

    

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_dashboards_id_cells_id_0(request: web.Request, dashboard_id, cell_id, zap_trace_span=None) -> web.Response:
    """Delete a dashboard cell

    

    :param dashboard_id: The ID of the dashboard to delete.
    :type dashboard_id: str
    :param cell_id: The ID of the cell to delete.
    :type cell_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_dashboards_id_labels_id(request: web.Request, dashboard_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a dashboard

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param label_id: The ID of the label to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_dashboards_id_members_id(request: web.Request, user_id, dashboard_id, zap_trace_span=None) -> web.Response:
    """Remove a member from a dashboard

    

    :param user_id: The ID of the member to remove.
    :type user_id: str
    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_dashboards_id_owners_id(request: web.Request, user_id, dashboard_id, zap_trace_span=None) -> web.Response:
    """Remove an owner from a dashboard

    

    :param user_id: The ID of the owner to remove.
    :type user_id: str
    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_dashboards(request: web.Request, zap_trace_span=None, offset=None, limit=None, descending=None, owner=None, sort_by=None, id=None, org_id=None, org=None) -> web.Response:
    """List all dashboards

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param descending: 
    :type descending: bool
    :param owner: A user identifier. Returns only dashboards where this user has the &#x60;owner&#x60; role.
    :type owner: str
    :param sort_by: The column to sort by.
    :type sort_by: str
    :param id: A list of dashboard identifiers. Returns only the listed dashboards. If both &#x60;id&#x60; and &#x60;owner&#x60; are specified, only &#x60;id&#x60; is used.
    :type id: List[str]
    :param org_id: The identifier of the organization.
    :type org_id: str
    :param org: The name of the organization.
    :type org: str

    """
    return web.Response(status=200)


async def get_dashboards_id(request: web.Request, dashboard_id, zap_trace_span=None, include=None) -> web.Response:
    """Retrieve a Dashboard

    

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param include: Includes the cell view properties in the response if set to &#x60;properties&#x60;
    :type include: str

    """
    return web.Response(status=200)


async def get_dashboards_id_cells_id_view_0(request: web.Request, dashboard_id, cell_id, zap_trace_span=None) -> web.Response:
    """Retrieve the view for a cell

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param cell_id: The cell ID.
    :type cell_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_dashboards_id_labels(request: web.Request, dashboard_id, zap_trace_span=None) -> web.Response:
    """List all labels for a dashboard

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_dashboards_id_members(request: web.Request, dashboard_id, zap_trace_span=None) -> web.Response:
    """List all dashboard members

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_dashboards_id_owners(request: web.Request, dashboard_id, zap_trace_span=None) -> web.Response:
    """List all dashboard owners

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_dashboards_id(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
    """Update a dashboard

    

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param body: Patching of a dashboard
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PatchDashboardRequest.from_dict(body)
    return web.Response(status=200)


async def patch_dashboards_id_cells_id_0(request: web.Request, dashboard_id, cell_id, body, zap_trace_span=None) -> web.Response:
    """Update the non-positional information related to a cell

    Updates the non positional information related to a cell. Updates to a single cell&#39;s positional data could cause grid conflicts.

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param cell_id: The ID of the cell to update.
    :type cell_id: str
    :param body: 
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = CellUpdate.from_dict(body)
    return web.Response(status=200)


async def patch_dashboards_id_cells_id_view_0(request: web.Request, dashboard_id, cell_id, body, zap_trace_span=None) -> web.Response:
    """Update the view for a cell

    

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param cell_id: The ID of the cell to update.
    :type cell_id: str
    :param body: 
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = View.from_dict(body)
    return web.Response(status=200)


async def post_dashboards(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a dashboard

    

    :param body: Dashboard to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = CreateDashboardRequest.from_dict(body)
    return web.Response(status=200)


async def post_dashboards_id_cells_0(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
    """Create a dashboard cell

    

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param body: Cell that will be added
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = CreateCell.from_dict(body)
    return web.Response(status=200)


async def post_dashboards_id_labels(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a dashboard

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def post_dashboards_id_members(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
    """Add a member to a dashboard

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param body: User to add as member
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_dashboards_id_owners(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
    """Add an owner to a dashboard

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param body: User to add as owner
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def put_dashboards_id_cells_0(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
    """Replace cells in a dashboard

    Replaces all cells in a dashboard. This is used primarily to update the positional information of all cells.

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param body: 
    :type body: list | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = [Cell.from_dict(d) for d in body]
    return web.Response(status=200)
