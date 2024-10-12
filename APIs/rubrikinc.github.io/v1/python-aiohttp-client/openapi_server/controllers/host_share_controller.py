from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_share_add_response import BulkShareAddResponse
from openapi_server.models.host_share_detail import HostShareDetail
from openapi_server.models.host_share_update import HostShareUpdate
from openapi_server.models.nas_shares_to_add import NasSharesToAdd
from openapi_server import util


async def bulk_add_host_shares(request: web.Request, body) -> web.Response:
    """Add NAS shares in bulk

    Add NAS shares for a NAS host to the Rubrik cluster in bulk. This operation does not validate share credentials. If the default share credentials are incorrect, the share status on shares UI displays as \&quot;Wrong credential\&quot;. Use the PATCH /v1/host/share/bulk endpoint to enter the correct credentials when this status displays.

    :param body: The properties used to add the NAS Shares to the Rubrik cluster.
    :type body: dict | bytes

    """
    body = NasSharesToAdd.from_dict(body)
    return web.Response(status=200)


async def bulk_update_host_share(request: web.Request, body) -> web.Response:
    """Update network shares

    Update the properties of the objects that represent the specified network share.

    :param body: Properties to use for the update of network share objects.
    :type body: list | bytes

    """
    body = [HostShareUpdate.from_dict(d) for d in body]
    return web.Response(status=200)
