# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getglobaltime200_response import Getglobaltime200Response


pytestmark = pytest.mark.asyncio

async def test_getglobaltime(client):
    """Test case for getglobaltime

    Gets the current time for a global locale
    """
    params = [('license', 'license_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getglobaltime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

