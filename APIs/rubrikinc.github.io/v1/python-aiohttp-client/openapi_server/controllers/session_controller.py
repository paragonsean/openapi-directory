from typing import List, Dict
from aiohttp import web

from openapi_server.models.session_summary import SessionSummary
from openapi_server import util


async def create_session(request: web.Request, organization_id=None, realm=None) -> web.Response:
    """Create user session

    Open a user session.

    :param organization_id: Bind the new session to the specified organization. When this parameter is not specified, the session will be bound to an organization chosen according to the user&#39;s preferences and authorizations.
    :type organization_id: str
    :param realm: Bind the new session to the specified directory. When this parameter is unspecified, the session will be bound to local domain.
    :type realm: str

    """
    return web.Response(status=200)


async def delete_session(request: web.Request, id) -> web.Response:
    """Delete user session

    Close a user session and invalidate the session token.

    :param id: Session ID or  *me* for session of bearer token.
    :type id: str

    """
    return web.Response(status=200)
