# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verify_v2_service_entity_challenge_notification import VerifyV2ServiceEntityChallengeNotification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_notification(client):
    """Test case for create_notification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications'.format(service_sid='service_sid_example', identity='identity_example', challenge_sid='challenge_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

