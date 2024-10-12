from typing import List, Dict
from aiohttp import web

from openapi_server.models.o_auth2_permission_grant import OAuth2PermissionGrant
from openapi_server import util


async def o_auth2_permission_grant_create(request: web.Request, api_version, tenant_id, body=None) -> web.Response:
    """o_auth2_permission_grant_create

    Grants OAuth2 permissions for the relevant resource Ids of an app.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: The relevant app Service Principal Object Id and the Service Principal Object Id you want to grant.
    :type body: dict | bytes

    """
    body = OAuth2PermissionGrant.from_dict(body)
    return web.Response(status=200)
