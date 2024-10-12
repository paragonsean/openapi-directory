from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_patch import AppPatch
from openapi_server.models.app_post import AppPost
from openapi_server.models.app_response import AppResponse
from openapi_server.models.error import Error
from openapi_server import util


async def accounts_account_id_apps_get(request: web.Request, account_id) -> web.Response:
    """Lists account apps

    

    :param account_id: 
    :type account_id: str

    """
    return web.Response(status=200)


async def accounts_account_id_apps_post(request: web.Request, account_id, body=None) -> web.Response:
    """Creates an app

    

    :param account_id: 
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppPost.from_dict(body)
    return web.Response(status=200)


async def apps_id_delete(request: web.Request, id) -> web.Response:
    """Deletes an app

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def apps_id_patch(request: web.Request, id, body=None) -> web.Response:
    """Updates an app

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppPatch.from_dict(body)
    return web.Response(status=200)


async def apps_id_pkcs12_post(request: web.Request, id, p12_file, p12_pass) -> web.Response:
    """Updates app&#39;s APNS info from a .p12 file

    

    :param id: 
    :type id: str
    :param p12_file: 
    :type p12_file: str
    :param p12_pass: 
    :type p12_pass: str

    """
    return web.Response(status=200)
