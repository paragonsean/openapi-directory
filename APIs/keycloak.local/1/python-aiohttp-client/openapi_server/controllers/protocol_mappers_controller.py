from typing import List, Dict
from aiohttp import web

from openapi_server.models.protocol_mapper_representation import ProtocolMapperRepresentation
from openapi_server import util


async def realm_client_scopes_id1_protocol_mappers_models_id2_delete(request: web.Request, realm, id1, id2) -> web.Response:
    """Delete the mapper

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id1: 
    :type id1: str
    :param id2: 
    :type id2: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id1_protocol_mappers_models_id2_get(request: web.Request, realm, id1, id2) -> web.Response:
    """Get mapper by id

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id1: 
    :type id1: str
    :param id2: 
    :type id2: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id1_protocol_mappers_models_id2_put(request: web.Request, realm, id1, id2, body) -> web.Response:
    """Update the mapper

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id1: 
    :type id1: str
    :param id2: 
    :type id2: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProtocolMapperRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_client_scopes_id_protocol_mappers_add_models_post(request: web.Request, realm, id, body) -> web.Response:
    """Create multiple mappers

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [ProtocolMapperRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_client_scopes_id_protocol_mappers_models_get(request: web.Request, realm, id) -> web.Response:
    """Get mappers

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str

    """
    return web.Response(status=200)


async def realm_client_scopes_id_protocol_mappers_models_post(request: web.Request, realm, id, body) -> web.Response:
    """Create a mapper

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProtocolMapperRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_client_scopes_id_protocol_mappers_protocol_protocol_get(request: web.Request, realm, id, protocol) -> web.Response:
    """Get mappers by name for a specific protocol

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client scope (not name)
    :type id: str
    :param protocol: 
    :type protocol: str

    """
    return web.Response(status=200)


async def realm_clients_id1_protocol_mappers_models_id2_delete(request: web.Request, realm, id1, id2) -> web.Response:
    """Delete the mapper

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id1: 
    :type id1: str
    :param id2: 
    :type id2: str

    """
    return web.Response(status=200)


async def realm_clients_id1_protocol_mappers_models_id2_get(request: web.Request, realm, id1, id2) -> web.Response:
    """Get mapper by id

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id1: 
    :type id1: str
    :param id2: 
    :type id2: str

    """
    return web.Response(status=200)


async def realm_clients_id1_protocol_mappers_models_id2_put(request: web.Request, realm, id1, id2, body) -> web.Response:
    """Update the mapper

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id1: 
    :type id1: str
    :param id2: 
    :type id2: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProtocolMapperRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_protocol_mappers_add_models_post(request: web.Request, realm, id, body) -> web.Response:
    """Create multiple mappers

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [ProtocolMapperRepresentation.from_dict(d) for d in body]
    return web.Response(status=200)


async def realm_clients_id_protocol_mappers_models_get(request: web.Request, realm, id) -> web.Response:
    """Get mappers

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_protocol_mappers_models_post(request: web.Request, realm, id, body) -> web.Response:
    """Create a mapper

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProtocolMapperRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_protocol_mappers_protocol_protocol_get(request: web.Request, realm, id, protocol) -> web.Response:
    """Get mappers by name for a specific protocol

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param protocol: 
    :type protocol: str

    """
    return web.Response(status=200)
