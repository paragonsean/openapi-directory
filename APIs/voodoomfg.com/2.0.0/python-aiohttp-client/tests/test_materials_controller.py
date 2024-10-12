# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.material import Material


pytestmark = pytest.mark.asyncio

async def test_materials_get(client):
    """Test case for materials_get

    Voodoo Manufacturing offers printing in a number of different materials, with different color options for each. Your organization can expose as many or as few material options as you want to your end-customer. 
    """
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/materials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

