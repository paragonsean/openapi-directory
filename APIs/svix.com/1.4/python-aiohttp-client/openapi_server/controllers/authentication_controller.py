from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_portal_access_in import AppPortalAccessIn
from openapi_server.models.app_portal_access_out import AppPortalAccessOut
from openapi_server.models.application_token_expire_in import ApplicationTokenExpireIn
from openapi_server.models.dashboard_access_out import DashboardAccessOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server import util


async def expire_all_api_v1_auth_app_app_id_expire_all_post(request: web.Request, app_id, body, idempotency_key=None) -> web.Response:
    """Expire All

    Expire all of the tokens associated with a specific Application

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = ApplicationTokenExpireIn.from_dict(body)
    return web.Response(status=200)


async def get_app_portal_access_api_v1_auth_app_portal_access_app_id_post(request: web.Request, app_id, body, idempotency_key=None) -> web.Response:
    """Get Consumer App Portal Access

    Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = AppPortalAccessIn.from_dict(body)
    return web.Response(status=200)


async def get_dashboard_access_api_v1_auth_dashboard_access_app_id_post(request: web.Request, app_id, idempotency_key=None) -> web.Response:
    """Get Dashboard Access

    DEPRECATED: Please use &#x60;app-portal-access&#x60; instead.  Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def logout_api_v1_auth_logout_post(request: web.Request, idempotency_key=None) -> web.Response:
    """Logout

    Logout an app token.  Trying to log out other tokens will fail.

    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)
