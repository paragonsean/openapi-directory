# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_server_configuration_request import EditServerConfigurationRequest
from openapi_server.models.server_configuration_response import ServerConfigurationResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_edit_current_server_configuration(client):
    """Test case for edit_current_server_configuration

    Edit Server Configuration
    """
    body = {"ClickHookUrl":"ClickHookUrl","Color":"purple","DeliveryHookUrl":"DeliveryHookUrl","RawEmailEnabled":True,"TrackLinks":"None","InboundSpamThreshold":0,"OpenHookUrl":"OpenHookUrl","BounceHookUrl":"BounceHookUrl","InboundHookUrl":"InboundHookUrl","Name":"Name","TrackOpens":True,"PostFirstOpenOnly":True,"InboundDomain":"InboundDomain","SmtpApiActivated":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/server',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_current_server_configuration(client):
    """Test case for get_current_server_configuration

    Get Server Configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/server',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

