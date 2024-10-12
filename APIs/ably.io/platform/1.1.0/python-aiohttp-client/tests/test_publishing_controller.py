# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.message import Message
from openapi_server.models.publish_messages_to_channel2_xx_response import PublishMessagesToChannel2XXResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_publish_messages_to_channel(client):
    """Test case for publish_messages_to_channel

    Publish a message to a channel
    """
    body = {"clientId":"clientId","data":"data","name":"name","connectionId":"connectionId","extras":{"push":{"fcm":{"notification":{"collapseKey":"collapseKey","sound":"sound","icon":"icon","body":"body","title":"title"}},"notification":{"collapseKey":"collapseKey","sound":"sound","icon":"icon","body":"body","title":"title"},"data":"data","web":{"notification":{"collapseKey":"collapseKey","sound":"sound","icon":"icon","body":"body","title":"title"}},"apns":{"notification":{"collapseKey":"collapseKey","sound":"sound","icon":"icon","body":"body","title":"title"}}}},"id":"id","encoding":"encoding","timestamp":0}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_id}/messages'.format(channel_id='channel_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

