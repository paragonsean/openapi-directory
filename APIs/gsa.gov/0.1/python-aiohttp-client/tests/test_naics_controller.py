# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_naics_get(client):
    """Test case for list_naics_get

    This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/naics/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

