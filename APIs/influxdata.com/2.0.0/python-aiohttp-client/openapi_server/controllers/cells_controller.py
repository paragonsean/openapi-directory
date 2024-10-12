from typing import List, Dict
from aiohttp import web

from openapi_server.models.cell import Cell
from openapi_server.models.cell_update import CellUpdate
from openapi_server.models.create_cell import CreateCell
from openapi_server.models.dashboard import Dashboard
from openapi_server.models.error import Error
from openapi_server.models.view import View
from openapi_server import util


async def delete_dashboards_id_cells_id(request: web.Request, dashboard_id, cell_id, zap_trace_span=None) -> web.Response:
    """Delete a dashboard cell

    

    :param dashboard_id: The ID of the dashboard to delete.
    :type dashboard_id: str
    :param cell_id: The ID of the cell to delete.
    :type cell_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_dashboards_id_cells_id_view(request: web.Request, dashboard_id, cell_id, zap_trace_span=None) -> web.Response:
    """Retrieve the view for a cell

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param cell_id: The cell ID.
    :type cell_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_dashboards_id_cells_id(request: web.Request, dashboard_id, cell_id, body, zap_trace_span=None) -> web.Response:
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


async def patch_dashboards_id_cells_id_view(request: web.Request, dashboard_id, cell_id, body, zap_trace_span=None) -> web.Response:
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


async def post_dashboards_id_cells(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
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


async def put_dashboards_id_cells(request: web.Request, dashboard_id, body, zap_trace_span=None) -> web.Response:
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
