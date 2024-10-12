from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.client_representation import ClientRepresentation
from openapi_server.models.client_scope_evaluate_resource_protocol_mapper_evaluation_representation import ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation
from openapi_server.models.client_scope_representation import ClientScopeRepresentation
from openapi_server.models.credential_representation import CredentialRepresentation
from openapi_server.models.global_request_result import GlobalRequestResult
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server.models.user_representation import UserRepresentation
from openapi_server.models.user_session_representation import UserSessionRepresentation
from openapi_server import util


async def realm_clients_get(request: web.Request, realm, client_id=None, first=None, max=None, search=None, viewable_only=None) -> web.Response:
    """Get clients belonging to the realm   Returns a list of clients belonging to the realm

    

    :param realm: realm name (not id!)
    :type realm: str
    :param client_id: filter by clientId
    :type client_id: str
    :param first: the first result
    :type first: int
    :param max: the max results to return
    :type max: int
    :param search: whether this is a search query or a getClientById query
    :type search: bool
    :param viewable_only: filter clients that cannot be viewed in full by admin
    :type viewable_only: bool

    """
    return web.Response(status=200)


async def realm_clients_id_client_secret_get(request: web.Request, realm, id) -> web.Response:
    """Get the client secret

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_client_secret_post(request: web.Request, realm, id) -> web.Response:
    """Generate a new secret for the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_default_client_scopes_client_scope_id_delete(request: web.Request, realm, id, client_scope_id) -> web.Response:
    """realm_clients_id_default_client_scopes_client_scope_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_clients_id_default_client_scopes_client_scope_id_put(request: web.Request, realm, id, client_scope_id) -> web.Response:
    """realm_clients_id_default_client_scopes_client_scope_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_clients_id_default_client_scopes_get(request: web.Request, realm, id) -> web.Response:
    """Get default client scopes.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_delete(request: web.Request, realm, id) -> web.Response:
    """Delete the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_evaluate_scopes_generate_example_access_token_get(request: web.Request, realm, id, scope=None, user_id=None) -> web.Response:
    """Create JSON with payload of example access token

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param scope: 
    :type scope: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def realm_clients_id_evaluate_scopes_protocol_mappers_get(request: web.Request, realm, id, scope=None) -> web.Response:
    """Return list of all protocol mappers, which will be used when generating tokens issued for particular client.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param scope: 
    :type scope: str

    """
    return web.Response(status=200)


async def realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get(request: web.Request, realm, id, role_container_id, scope=None) -> web.Response:
    """Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_container_id: either realm name OR client UUID
    :type role_container_id: str
    :param scope: 
    :type scope: str

    """
    return web.Response(status=200)


async def realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(request: web.Request, realm, id, role_container_id, scope=None) -> web.Response:
    """Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param role_container_id: either realm name OR client UUID
    :type role_container_id: str
    :param scope: 
    :type scope: str

    """
    return web.Response(status=200)


async def realm_clients_id_get(request: web.Request, realm, id) -> web.Response:
    """Get representation of the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_installation_providers_provider_id_get(request: web.Request, realm, id, provider_id) -> web.Response:
    """realm_clients_id_installation_providers_provider_id_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def realm_clients_id_management_permissions_get(request: web.Request, realm, id) -> web.Response:
    """Return object stating whether client Authorization permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_management_permissions_put(request: web.Request, realm, id, body) -> web.Response:
    """Return object stating whether client Authorization permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_nodes_node_delete(request: web.Request, realm, id, node) -> web.Response:
    """Unregister a cluster node from the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param node: 
    :type node: str

    """
    return web.Response(status=200)


async def realm_clients_id_nodes_post(request: web.Request, realm, id, body) -> web.Response:
    """Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def realm_clients_id_offline_session_count_get(request: web.Request, realm, id) -> web.Response:
    """Get application offline session count   Returns a number of offline user sessions associated with this client   {      \&quot;count\&quot;: number  }

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_offline_sessions_get(request: web.Request, realm, id, first=None, max=None) -> web.Response:
    """Get offline sessions for client   Returns a list of offline user sessions associated with this client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param first: Paging offset
    :type first: int
    :param max: Maximum results size (defaults to 100)
    :type max: int

    """
    return web.Response(status=200)


async def realm_clients_id_optional_client_scopes_client_scope_id_delete(request: web.Request, realm, id, client_scope_id) -> web.Response:
    """realm_clients_id_optional_client_scopes_client_scope_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_clients_id_optional_client_scopes_client_scope_id_put(request: web.Request, realm, id, client_scope_id) -> web.Response:
    """realm_clients_id_optional_client_scopes_client_scope_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param client_scope_id: 
    :type client_scope_id: str

    """
    return web.Response(status=200)


async def realm_clients_id_optional_client_scopes_get(request: web.Request, realm, id) -> web.Response:
    """Get optional client scopes.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_push_revocation_post(request: web.Request, realm, id) -> web.Response:
    """Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_put(request: web.Request, realm, id, body) -> web.Response:
    """Update the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_clients_id_registration_access_token_post(request: web.Request, realm, id) -> web.Response:
    """Generate a new registration access token for the client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_service_account_user_get(request: web.Request, realm, id) -> web.Response:
    """Get a user dedicated to the service account

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_session_count_get(request: web.Request, realm, id) -> web.Response:
    """Get application session count   Returns a number of user sessions associated with this client   {      \&quot;count\&quot;: number  }

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_test_nodes_available_get(request: web.Request, realm, id) -> web.Response:
    """Test if registered cluster nodes are available   Tests availability by sending &#39;ping&#39; request to all cluster nodes.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str

    """
    return web.Response(status=200)


async def realm_clients_id_user_sessions_get(request: web.Request, realm, id, first=None, max=None) -> web.Response:
    """Get user sessions for client   Returns a list of user sessions associated with this client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: id of client (not client-id)
    :type id: str
    :param first: Paging offset
    :type first: int
    :param max: Maximum results size (defaults to 100)
    :type max: int

    """
    return web.Response(status=200)


async def realm_clients_post(request: web.Request, realm, body) -> web.Response:
    """Create a new client   Client’s client_id must be unique!

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClientRepresentation.from_dict(body)
    return web.Response(status=200)
