# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getfullnamematch200_response import Getfullnamematch200Response


pytestmark = pytest.mark.asyncio

async def test_getfullnamematch(client):
    """Test case for getfullnamematch

    Gets a similarity key for matching purposes for full name data
    """
    params = [('license', 'license_example'),
                    ('fullname', 'fullname_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getfullnamematch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

