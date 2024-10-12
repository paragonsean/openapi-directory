from typing import List, Dict
from aiohttp import web

from openapi_server.models.component_representation import ComponentRepresentation
from openapi_server.models.component_type_representation import ComponentTypeRepresentation
from openapi_server import util


async def realm_components_get(request: web.Request, realm, name=None, parent=None, type=None) -> web.Response:
    """realm_components_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param name: 
    :type name: str
    :param parent: 
    :type parent: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def realm_components_id_delete(request: web.Request, realm, id) -> web.Response:
    """realm_components_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_components_id_get(request: web.Request, realm, id) -> web.Response:
    """realm_components_id_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_components_id_put(request: web.Request, realm, id, body) -> web.Response:
    """realm_components_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ComponentRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_components_id_sub_component_types_get(request: web.Request, realm, id, type=None) -> web.Response:
    """List of subcomponent types that are available to configure for a particular parent component.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def realm_components_post(request: web.Request, realm, body) -> web.Response:
    """realm_components_post

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = ComponentRepresentation.from_dict(body)
    return web.Response(status=200)
