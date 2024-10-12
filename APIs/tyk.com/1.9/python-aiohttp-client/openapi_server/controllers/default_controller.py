from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_definition import APIDefinition
from openapi_server.models.o_auth_client import OAuthClient
from openapi_server.models.session_object import SessionObject
from openapi_server.models.tyk_apis_api_id_delete200_response import TykApisApiIDDelete200Response
from openapi_server.models.tyk_apis_post200_response import TykApisPost200Response
from openapi_server.models.tyk_health_get200_response import TykHealthGet200Response
from openapi_server.models.tyk_keys_create_post200_response import TykKeysCreatePost200Response
from openapi_server.models.tyk_keys_get200_response import TykKeysGet200Response
from openapi_server.models.tyk_keys_key_id_post200_response import TykKeysKeyIdPost200Response
from openapi_server.models.tyk_keys_key_id_put200_response import TykKeysKeyIdPut200Response
from openapi_server.models.tyk_oauth_authorize_client_post200_response import TykOauthAuthorizeClientPost200Response
from openapi_server.models.tyk_oauth_clients_create_post_request import TykOauthClientsCreatePostRequest
from openapi_server.models.tyk_reload_get200_response import TykReloadGet200Response
from openapi_server import util


async def tyk_apis_api_iddelete(request: web.Request, x_tyk_authorization, api_id) -> web.Response:
    """tyk_apis_api_iddelete

    Deletes an *API Definition* object, if it exists 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param api_id: API ID
    :type api_id: str

    """
    return web.Response(status=200)


async def tyk_apis_api_idget(request: web.Request, x_tyk_authorization, api_id) -> web.Response:
    """tyk_apis_api_idget

    Gets an *API Definition* object, if it exists 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param api_id: API ID
    :type api_id: str

    """
    return web.Response(status=200)


async def tyk_apis_api_idput(request: web.Request, x_tyk_authorization, api_id, api_definition=None) -> web.Response:
    """tyk_apis_api_idput

    Updates an *API Definition* object, if it exists 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param api_id: API ID
    :type api_id: str
    :param api_definition: 
    :type api_definition: dict | bytes

    """
    api_definition = APIDefinition.from_dict(api_definition)
    return web.Response(status=200)


async def tyk_apis_get(request: web.Request, x_tyk_authorization) -> web.Response:
    """tyk_apis_get

    Gets a list of *API Definition* objects that are currently live on the gateway  

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str

    """
    return web.Response(status=200)


async def tyk_apis_post(request: web.Request, api_definition=None) -> web.Response:
    """tyk_apis_post

    Create an *API Definition* object 

    :param api_definition: 
    :type api_definition: dict | bytes

    """
    api_definition = APIDefinition.from_dict(api_definition)
    return web.Response(status=200)


async def tyk_health_get(request: web.Request, x_tyk_authorization, api_id) -> web.Response:
    """tyk_health_get

    Gets the health check values for an API if it is being recorded 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param api_id: API ID to query
    :type api_id: str

    """
    return web.Response(status=200)


async def tyk_keys_create_post(request: web.Request, x_tyk_authorization, suppress_reset=None, session_object=None) -> web.Response:
    """tyk_keys_create_post

    Create a new *API token* with the *session object* defined in the body 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param suppress_reset: Adding the &#x60;suppress_reset&#x60; parameter and setting it to &#x60;1&#x60;, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the &#x60;suppress_reset&#x60; flag to the URL parameters will avoid this behaviour.
    :type suppress_reset: 
    :param session_object: 
    :type session_object: dict | bytes

    """
    session_object = SessionObject.from_dict(session_object)
    return web.Response(status=200)


async def tyk_keys_get(request: web.Request, api_id, x_tyk_authorization) -> web.Response:
    """tyk_keys_get

    Gets a list of *key* IDs (will only work with non-hashed installations) 

    :param api_id: Back-end to target
    :type api_id: str
    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str

    """
    return web.Response(status=200)


async def tyk_keys_key_id_delete(request: web.Request, x_tyk_authorization, key_id, api_id) -> web.Response:
    """tyk_keys_key_id_delete

    Remove this *API token* from the gateway, this will completely destroy the token and metadata associated with the token and instantly stop access from being granted 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param key_id: Access Token
    :type key_id: str
    :param api_id: Back-end to target
    :type api_id: str

    """
    return web.Response(status=200)


async def tyk_keys_key_id_post(request: web.Request, x_tyk_authorization, key_id, session_object=None) -> web.Response:
    """tyk_keys_key_id_post

    Add a pre-specified *API token* with the *session object* defined in the body, this operatin creates a custom token that dsoes not use the gateway naming convention for tokens 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param key_id: Access Token
    :type key_id: str
    :param session_object: 
    :type session_object: dict | bytes

    """
    session_object = SessionObject.from_dict(session_object)
    return web.Response(status=200)


async def tyk_keys_key_id_put(request: web.Request, x_tyk_authorization, key_id, api_id, suppress_reset=None, session_object=None) -> web.Response:
    """tyk_keys_key_id_put

    Update an *API token* with the *session object* defined in the body, this operatin overwrites the existing object 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param key_id: Access Token
    :type key_id: str
    :param api_id: Back-end to target
    :type api_id: str
    :param suppress_reset: Adding the &#x60;suppress_reset&#x60; parameter and setting it to &#x60;1&#x60;, will cause Tyk to not reset the quota limit that is in the current live quota manager. By default Tyk will reset the quota in the live quota manager (initialising it) when ADDing a key. Adding the &#x60;suppress_reset&#x60; flag to the URL parameters will avoid this behaviour.
    :type suppress_reset: 
    :param session_object: 
    :type session_object: dict | bytes

    """
    session_object = SessionObject.from_dict(session_object)
    return web.Response(status=200)


async def tyk_oauth_authorize_client_post(request: web.Request, x_tyk_authorization, response_type, client_id, redirect_uri, key_rules) -> web.Response:
    """tyk_oauth_authorize_client_post

    The final request from an authorising party for a redirect URI during the Tyk OAuth flow 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param response_type: Should be provided by requesting client as part of authorisation request, this should be either &#x60;code&#x60; or &#x60;token&#x60; depending on the methods you have specified for the API
    :type response_type: str
    :param client_id: Should be provided by requesting client as part of authorisation request. The Client ID that is making the request
    :type client_id: str
    :param redirect_uri: Should be provided by requesting client as part of authorisation request. Must match with the record stored with Tyk
    :type redirect_uri: str
    :param key_rules: A string representation of a *Session Object (form-encoded)*. This should be provided by your application in order to apply any quotas or rules to the key
    :type key_rules: str

    """
    return web.Response(status=200)


async def tyk_oauth_clients_api_id_client_id_delete(request: web.Request, x_tyk_authorization, api_id, client_id) -> web.Response:
    """tyk_oauth_clients_api_id_client_id_delete

    Delete the OAuth client 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param api_id: API ID that owns this client (back end)
    :type api_id: str
    :param client_id: OAuth Client ID to delete
    :type client_id: str

    """
    return web.Response(status=200)


async def tyk_oauth_clients_api_id_get(request: web.Request, x_tyk_authorization, api_id) -> web.Response:
    """tyk_oauth_clients_api_id_get

    Get a list of OAuth clients bound to this back end  

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param api_id: API ID that owns this client (back end)
    :type api_id: str

    """
    return web.Response(status=200)


async def tyk_oauth_clients_create_post(request: web.Request, x_tyk_authorization, oauth_client=None) -> web.Response:
    """tyk_oauth_clients_create_post

    Create a new OAuth client 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param oauth_client: 
    :type oauth_client: dict | bytes

    """
    oauth_client = TykOauthClientsCreatePostRequest.from_dict(oauth_client)
    return web.Response(status=200)


async def tyk_oauth_refresh_key_id_delete(request: web.Request, x_tyk_authorization, key_id, api_id) -> web.Response:
    """tyk_oauth_refresh_key_id_delete

    Invalidate a refresh token 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str
    :param key_id: Access Token
    :type key_id: str
    :param api_id: API ID
    :type api_id: str

    """
    return web.Response(status=200)


async def tyk_reload_get(request: web.Request, x_tyk_authorization) -> web.Response:
    """tyk_reload_get

    Will reload the targetted gateway 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str

    """
    return web.Response(status=200)


async def tyk_reload_group_get(request: web.Request, x_tyk_authorization) -> web.Response:
    """tyk_reload_group_get

    Will reload the cluster via the targeted gateway 

    :param x_tyk_authorization: tyk gateway shared secret
    :type x_tyk_authorization: str

    """
    return web.Response(status=200)
