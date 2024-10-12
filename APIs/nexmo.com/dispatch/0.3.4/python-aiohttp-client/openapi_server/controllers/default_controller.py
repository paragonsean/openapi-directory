from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_workflow import CreateWorkflow
from openapi_server.models.error import Error
from openapi_server.models.response import Response
from openapi_server import util


async def create_workflow(request: web.Request, body) -> web.Response:
    """Create a workflow

    

    :param body: Please note that last message does not have failover attribute inside it. All other messages must contain a failover attribute.
    :type body: dict | bytes

    """
    body = CreateWorkflow.from_dict(body)
    return web.Response(status=200)
