# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.channel_enum_webhook_enabled_type import ChannelEnumWebhookEnabledType
from openapi_server.models.chat_v3_channel import ChatV3Channel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_channel(client):
    """Test case for update_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.ChannelEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'messaging_service_sid': 'messaging_service_sid_example',
        'type': openapi_server.ChannelEnumChannelType()
        }
    response = await client.request(
        method='POST',
        path='/v3/Services/{service_sid}/Channels/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

