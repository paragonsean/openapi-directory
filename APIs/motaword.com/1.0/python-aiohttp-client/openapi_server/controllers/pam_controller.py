from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_profile import ClientProfile
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.pam_message import PamMessage
from openapi_server.models.project_completion_report import ProjectCompletionReport
from openapi_server import util


async def get_client_profile_for_pam(request: web.Request, client_id) -> web.Response:
    """Get the Pam profile of a client for this client ID

    Get the Pam  profile of a client for this client ID

    :param client_id: Client ID
    :type client_id: int

    """
    return web.Response(status=200)


async def get_project_completion_report_for_pam(request: web.Request, project_id) -> web.Response:
    """Get completion report data of a project

    Get completion report data of a project

    :param project_id: Quote ID
    :type project_id: int

    """
    return web.Response(status=200)


async def post_message(request: web.Request, body=None) -> web.Response:
    """Sends a message to chat

    Sends a message to the channel.

    :param body: 
    :type body: dict | bytes

    """
    body = PamMessage.from_dict(body)
    return web.Response(status=200)
