# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gsi_dispatch200_response import GsiDispatch200Response


pytestmark = pytest.mark.asyncio

async def test_gsi_dispatch_0(client):
    """Test case for gsi_dispatch_0

    Dispatch (Green Energy Distribution Schedule)
    """
    params = [('zip', 'zip_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/gsi/dispatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

