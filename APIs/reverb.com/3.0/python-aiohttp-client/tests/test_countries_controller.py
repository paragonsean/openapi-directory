# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_countries_get(client):
    """Test case for countries_get

    Retrieve a list of country codes with corresponding subregions
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

