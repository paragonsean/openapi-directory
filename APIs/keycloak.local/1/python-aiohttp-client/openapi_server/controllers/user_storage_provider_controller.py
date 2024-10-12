from typing import List, Dict
from aiohttp import web

from openapi_server.models.synchronization_result import SynchronizationResult
from openapi_server import util


async def id_name_get(request: web.Request, id) -> web.Response:
    """Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_user_storage_id_name_get(request: web.Request, realm, id) -> web.Response:
    """Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_user_storage_id_remove_imported_users_post(request: web.Request, realm, id) -> web.Response:
    """Remove imported users

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_user_storage_id_sync_post(request: web.Request, realm, id, action=None) -> web.Response:
    """Trigger sync of users   Action can be \&quot;triggerFullSync\&quot; or \&quot;triggerChangedUsersSync\&quot;

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param action: 
    :type action: str

    """
    return web.Response(status=200)


async def realm_user_storage_id_unlink_users_post(request: web.Request, realm, id) -> web.Response:
    """Unlink imported users from a storage provider

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_user_storage_parent_id_mappers_id_sync_post(request: web.Request, realm, parent_id, id, direction=None) -> web.Response:
    """Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \&quot;fedToKeycloak\&quot; or \&quot;keycloakToFed\&quot;

    

    :param realm: realm name (not id!)
    :type realm: str
    :param parent_id: 
    :type parent_id: str
    :param id: 
    :type id: str
    :param direction: 
    :type direction: str

    """
    return web.Response(status=200)
