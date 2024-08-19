from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_my_details200_response import GetMyDetails200Response
from openapi_server.models.get_user_details200_response import GetUserDetails200Response
from openapi_server.models.modify_project_notification_settings_request import ModifyProjectNotificationSettingsRequest
from openapi_server.models.org_org_id_notification_settings_get200_response import OrgOrgIdNotificationSettingsGet200Response
from openapi_server.models.set_notification_settings_request import SetNotificationSettingsRequest
from openapi_server import util


async def get_my_details(request: web.Request, ) -> web.Response:
    """Get My Details

    


    """
    return web.Response(status=200)


async def get_organization_notification_settings(request: web.Request, org_id) -> web.Response:
    """Get organization notification settings

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str

    """
    return web.Response(status=200)


async def get_project_notification_settings(request: web.Request, org_id, project_id) -> web.Response:
    """Get project notification settings

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to return notification settings for.
    :type project_id: str

    """
    return web.Response(status=200)


async def get_user_details(request: web.Request, user_id) -> web.Response:
    """Get User Details

    

    :param user_id: The users ID. The &#x60;API_KEY&#x60; must have admin access to at least one group or organization where the requested user is a member and must have the &#x60;api&#x60; entitlement on their preferred organization.
    :type user_id: str

    """
    return web.Response(status=200)


async def modify_organization_notification_settings(request: web.Request, org_id, body=None) -> web.Response:
    """Modify organization notification settings

    

    :param org_id: Automatically added
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetNotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def modify_project_notification_settings(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Modify project notification settings

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyProjectNotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)
