# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_vendor_get(client):
    """Test case for get_vendor_get

    This endpoint returns a single vendor by their 9 digit DUNS number
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/vendor/{duns}'.format(duns='duns_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

