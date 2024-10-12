from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.org_settings import OrgSettings
from openapi_server.models.v2_orgs_name_settings_put_request import V2OrgsNameSettingsPutRequest
from openapi_server import util


async def v2_orgs_name_settings_get(request: web.Request, name) -> web.Response:
    """Get organization settings

    Returns organization settings by name. 

    :param name: Name of the organization.
    :type name: str

    """
    return web.Response(status=200)


async def v2_orgs_name_settings_put(request: web.Request, name, body) -> web.Response:
    """Update organization settings

    Updates an organization&#39;s settings. Some settings are only used when the organization is on a business plan.  ***Only users in the \&quot;owners\&quot; group of the organization can use this endpoint.***  The following settings are only used on a business plan: - &#x60;restricted_images&#x60; 

    :param name: Name of the organization.
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = V2OrgsNameSettingsPutRequest.from_dict(body)
    return web.Response(status=200)
