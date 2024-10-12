from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.view import View
from openapi_server import util


async def get_dashboards_id_cells_id_view_1(request: web.Request, dashboard_id, cell_id, zap_trace_span=None) -> web.Response:
    """Retrieve the view for a cell

    

    :param dashboard_id: The dashboard ID.
    :type dashboard_id: str
    :param cell_id: The cell ID.
    :type cell_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_dashboards_id_cells_id_view_1(request: web.Request, dashboard_id, cell_id, body, zap_trace_span=None) -> web.Response:
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
