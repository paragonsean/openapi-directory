from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_log_msg import BuildLogMsg
from openapi_server.models.error import Error
from openapi_server import util


async def update_site_build_log(request: web.Request, build_id, msg) -> web.Response:
    """update_site_build_log

    

    :param build_id: 
    :type build_id: str
    :param msg: 
    :type msg: dict | bytes

    """
    msg = BuildLogMsg.from_dict(msg)
    return web.Response(status=200)
