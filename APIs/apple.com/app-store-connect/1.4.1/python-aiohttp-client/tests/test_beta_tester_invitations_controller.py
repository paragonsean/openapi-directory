# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beta_tester_invitation_create_request import BetaTesterInvitationCreateRequest
from openapi_server.models.beta_tester_invitation_response import BetaTesterInvitationResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_tester_invitations_create_instance(client):
    """Test case for beta_tester_invitations_create_instance

    
    """
    body = {"data":{"relationships":{"app":{"data":{"id":"id","type":"apps"}},"betaTester":{"data":{"id":"id","type":"betaTesters"}}},"type":"betaTesterInvitations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaTesterInvitations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

