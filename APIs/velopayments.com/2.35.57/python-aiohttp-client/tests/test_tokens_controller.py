# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.resend_token_request import ResendTokenRequest


pytestmark = pytest.mark.asyncio

async def test_resend_token(client):
    """Test case for resend_token

    Resend a token
    """
    body = {"tokenType":"INVITE_MFA_USER","verificationCode":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/tokens'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

