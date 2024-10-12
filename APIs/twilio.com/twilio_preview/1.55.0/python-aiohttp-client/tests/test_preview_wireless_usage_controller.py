# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.preview_wireless_sim_usage import PreviewWirelessSimUsage


pytestmark = pytest.mark.asyncio

async def test_fetch_wireless_usage(client):
    """Test case for fetch_wireless_usage

    
    """
    params = [('End', 'end_example'),
                    ('Start', 'start_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/Sims/{sim_sid}/Usage'.format(sim_sid='sim_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

