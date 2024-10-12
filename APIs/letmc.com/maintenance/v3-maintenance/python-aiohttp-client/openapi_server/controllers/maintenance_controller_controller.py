from typing import List, Dict
from aiohttp import web

from openapi_server.models.maintenance_issue_model import MaintenanceIssueModel
from openapi_server import util


async def maintenance_controller_create_maintenance_job(request: web.Request, short_name, branch_id, body) -> web.Response:
    """Create a maintenance job for a specific branch

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param body: A JSON object containing details of the maintenance job
    :type body: dict | bytes

    """
    body = MaintenanceIssueModel.from_dict(body)
    return web.Response(status=200)
