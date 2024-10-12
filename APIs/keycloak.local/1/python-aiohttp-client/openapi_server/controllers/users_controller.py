from typing import List, Dict
from aiohttp import web

from openapi_server.models.credential_representation import CredentialRepresentation
from openapi_server.models.federated_identity_representation import FederatedIdentityRepresentation
from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.user_representation import UserRepresentation
from openapi_server.models.user_session_representation import UserSessionRepresentation
from openapi_server import util


async def realm_users_count_get(request: web.Request, realm, email=None, first_name=None, last_name=None, search=None, username=None) -> web.Response:
    """Returns the number of users that match the given criteria.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param email: email filter
    :type email: str
    :param first_name: first name filter
    :type first_name: str
    :param last_name: last name filter
    :type last_name: str
    :param search: arbitrary search string for all the fields below
    :type search: str
    :param username: username filter
    :type username: str

    """
    return web.Response(status=200)


async def realm_users_get(request: web.Request, realm, brief_representation=None, email=None, first=None, first_name=None, last_name=None, max=None, search=None, username=None) -> web.Response:
    """Get users   Returns a list of users, filtered according to query parameters

    

    :param realm: realm name (not id!)
    :type realm: str
    :param brief_representation: 
    :type brief_representation: bool
    :param email: 
    :type email: str
    :param first: 
    :type first: int
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param max: Maximum results size (defaults to 100)
    :type max: int
    :param search: A String contained in username, first or last name, or email
    :type search: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def realm_users_id_configured_user_storage_credential_types_get(request: web.Request, realm, id) -> web.Response:
    """Return credential types, which are provided by the user storage where user is stored.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_consents_client_delete(request: web.Request, realm, id, client) -> web.Response:
    """Revoke consent and offline tokens for particular client from user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client: Client id
    :type client: str

    """
    return web.Response(status=200)


async def realm_users_id_consents_get(request: web.Request, realm, id) -> web.Response:
    """Get consents granted by the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_credentials_credential_id_delete(request: web.Request, realm, id, credential_id) -> web.Response:
    """Remove a credential for a user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param credential_id: 
    :type credential_id: str

    """
    return web.Response(status=200)


async def realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post(request: web.Request, realm, id, credential_id, new_previous_credential_id) -> web.Response:
    """Move a credential to a position behind another credential

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param credential_id: The credential to move
    :type credential_id: str
    :param new_previous_credential_id: The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list.
    :type new_previous_credential_id: str

    """
    return web.Response(status=200)


async def realm_users_id_credentials_credential_id_move_to_first_post(request: web.Request, realm, id, credential_id) -> web.Response:
    """Move a credential to a first position in the credentials list of the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param credential_id: The credential to move
    :type credential_id: str

    """
    return web.Response(status=200)


async def realm_users_id_credentials_credential_id_user_label_put(request: web.Request, realm, id, credential_id, body) -> web.Response:
    """Update a credential label for a user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param credential_id: 
    :type credential_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def realm_users_id_credentials_get(request: web.Request, realm, id) -> web.Response:
    """realm_users_id_credentials_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_delete(request: web.Request, realm, id) -> web.Response:
    """Delete the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_disable_credential_types_put(request: web.Request, realm, id, body) -> web.Response:
    """Disable all credentials for a user of a specific type

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def realm_users_id_execute_actions_email_put(request: web.Request, realm, id, body, client_id=None, lifespan=None, redirect_uri=None) -> web.Response:
    """Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param body: required actions the user needs to complete
    :type body: List[str]
    :param client_id: Client id
    :type client_id: str
    :param lifespan: Number of seconds after which the generated token expires
    :type lifespan: int
    :param redirect_uri: Redirect uri
    :type redirect_uri: str

    """
    return web.Response(status=200)


async def realm_users_id_federated_identity_get(request: web.Request, realm, id) -> web.Response:
    """Get social logins associated with the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_federated_identity_provider_delete(request: web.Request, realm, id, provider) -> web.Response:
    """Remove a social login provider from user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param provider: Social login provider id
    :type provider: str

    """
    return web.Response(status=200)


async def realm_users_id_federated_identity_provider_post(request: web.Request, realm, id, provider, body) -> web.Response:
    """Add a social login provider to the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param provider: Social login provider id
    :type provider: str
    :param body: 
    :type body: dict | bytes

    """
    body = FederatedIdentityRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_users_id_get(request: web.Request, realm, id) -> web.Response:
    """Get representation of the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_groups_count_get(request: web.Request, realm, id, search=None) -> web.Response:
    """realm_users_id_groups_count_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def realm_users_id_groups_get(request: web.Request, realm, id, brief_representation=None, first=None, max=None, search=None) -> web.Response:
    """realm_users_id_groups_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param brief_representation: 
    :type brief_representation: bool
    :param first: 
    :type first: int
    :param max: 
    :type max: int
    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def realm_users_id_groups_group_id_delete(request: web.Request, realm, id, group_id) -> web.Response:
    """realm_users_id_groups_group_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def realm_users_id_groups_group_id_put(request: web.Request, realm, id, group_id) -> web.Response:
    """realm_users_id_groups_group_id_put

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def realm_users_id_impersonation_post(request: web.Request, realm, id) -> web.Response:
    """Impersonate the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_logout_post(request: web.Request, realm, id) -> web.Response:
    """Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_id_offline_sessions_client_id_get(request: web.Request, realm, id, client_id) -> web.Response:
    """Get offline sessions associated with the user and client

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def realm_users_id_put(request: web.Request, realm, id, body) -> web.Response:
    """Update the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_users_id_reset_password_put(request: web.Request, realm, id, body) -> web.Response:
    """Set up a new password for the user.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param body: The representation must contain a rawPassword with the plain-text password
    :type body: dict | bytes

    """
    body = CredentialRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_users_id_send_verify_email_put(request: web.Request, realm, id, client_id=None, redirect_uri=None) -> web.Response:
    """Send an email-verification email to the user   An email contains a link the user can click to verify their email address.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str
    :param client_id: Client id
    :type client_id: str
    :param redirect_uri: Redirect uri
    :type redirect_uri: str

    """
    return web.Response(status=200)


async def realm_users_id_sessions_get(request: web.Request, realm, id) -> web.Response:
    """Get sessions associated with the user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: User id
    :type id: str

    """
    return web.Response(status=200)


async def realm_users_post(request: web.Request, realm, body) -> web.Response:
    """Create a new user   Username must be unique.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserRepresentation.from_dict(body)
    return web.Response(status=200)
