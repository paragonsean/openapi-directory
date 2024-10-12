from typing import List, Dict
from aiohttp import web

from openapi_server.models.codat_error_message import CodatErrorMessage
from openapi_server.models.post_sync import PostSync
from openapi_server.models.sync_initiated import SyncInitiated
from openapi_server import util


async def intiate_sync(request: web.Request, company_id, company_id2, body=None) -> web.Response:
    """Initiate sync

    Initiate sync of pending transactions.

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param company_id2: 
    :type company_id2: str
    :type company_id2: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostSync.from_dict(body)
    return web.Response(status=200)
