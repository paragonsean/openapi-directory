# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sync_v1_service_sync_stream_stream_message import SyncV1ServiceSyncStreamStreamMessage


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_stream_message(client):
    """Test case for create_stream_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'data': None
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Streams/{stream_sid}/Messages'.format(service_sid='service_sid_example', stream_sid='stream_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

