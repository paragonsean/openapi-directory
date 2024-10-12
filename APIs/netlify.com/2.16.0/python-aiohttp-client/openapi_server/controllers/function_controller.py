from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.function import Function
from openapi_server import util


async def upload_deploy_function(request: web.Request, deploy_id, name, file_body, runtime=None, size=None, x_nf_retry_count=None) -> web.Response:
    """upload_deploy_function

    

    :param deploy_id: 
    :type deploy_id: str
    :param name: 
    :type name: str
    :param file_body: 
    :type file_body: str
    :param runtime: 
    :type runtime: str
    :param size: 
    :type size: int
    :param x_nf_retry_count: 
    :type x_nf_retry_count: int

    """
    return web.Response(status=200)
