from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity_provider_mapper_representation import IdentityProviderMapperRepresentation
from openapi_server.models.identity_provider_representation import IdentityProviderRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server import util


async def realm_identity_provider_import_config_post(request: web.Request, realm) -> web.Response:
    """Import identity provider from uploaded JSON file

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_delete(request: web.Request, realm, alias) -> web.Response:
    """Delete the identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_export_get(request: web.Request, realm, alias, format=None) -> web.Response:
    """Export public broker configuration for identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param format: Format to use
    :type format: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_get(request: web.Request, realm, alias) -> web.Response:
    """Get the identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_management_permissions_get(request: web.Request, realm, alias) -> web.Response:
    """Return object stating whether client Authorization permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_management_permissions_put(request: web.Request, realm, alias, body) -> web.Response:
    """Return object stating whether client Authorization permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_mapper_types_get(request: web.Request, realm, alias) -> web.Response:
    """Get mapper types for identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_mappers_get(request: web.Request, realm, alias) -> web.Response:
    """Get mappers for identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_mappers_id_delete(request: web.Request, realm, alias, id) -> web.Response:
    """Delete a mapper for the identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param id: Mapper id
    :type id: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_mappers_id_get(request: web.Request, realm, alias, id) -> web.Response:
    """Get mapper by id for the identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param id: Mapper id
    :type id: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_mappers_id_put(request: web.Request, realm, alias, id, body) -> web.Response:
    """Update a mapper for the identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param id: Mapper id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentityProviderMapperRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_mappers_post(request: web.Request, realm, alias, body) -> web.Response:
    """Add a mapper to identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentityProviderMapperRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_identity_provider_instances_alias_put(request: web.Request, realm, alias, body) -> web.Response:
    """Update the identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: 
    :type alias: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentityProviderRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_identity_provider_instances_get(request: web.Request, realm) -> web.Response:
    """Get identity providers

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_identity_provider_instances_post(request: web.Request, realm, body) -> web.Response:
    """Create a new identity provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: JSON body
    :type body: dict | bytes

    """
    body = IdentityProviderRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_identity_provider_providers_provider_id_get(request: web.Request, realm, provider_id) -> web.Response:
    """Get identity providers

    

    :param realm: realm name (not id!)
    :type realm: str
    :param provider_id: Provider id
    :type provider_id: str

    """
    return web.Response(status=200)
