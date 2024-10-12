# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_check(client):
    """Test case for check

    Gets details of a UK Vehicle
    """
    params = [('searchString', 'search_string_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/infiniteloopltd/CarRegistration/1.0.0/Check',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

