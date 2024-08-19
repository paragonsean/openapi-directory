from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_public_v1_policies_types_contacts_get200_response import ApiPublicV1PoliciesTypesContactsGet200Response
from openapi_server.models.api_public_v1_policies_types_notifications_get200_response import ApiPublicV1PoliciesTypesNotificationsGet200Response
from openapi_server.models.api_public_v1_policies_types_timeouts_get200_response import ApiPublicV1PoliciesTypesTimeoutsGet200Response
from openapi_server import util


async def api_public_v1_policies_types_contacts_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get the available contact types

    Get the available contact types  description: \&quot;Email Address\&quot;, type: \&quot;email\&quot; description: \&quot;Phone Number\&quot;, type: \&quot;phone\&quot;  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_policies_types_notifications_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get the available notification types

    Get the available notification types  description: \&quot;Send a push notification to all my devices\&quot;, type: \&quot;push\&quot; description: \&quot;Send an email to an email address\&quot;, type: \&quot;email\&quot; description: \&quot;Send an SMS to a phone number\&quot;, type: \&quot;sms\&quot; description: \&quot;Make a phone call to a phone number\&quot;, type: \&quot;phone\&quot;  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_policies_types_timeouts_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get the available timeout values

    Get the available timeout values  description: \&quot;If still unacked after 1 minute\&quot;, type: 1 description: \&quot;If still unacked after 5 minutes\&quot;, type: 5 description: \&quot;If still unacked after 10 minutes\&quot;, type: 10 description: \&quot;If still unacked after 15 minutes\&quot;, type: 15 description: \&quot;If still unacked after 20 minutes\&quot;, type: 20 description: \&quot;If still unacked after 25 minutes\&quot;, type: 25 description: \&quot;If still unacked after 30 minutes\&quot;, type: 30 description: \&quot;If still unacked after 45 minutes\&quot;, type: 45 description: \&quot;If still unacked after 60 minutes\&quot;, type: 60  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)
