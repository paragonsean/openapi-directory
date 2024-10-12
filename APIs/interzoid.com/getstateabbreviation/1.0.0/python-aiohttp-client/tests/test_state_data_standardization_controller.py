# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getstateabbreviation200_response import Getstateabbreviation200Response


pytestmark = pytest.mark.asyncio

async def test_getstateabbreviation(client):
    """Test case for getstateabbreviation

    Gets a two-letter abbreviation for a state or province name data
    """
    params = [('license', 'license_example'),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getstateabbreviation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

