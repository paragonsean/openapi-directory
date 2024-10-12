from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.connection import Connection
from openapi_server.models.connection_import_data import ConnectionImportData
from openapi_server.models.create_connection_response import CreateConnectionResponse
from openapi_server.models.get_connection_response import GetConnectionResponse
from openapi_server.models.get_connections_response import GetConnectionsResponse
from openapi_server.models.get_custom_fields_response import GetCustomFieldsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_connection_response import UpdateConnectionResponse
from openapi_server import util


async def connection_settings_all(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, unified_api, service_id, resource) -> web.Response:
    """Get resource settings

    This endpoint returns custom settings and their defaults required by connection for a given resource. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param resource: Name of the resource (plural)
    :type resource: str

    """
    return web.Response(status=200)


async def connection_settings_update(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api, resource, body) -> web.Response:
    """Update settings

    Update default values for a connection&#39;s resource settings

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param resource: Name of the resource (plural)
    :type resource: str
    :param body: Fields that need to be updated on the resource
    :type body: dict | bytes

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)


async def connections_add(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api, body) -> web.Response:
    """Create connection

    Create an authorized connection 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param body: Fields that need to be persisted on the resource
    :type body: dict | bytes

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)


async def connections_all(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, api=None, configured=None) -> web.Response:
    """Get all connections

    This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param api: Scope results to Unified API
    :type api: str
    :param configured: Scopes results to connections that have been configured or not
    :type configured: bool

    """
    return web.Response(status=200)


async def connections_authorize(request: web.Request, service_id, application_id, state, redirect_uri, scope=None) -> web.Response:
    """Authorize

    __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 

    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param application_id: Application ID of the resource to return
    :type application_id: str
    :param state: An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
    :type state: str
    :param redirect_uri: URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
    :type redirect_uri: str
    :param scope: One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector&#39;s documentation for the available scopes.
    :type scope: List[str]

    """
    return web.Response(status=200)


async def connections_callback(request: web.Request, state, code) -> web.Response:
    """Callback

    This endpoint gets called after the triggering the authorize flow.  Callback links need a state and code parameter to verify the validity of the request. 

    :param state: An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
    :type state: str
    :param code: An authorization code from the connector which Apideck Vault will later exchange for an access token.
    :type code: str

    """
    return web.Response(status=200)


async def connections_delete(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api) -> web.Response:
    """Deletes a connection

    Deletes a connection

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str

    """
    return web.Response(status=200)


async def connections_import(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api, body) -> web.Response:
    """Import connection

    Import an authorized connection. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param body: Fields that need to be persisted on the resource
    :type body: dict | bytes

    """
    body = ConnectionImportData.from_dict(body)
    return web.Response(status=200)


async def connections_one(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api) -> web.Response:
    """Get connection

    Get a connection

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str

    """
    return web.Response(status=200)


async def connections_revoke(request: web.Request, service_id, application_id, state, redirect_uri) -> web.Response:
    """Revoke connection

    __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to revoke an existing OAuth connector.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 

    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param application_id: Application ID of the resource to return
    :type application_id: str
    :param state: An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
    :type state: str
    :param redirect_uri: URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
    :type redirect_uri: str

    """
    return web.Response(status=200)


async def connections_token(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api, body=None) -> web.Response:
    """Get Access Token

    Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.  Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def connections_update(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, service_id, unified_api, body) -> web.Response:
    """Update connection

    Update a connection

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param body: Fields that need to be updated on the resource
    :type body: dict | bytes

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)


async def custom_fields_all(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, unified_api, service_id, resource) -> web.Response:
    """Get resource custom fields

    This endpoint returns an custom fields on a connection resource. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param unified_api: Unified API
    :type unified_api: str
    :param service_id: Service ID of the resource to return
    :type service_id: str
    :param resource: Name of the resource (plural)
    :type resource: str

    """
    return web.Response(status=200)
