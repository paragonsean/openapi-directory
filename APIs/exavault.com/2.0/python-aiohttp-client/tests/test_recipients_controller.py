# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resend_invitations_request_body import ResendInvitationsRequestBody
from openapi_server.models.share_recipients_response import ShareRecipientsResponse


pytestmark = pytest.mark.asyncio

async def test_resend_invitations_for_share(client):
    """Test case for resend_invitations_for_share

    Resend invitations to share recipients
    """
    body = {"recipientId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/recipients/shares/invites/{share_id}'.format(share_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

