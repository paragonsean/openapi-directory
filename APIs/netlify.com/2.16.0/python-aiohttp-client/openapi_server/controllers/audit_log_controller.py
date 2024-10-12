from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit_log import AuditLog
from openapi_server.models.error import Error
from openapi_server import util


async def list_account_audit_events(request: web.Request, account_id, query=None, log_type=None, page=None, per_page=None) -> web.Response:
    """list_account_audit_events

    

    :param account_id: 
    :type account_id: str
    :param query: 
    :type query: str
    :param log_type: 
    :type log_type: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)
