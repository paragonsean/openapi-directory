# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getzipcodeinfo200_response import Getzipcodeinfo200Response


pytestmark = pytest.mark.asyncio

async def test_getzipcodeinfo(client):
    """Test case for getzipcodeinfo

    Gets detailed zip code information
    """
    params = [('license', 'license_example'),
                    ('zip', 'zip_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getzipcodeinfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

