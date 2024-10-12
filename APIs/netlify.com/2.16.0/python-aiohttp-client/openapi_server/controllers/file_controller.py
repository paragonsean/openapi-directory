from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def get_site_file_by_path_name(request: web.Request, site_id, file_path) -> web.Response:
    """get_site_file_by_path_name

    

    :param site_id: 
    :type site_id: str
    :param file_path: 
    :type file_path: str

    """
    return web.Response(status=200)


async def list_site_files(request: web.Request, site_id) -> web.Response:
    """list_site_files

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def upload_deploy_file(request: web.Request, deploy_id, path, file_body, size=None) -> web.Response:
    """upload_deploy_file

    

    :param deploy_id: 
    :type deploy_id: str
    :param path: 
    :type path: str
    :param file_body: 
    :type file_body: str
    :param size: 
    :type size: int

    """
    return web.Response(status=200)
