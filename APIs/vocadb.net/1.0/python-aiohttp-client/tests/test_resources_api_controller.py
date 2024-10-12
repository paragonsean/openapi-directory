# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_resources_culture_code_get(client):
    """Test case for api_resources_culture_code_get

    
    """
    params = [('setNames[]', ['set_names_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/resources/{culture_code}'.format(culture_code='culture_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

