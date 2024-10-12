from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_provisioning_status import FlexV1ProvisioningStatus
from openapi_server import util


async def fetch_provisioning_status(request: web.Request, ) -> web.Response:
    """fetch_provisioning_status

    


    """
    return web.Response(status=200)
