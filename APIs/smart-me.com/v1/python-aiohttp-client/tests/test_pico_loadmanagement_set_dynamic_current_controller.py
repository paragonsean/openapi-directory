# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_pico_loadmanagement_set_dynamic_current_post(client):
    """Test case for pico_loadmanagement_set_dynamic_current_post

    Sets the dynamic current of a load management group or a single station.
    """
    params = [('current', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/pico/loadmanagementgroup/current/{serial}'.format(serial=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

