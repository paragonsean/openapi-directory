from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from openapi_server import util


async def v05_users_auth_fetch_modes_post_0(request: web.Request, authorization, body) -> web.Response:
    """Get a patient&#39;s authentication modes relevant to specified purpose

    This API is meant for identify supported authentication modes for a patient given a specific purpose 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthModeQueryRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_notify_post_0(request: web.Request, authorization, body) -> web.Response:
    """callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)

    This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)
