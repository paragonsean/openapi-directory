from typing import List, Dict
from aiohttp import web

from openapi_server.models.deploy_key import DeployKey
from openapi_server.models.error import Error
from openapi_server import util


async def create_deploy_key(request: web.Request, ) -> web.Response:
    """create_deploy_key

    


    """
    return web.Response(status=200)


async def delete_deploy_key(request: web.Request, key_id) -> web.Response:
    """delete_deploy_key

    

    :param key_id: 
    :type key_id: str

    """
    return web.Response(status=200)


async def get_deploy_key(request: web.Request, key_id) -> web.Response:
    """get_deploy_key

    

    :param key_id: 
    :type key_id: str

    """
    return web.Response(status=200)


async def list_deploy_keys(request: web.Request, ) -> web.Response:
    """list_deploy_keys

    


    """
    return web.Response(status=200)
