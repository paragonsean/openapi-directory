# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rtm_connect_error_schema import RtmConnectErrorSchema
from openapi_server.models.rtm_connect_schema import RtmConnectSchema


pytestmark = pytest.mark.asyncio

async def test_rtm_connect(client):
    """Test case for rtm_connect

    
    """
    params = [('token', 'token_example'),
                    ('batch_presence_aware', True),
                    ('presence_sub', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rtm.connect',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

