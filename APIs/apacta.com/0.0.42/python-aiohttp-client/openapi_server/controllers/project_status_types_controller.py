from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_status_types_get200_response import ProjectStatusTypesGet200Response
from openapi_server import util


async def project_status_types_get(request: web.Request, ) -> web.Response:
    """Get a list of project status types

    


    """
    return web.Response(status=200)
