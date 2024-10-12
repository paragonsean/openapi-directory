from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorization import Authorization
from openapi_server.models.authorization_post_request import AuthorizationPostRequest
from openapi_server.models.authorization_update_request import AuthorizationUpdateRequest
from openapi_server.models.authorizations import Authorizations
from openapi_server.models.error import Error
from openapi_server import util


async def delete_authorizations_id(request: web.Request, auth_id, zap_trace_span=None) -> web.Response:
    """Delete an authorization

    

    :param auth_id: The ID of the authorization to delete.
    :type auth_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_authorizations(request: web.Request, zap_trace_span=None, user_id=None, user=None, org_id=None, org=None) -> web.Response:
    """List all authorizations

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param user_id: Only show authorizations that belong to a user ID.
    :type user_id: str
    :param user: Only show authorizations that belong to a user name.
    :type user: str
    :param org_id: Only show authorizations that belong to an organization ID.
    :type org_id: str
    :param org: Only show authorizations that belong to a organization name.
    :type org: str

    """
    return web.Response(status=200)


async def get_authorizations_id(request: web.Request, auth_id, zap_trace_span=None) -> web.Response:
    """Retrieve an authorization

    

    :param auth_id: The ID of the authorization to get.
    :type auth_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_authorizations_id(request: web.Request, auth_id, body, zap_trace_span=None) -> web.Response:
    """Update an authorization to be active or inactive

    

    :param auth_id: The ID of the authorization to update.
    :type auth_id: str
    :param body: Authorization to update
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AuthorizationUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def post_authorizations(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create an authorization

    

    :param body: Authorization to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AuthorizationPostRequest.from_dict(body)
    return web.Response(status=200)
