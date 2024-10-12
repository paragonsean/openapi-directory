from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.file_needs_vendor import FileNeedsVendor
from openapi_server.models.vendor_invitation_list import VendorInvitationList
from openapi_server import util


async def get_invitation_vendors(request: web.Request, body=None) -> web.Response:
    """Get vendor list for compiled invitation needs

    Get vendor list for compiled invitation needs

    :param body: 
    :type body: list | bytes

    """
    body = [FileNeedsVendor.from_dict(d) for d in body]
    return web.Response(status=200)
