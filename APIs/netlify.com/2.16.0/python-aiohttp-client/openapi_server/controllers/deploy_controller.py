from typing import List, Dict
from aiohttp import web

from openapi_server.models.deploy import Deploy
from openapi_server.models.deploy_files import DeployFiles
from openapi_server.models.error import Error
from openapi_server import util


async def cancel_site_deploy(request: web.Request, deploy_id) -> web.Response:
    """cancel_site_deploy

    

    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def create_site_deploy(request: web.Request, site_id, deploy, deploy_previews=None, production=None, state=None, branch=None, latest_published=None, title=None) -> web.Response:
    """create_site_deploy

    

    :param site_id: 
    :type site_id: str
    :param deploy: 
    :type deploy: dict | bytes
    :param deploy_previews: 
    :type deploy_previews: bool
    :param production: 
    :type production: bool
    :param state: 
    :type state: str
    :param branch: 
    :type branch: str
    :param latest_published: 
    :type latest_published: bool
    :param title: 
    :type title: str

    """
    deploy = DeployFiles.from_dict(deploy)
    return web.Response(status=200)


async def delete_deploy(request: web.Request, deploy_id) -> web.Response:
    """delete_deploy

    

    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def delete_site_deploy(request: web.Request, deploy_id, site_id) -> web.Response:
    """delete_site_deploy

    

    :param deploy_id: 
    :type deploy_id: str
    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def get_deploy(request: web.Request, deploy_id) -> web.Response:
    """get_deploy

    

    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def get_site_deploy(request: web.Request, site_id, deploy_id) -> web.Response:
    """get_site_deploy

    

    :param site_id: 
    :type site_id: str
    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def list_site_deploys(request: web.Request, site_id, deploy_previews=None, production=None, state=None, branch=None, latest_published=None, page=None, per_page=None) -> web.Response:
    """list_site_deploys

    

    :param site_id: 
    :type site_id: str
    :param deploy_previews: 
    :type deploy_previews: bool
    :param production: 
    :type production: bool
    :param state: 
    :type state: str
    :param branch: 
    :type branch: str
    :param latest_published: 
    :type latest_published: bool
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def lock_deploy(request: web.Request, deploy_id) -> web.Response:
    """lock_deploy

    

    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def restore_site_deploy(request: web.Request, site_id, deploy_id) -> web.Response:
    """restore_site_deploy

    

    :param site_id: 
    :type site_id: str
    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def rollback_site_deploy(request: web.Request, site_id) -> web.Response:
    """rollback_site_deploy

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def unlock_deploy(request: web.Request, deploy_id) -> web.Response:
    """unlock_deploy

    

    :param deploy_id: 
    :type deploy_id: str

    """
    return web.Response(status=200)


async def update_site_deploy(request: web.Request, site_id, deploy_id, deploy) -> web.Response:
    """update_site_deploy

    

    :param site_id: 
    :type site_id: str
    :param deploy_id: 
    :type deploy_id: str
    :param deploy: 
    :type deploy: dict | bytes

    """
    deploy = DeployFiles.from_dict(deploy)
    return web.Response(status=200)
