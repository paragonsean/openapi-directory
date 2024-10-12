from typing import List, Dict
from aiohttp import web

from openapi_server.models.resend_invitations_request_body import ResendInvitationsRequestBody
from openapi_server.models.share_recipients_response import ShareRecipientsResponse
from openapi_server import util


async def resend_invitations_for_share(request: web.Request, ev_api_key, ev_access_token, share_id, body=None) -> web.Response:
    """Resend invitations to share recipients

    Resend invitations to one or all recipients attached to specified share. The most recent message that was sent for the share will be re-used for this email.  You can use [GET /shares/{id}](#operation/getShareById) to view the recipient list and message history for a share. Use [PATCH /shares/{id}](#operation/updateShareById) to add or remove recipients.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param share_id: ID of the share to resend invites for.
    :type share_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ResendInvitationsRequestBody.from_dict(body)
    return web.Response(status=200)
