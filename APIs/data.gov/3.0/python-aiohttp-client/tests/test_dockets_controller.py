# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_docket(client):
    """Test case for docket

    Returns Docket information
    """
    params = [('docketId', 'EPA-HQ-OAR-2011-0028')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/regulations/v3/docket.{response_format}'.format(response_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

