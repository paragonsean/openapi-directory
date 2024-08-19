from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.namespace_patch import NamespacePatch
from openapi_server.models.namespace_post import NamespacePost
from openapi_server.models.namespace_response import NamespaceResponse
from openapi_server import util


async def apps_app_id_namespaces_get(request: web.Request, app_id) -> web.Response:
    """Lists namespaces

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_app_id_namespaces_namespace_id_delete(request: web.Request, app_id, namespace_id) -> web.Response:
    """Deletes a namespace

    

    :param app_id: 
    :type app_id: str
    :param namespace_id: 
    :type namespace_id: str

    """
    return web.Response(status=200)


async def apps_app_id_namespaces_namespace_id_patch(request: web.Request, app_id, namespace_id, body=None) -> web.Response:
    """Updates a namespace

    

    :param app_id: 
    :type app_id: str
    :param namespace_id: 
    :type namespace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NamespacePatch.from_dict(body)
    return web.Response(status=200)


async def apps_app_id_namespaces_post(request: web.Request, app_id, body=None) -> web.Response:
    """Creates a namespace

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NamespacePost.from_dict(body)
    return web.Response(status=200)
