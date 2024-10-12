from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_default_project_statuses_error import AddDefaultProjectStatusesError
from openapi_server.models.add_default_project_statuses_success import AddDefaultProjectStatusesSuccess
from openapi_server import util


async def project_statuses_add_default_post(request: web.Request, ) -> web.Response:
    """Add default project statuses to company

    


    """
    return web.Response(status=200)
