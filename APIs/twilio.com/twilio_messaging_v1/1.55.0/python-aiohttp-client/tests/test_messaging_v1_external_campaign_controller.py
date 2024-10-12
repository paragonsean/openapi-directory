# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_external_campaign import MessagingV1ExternalCampaign


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_external_campaign(client):
    """Test case for create_external_campaign

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'campaign_id': 'campaign_id_example',
        'messaging_service_sid': 'messaging_service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/PreregisteredUsa2p',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

