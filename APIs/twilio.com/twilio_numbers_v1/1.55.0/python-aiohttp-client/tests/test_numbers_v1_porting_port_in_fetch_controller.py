# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_v1_porting_port_in_fetch import NumbersV1PortingPortInFetch


pytestmark = pytest.mark.asyncio

async def test_fetch_porting_port_in_fetch(client):
    """Test case for fetch_porting_port_in_fetch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Porting/PortIn/{port_in_request_sid}'.format(port_in_request_sid='port_in_request_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

