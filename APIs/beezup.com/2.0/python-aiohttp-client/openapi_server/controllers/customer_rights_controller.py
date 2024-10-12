from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.functionality_right_info import FunctionalityRightInfo
from openapi_server import util


async def get_rights(request: web.Request, store_id) -> web.Response:
    """Get store&#39;s rights

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)
