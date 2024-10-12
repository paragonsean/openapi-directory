from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_template200_response import DeleteTemplate200Response
from openapi_server.models.get_templates401_response import GetTemplates401Response
from openapi_server.models.get_templates403_response import GetTemplates403Response
from openapi_server.models.get_templates404_response import GetTemplates404Response
from openapi_server.models.get_templates422_response import GetTemplates422Response
from openapi_server.models.get_templates500_response import GetTemplates500Response
from openapi_server.models.get_workspace200_response import GetWorkspace200Response
from openapi_server import util


async def delete_workspace(request: web.Request, workspace_id) -> web.Response:
    """Delete workspace

    Deletes the workspace

    :param workspace_id: Workspace identifier
    :type workspace_id: str

    """
    return web.Response(status=200)


async def get_workspace(request: web.Request, workspace_id) -> web.Response:
    """Get workspace

    Returns workspace information

    :param workspace_id: Workspace identifier
    :type workspace_id: str

    """
    return web.Response(status=200)
