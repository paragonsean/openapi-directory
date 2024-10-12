from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_event_representation import AdminEventRepresentation
from openapi_server.models.client_representation import ClientRepresentation
from openapi_server.models.client_scope_representation import ClientScopeRepresentation
from openapi_server.models.event_representation import EventRepresentation
from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.partial_import_representation import PartialImportRepresentation
from openapi_server.models.realm_events_config_representation import RealmEventsConfigRepresentation
from openapi_server.models.realm_representation import RealmRepresentation
from openapi_server.models.test_ldap_connection_representation import TestLdapConnectionRepresentation
from openapi_server import util


async def realm_admin_events_delete(request: web.Request, realm) -> web.Response:
    """Delete all admin events

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_admin_events_get(request: web.Request, realm, auth_client=None, auth_ip_address=None, auth_realm=None, auth_user=None, date_from=None, date_to=None, first=None, max=None, operation_types=None, _resource_path=None, resource_types=None) -> web.Response:
    """Get admin events   Returns all admin events, or filters events based on URL query parameters listed here

    

    :param realm: realm name (not id!)
    :type realm: str
    :param auth_client: 
    :type auth_client: str
    :param auth_ip_address: 
    :type auth_ip_address: str
    :param auth_realm: 
    :type auth_realm: str
    :param auth_user: user id
    :type auth_user: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param first: 
    :type first: int
    :param max: Maximum results size (defaults to 100)
    :type max: int
    :param operation_types: 
    :type operation_types: List[str]
    :param _resource_path: 
    :type _resource_path: str
    :param resource_types: 
    :type resource_types: List[str]

    """
    return web.Response(status=200)


async def realm_clear_keys_cache_post(request: web.Request, realm) -> web.Response:
    """Clear cache of external public keys (Public keys of clients or Identity providers)

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_clear_realm_cache_post(request: web.Request, realm) -> web.Response:
    """Clear realm cache

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_clear_user_cache_post(request: web.Request, realm) -> web.Response:
    """Clear user cache

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_client_description_converter_post(request: web.Request, realm, body) -> web.Response:
    """Base path for importing clients under this realm.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def realm_client_session_stats_get(request: web.Request, realm) -> web.Response:
    """Get client session stats   Returns a JSON map.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_credential_registrators_get(request: web.Request, realm) -> web.Response:
    """realm_credential_registrators_get

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_default_default_client_scopes_client_scope_id_delete(request: web.Request, realm, client_scope_id) -> web.Response:
    """realm_default_default_client_scopes_client_scope_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_default_default_client_scopes_client_scope_id_put(request: web.Request, realm, client_scope_id) -> web.Response:
    """realm_default_default_client_scopes_client_scope_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_default_default_client_scopes_get(request: web.Request, realm) -> web.Response:
    """Get realm default client scopes.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_default_groups_get(request: web.Request, realm) -> web.Response:
    """Get group hierarchy.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_default_groups_group_id_delete(request: web.Request, realm, group_id) -> web.Response:
    """realm_default_groups_group_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def realm_default_groups_group_id_put(request: web.Request, realm, group_id) -> web.Response:
    """realm_default_groups_group_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def realm_default_optional_client_scopes_client_scope_id_delete(request: web.Request, realm, client_scope_id) -> web.Response:
    """realm_default_optional_client_scopes_client_scope_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_default_optional_client_scopes_client_scope_id_put(request: web.Request, realm, client_scope_id) -> web.Response:
    """realm_default_optional_client_scopes_client_scope_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_default_optional_client_scopes_get(request: web.Request, realm) -> web.Response:
    """Get realm optional client scopes.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_delete(request: web.Request, realm) -> web.Response:
    """Delete the realm

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_events_config_get(request: web.Request, realm) -> web.Response:
    """Get the events provider configuration   Returns JSON object with events provider configuration

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_events_config_put(request: web.Request, realm, body) -> web.Response:
    """Update the events provider   Change the events provider and/or its configuration

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = RealmEventsConfigRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_events_delete(request: web.Request, realm) -> web.Response:
    """Delete all events

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_events_get(request: web.Request, realm, client=None, date_from=None, date_to=None, first=None, ip_address=None, max=None, type=None, user=None) -> web.Response:
    """Get events   Returns all events, or filters them based on URL query parameters listed here

    

    :param realm: realm name (not id!)
    :type realm: str
    :param client: App or oauth client name
    :type client: str
    :param date_from: From date
    :type date_from: str
    :param date_to: To date
    :type date_to: str
    :param first: Paging offset
    :type first: int
    :param ip_address: IP address
    :type ip_address: str
    :param max: Maximum results size (defaults to 100)
    :type max: int
    :param type: The types of events to return
    :type type: List[str]
    :param user: User id
    :type user: str

    """
    return web.Response(status=200)


async def realm_get(request: web.Request, realm) -> web.Response:
    """Get the top-level representation of the realm   It will not include nested information like User and Client representations.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_group_by_path_path_get(request: web.Request, realm, path) -> web.Response:
    """realm_group_by_path_path_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param path: 
    :type path: str

    """
    return web.Response(status=200)


async def realm_logout_all_post(request: web.Request, realm) -> web.Response:
    """Removes all user sessions.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_partial_export_post(request: web.Request, realm, export_clients=None, export_groups_and_roles=None) -> web.Response:
    """Partial export of existing realm into a JSON file.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param export_clients: 
    :type export_clients: bool
    :param export_groups_and_roles: 
    :type export_groups_and_roles: bool

    """
    return web.Response(status=200)


async def realm_partial_import_post(request: web.Request, realm, body) -> web.Response:
    """Partial import from a JSON file to an existing realm.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = PartialImportRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_push_revocation_post(request: web.Request, realm) -> web.Response:
    """Push the realm’s revocation policy to any client that has an admin url associated with it.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_put(request: web.Request, realm, body) -> web.Response:
    """Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = RealmRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_sessions_session_delete(request: web.Request, realm, session) -> web.Response:
    """Remove a specific user session.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param session: 
    :type session: str

    """
    return web.Response(status=200)


async def realm_test_ldap_connection_post(request: web.Request, realm, body) -> web.Response:
    """Test LDAP connection

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestLdapConnectionRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_test_smtp_connection_post(request: web.Request, realm, body) -> web.Response:
    """realm_test_smtp_connection_post

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def realm_users_management_permissions_get(request: web.Request, realm) -> web.Response:
    """realm_users_management_permissions_get

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_users_management_permissions_put(request: web.Request, realm, body) -> web.Response:
    """realm_users_management_permissions_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def root_post(request: web.Request, body) -> web.Response:
    """Import a realm   Imports a realm from a full representation of that realm.

    

    :param body: JSON representation of the realm
    :type body: dict | bytes

    """
    body = RealmRepresentation.from_dict(body)
    return web.Response(status=200)
